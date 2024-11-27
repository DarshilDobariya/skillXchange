<<<<<<< Updated upstream
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
=======
# from django.shortcuts import render , redirect , HttpResponseRedirect

# from django.views import View

# from django.shortcuts import render, redirect, HttpResponseRedirect

# from django.views import View
# from django.http import JsonResponse
# from store.models.customer import Customer, Skill  # Import your Customer and Skill models
# import json
# from datetime import datetime
# # Create your views here.
# class Index(View):

#     def get(self,request):
#         # cart = request.session.get('cart')
#         # if not cart:
#         #     request.session['cart'] = {}
#         # products = None
#         # categories = Category.get_all_categories()
#         # categoryID = request.GET.get('category')
#         # if categoryID:
#         #     products = Products.get_all_products_by_categoryid(categoryID)
#         # else:
#         #     products = Products.get_all_products()

#         # data = {}
#         # data['products'] = products
#         # data['categories'] = categories

#         # print('you are : ', request.session.get('email'))
#         # return render(request, 'index.html', data)
#         if request.session.get('customer'):

#             customer_id = request.session.get('customer')  # Get the customer ID from session
#             customer = Customer.objects.filter(id=customer_id).first()

#             # Retrieve the visit history cookie (default to an empty JSON if not present)
#             visit_history = request.COOKIES.get('visit_history', '{}')
            
#             # Parse the JSON string into a Python dictionary
#             visit_history = json.loads(visit_history)
            
#             # Get today's date in YYYY-MM-DD format
#             today = datetime.now().strftime('%Y-%m-%d')
#             name = customer.first_name + " "+ customer.last_name
#             # Increment the visit count for today
#             visit_count_today = visit_history.get(today, 0) + 1
#             visit_history[today] = visit_count_today
            
#             # # Create a response object
#             # response = render(request, 'index.html', {
#             #     'name': name,
#             #     'visit_history': visit_history,
#             #     'visit_count_today': visit_count_today,
#             # })
            
#             # # Update the visit history cookie (store it as a JSON string)
#             # response.set_cookie('visit_history', json.dumps(visit_history), max_age=30*24*60*60)  # 30 days
            
#             skills = list(customer.skills.values_list('name', flat=True)) if customer else []
#             if customer:
#                 # first_name = customer.first_name()  # Get all skills for this customer
#                 skills = customer.skills.all()
#                 response = render(request, 'index.html', {
#                     'customer': customer,
#                     'skills': skills,
#                     'name': name,
#                     'visit_history': visit_history,
#                     'visit_count_today': visit_count_today,
#                 })
#                 # response = {
#                 #     'customer': customer,
#                 #     'skills': skills,
#                 #     'name': name,
#                 #     'visit_history': visit_history,
#                 #     'visit_count_today': visit_count_today,
#                 # }
#                 # Update the visit history cookie (store it as a JSON string)
#                 response.set_cookie('visit_history', json.dumps(visit_history), max_age=30*24*60*60)  # 30 days
#                 return response
#             else:
#                 response = {}

#         if response:
#             return render(request, 'index.html',response)
#         else:
#             return render(request, 'index.html')

            


from django.shortcuts import render
>>>>>>> Stashed changes
from django.views import View
from store.models.customer import Customer
import json
<<<<<<< Updated upstream
# Create your views here.
=======
from datetime import datetime

>>>>>>> Stashed changes
class Index(View):
    def get(self, request):
        # Initialize the response variable to avoid UnboundLocalError
        response = None

<<<<<<< Updated upstream
    


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

=======
        # Check for logged-in customer
        customer_id = request.session.get('customer')
        customer = Customer.objects.filter(id=customer_id).first() if customer_id else None

        # Handle visit history
        visit_history = json.loads(request.COOKIES.get('visit_history', '{}'))
        today = datetime.now().strftime('%Y-%m-%d')
        visit_history[today] = visit_history.get(today, 0) + 1

        if customer:
            # Prepare context if customer exists
            context = {
                'customer': customer,
                'name': f"{customer.first_name} {customer.last_name}",
                'skills': customer.skills.all(),
                'visit_history': visit_history,
                'visit_count_today': visit_history[today],
            }

            # Render response and set cookie
            response = render(request, 'index.html', context)
            response.set_cookie('visit_history', json.dumps(visit_history), max_age=30 * 24 * 60 * 60)  # 30 days
        else:
            # Render a default response for anonymous users
            response = render(request, 'index.html')
>>>>>>> Stashed changes

        return response
