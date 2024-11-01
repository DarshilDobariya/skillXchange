from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.http import JsonResponse
from store.models.customer import Customer, Skill  # Import your Customer and Skill models
import json
# Create your views here.
class Index(View):

    


    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    # cart = request.session.get('cart')
    # if not cart:
    #     request.session['cart'] = {}
    # products = None
    # categories = Category.get_all_categories()
    # categoryID = request.GET.get('category')
    # if categoryID:
    #     products = Products.get_all_products_by_categoryid(categoryID)
    # else:
    #     products = Products.get_all_products()

    # data = {}
    # data['products'] = products
    # data['categories'] = categories

    # print('you are : ', request.session.get('email'))
    # return render(request, 'index.html', data)
    customer_id = request.session.get('customer')  # Get the customer ID from session
    customer = Customer.objects.filter(id=customer_id).first()
    skills = list(customer.skills.values_list('name', flat=True)) if customer else []
    if customer:
        # first_name = customer.first_name()  # Get all skills for this customer
        skills = customer.skills.all()
        data = {
            'customer': customer,
            'skills': skills,
        }
    else:
        data = {}

    return render(request, 'index.html', data)


