from django.shortcuts import render, redirect, HttpResponseRedirect
from skillXchange.models.product import Products
from skillXchange.models.category import Category
from django.views import View
from django.http import JsonResponse
from skillXchange.models.customer import Customer, Skill  # Import your Customer and Skill models
import json

class Profile1(View):
    def get(self, request):
        customer_id = request.session.get('customer')  # Get the customer ID from session
        customer = Customer.objects.filter(id=customer_id).first()
        skills = list(customer.skills.values_list('name', flat=True)) if customer else []

        if customer:
            # Prepare customer data
            data = {
                'customer': customer,
                'skills': skills,
            }
        else:
            data = {}

        return render(request, 'profile.html', data)

    def post(self, request):
        try:
            data = json.loads(request.body)
            new_skills = data.get('skills', [])
            customer_id = request.session.get('customer')
            customer = Customer.objects.filter(id=customer_id).first()

            if customer:
                # Get a set of current skill names for the customer
                current_skill_names = set(customer.skills.values_list('name', flat=True))

                # Iterate through the new skills list, add only if not already present
                for skill_name in new_skills:
                    if skill_name not in current_skill_names:
                        skill, created = Skill.objects.get_or_create(name=skill_name)
                        customer.skills.add(skill)  # Add the new skill

                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Customer not found'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    def delete_skill(self, request, skill_id):
        if request.method == 'POST':
            customer_id = request.session.get('customer')
            customer = Customer.objects.filter(id=customer_id).first()

            if customer:
                try:
                    skill = Skill.objects.get(id=skill_id)
                    customer.skills.remove(skill)
                    return JsonResponse({'status': 'success', 'message': 'Skill deleted successfully.'})
                except Skill.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'Skill not found.'})

        return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
