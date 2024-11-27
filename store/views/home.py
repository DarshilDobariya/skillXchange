from django.shortcuts import render
from django.views import View
from store.models.customer import Customer
import json
from datetime import datetime

class Index(View):
    def get(self, request):
        # Initialize the response variable to avoid UnboundLocalError
        response = None

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

        return response
