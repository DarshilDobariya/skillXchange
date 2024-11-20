from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from store.models.customer import Customer
from store.models.connection import ConnectionRequest
from store.models.meetings import Meeting
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.db.models import Q


def schedule_meeting_page(request):
    main_customer_id = request.session.get('customer')
    senderObject = Customer.objects.filter(id=main_customer_id).first()
    connected_customers = ConnectionRequest.objects.filter(
        (Q(sender=senderObject) | Q(receiver=senderObject)) & 
        Q(status="accepted")
    ).exclude(id=main_customer_id)
    customers = [
        conn.receiver if conn.sender == senderObject else conn.sender
        for conn in connected_customers
    ]
    return render(request, 'schedule_meeting.html', {'connected_customers': customers})

@csrf_exempt
def schedule_meeting(request):
    if request.method == 'POST':
        print('we are here')
        data = json.loads(request.body)
        meeting_title = data.get('meeting_title')
        selected_customers = data.get('selected_customers')  # List of selected customer emails
        sender_id = request.session.get('customer')
        sender = Customer.objects.filter(id=sender_id).first() # Assuming the logged-in user is the sender
        
        if not meeting_title or not selected_customers:
            return JsonResponse({"error": "Meeting title and customers are required."}, status=400)
        
        # Generate unique link and meeting code
        meeting_code = get_random_string(8).upper()
        meeting_link = f"http://127.0.0.1:8000/lobby?channel={meeting_title}"  # Update with your domain

        # Check connections and send emails
        valid_customers = []
        for email in selected_customers:
            # if email == sender.email:
            #     continue  # Skip sender's own email
            
            try:
                receiver = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                continue  # Skip if customer does not exist
            
            # Check if the sender and receiver are connected
            connection = ConnectionRequest.objects.filter(
                sender=sender, receiver=receiver, status="accepted"
            ).exists() or ConnectionRequest.objects.filter(
                sender=receiver, receiver=sender, status="accepted"
            ).exists()

            if connection:
                valid_customers.append(receiver)
        
        if not valid_customers:
            return JsonResponse({"error": "No valid connected customers found."}, status=400)

         # Save meeting details in the Meeting object
        meeting = Meeting.objects.create(
            title=meeting_title,
            scheduled_by=sender,
            meeting_link=meeting_link,
            meeting_code=meeting_code,
            participant_emails=[customer.email for customer in valid_customers],
        )
        meeting.participants.set(valid_customers)
        
        # Send email invitations
        for customer in valid_customers:
            send_mail(
                subject=f"You are invited to a meeting: {meeting_title}",
                message=(
                    f"{sender.first_name} {sender.last_name} has invited you to join a meeting.\n\n"
                    f"Meeting Title: {meeting_title}\n"
                    f"Meeting Link: {meeting_link}\n"
                    f"Meeting Code: {meeting_code}\n\n"
                    f"Please join the meeting using the link and meeting code provided."
                ),
                from_email="devangp539@gmail.com",  # Update with your email
                recipient_list=[customer.email],
            )
        
        return JsonResponse({
            "message": f"Meeting scheduled successfully. Invitation sent to {len(valid_customers)} connections.",
            "meeting_link": meeting_link,
            "meeting_code": meeting_code,
        })

    return JsonResponse({"error": "Invalid request method."}, status=405)
