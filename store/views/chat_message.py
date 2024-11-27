from django.shortcuts import render, redirect, get_object_or_404
from store.models.chat import Message
from store.models.customer import Customer
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def customer_list(request):
    customer_id = request.session.get('customer')
    customers = Customer.objects.exclude(id=customer_id)  # Exclude the current customer
    # return render(request, 'customer_list.html', {'customers': customers}) -- old
    return render(request, 'main_chat.html', {'customers': customers})

# @login_required
def chat_window(request, customer_id):
    main_customer_id = request.session.get('customer')
    
    customers = Customer.objects.exclude(id=main_customer_id)  # Exclude the current customer
    # return render(request, 'customer_list.html', {'customers': customers}) -- old
    # return render(request, 'main_chat.html', {'customers': customers})


    current_customer = request.session.get('customer')  # Assuming a OneToOne relationship with the Customer model
    customer = Customer.objects.filter(id=current_customer).first()
    other_customer = get_object_or_404(Customer, id=customer_id)
    
    # Get the message history between the current customer and the other customer
    messages = Message.objects.filter(
        (Q(sender=current_customer) & Q(receiver=other_customer)) |
        (Q(sender=other_customer) & Q(receiver=current_customer))
    ).order_by('timestamp')

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(sender=customer, receiver=other_customer, content=message_content)
            return redirect('chat_window', customer_id=customer_id)
    
    return render(request, 'main_chat.html', {'messages': messages, 'other_customer': other_customer,'current_customer':current_customer,'customers': customers,'main_customer_id':main_customer_id})


def showHtml(request):
    return render(request,'main_chat.html')
