# views/search.py

from django.shortcuts import render
from django.db.models import Q  # Import Q for complex queries
from store.models.customer import Customer
 # Assuming Skill is in the same module

def search_customers(request):
    query = request.GET.get('query', '')
    customers = []
    
    if query:
        # Fetch customers by first_name or last_name or skills
        customers = Customer.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(skills__name__icontains=query)
        ).distinct()  # distinct to avoid duplicates

    return render(request, 'result.html', {'customers': customers, 'query': query})
