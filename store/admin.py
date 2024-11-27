from django.contrib import admin

from .models.customer import Customer
<<<<<<< Updated upstream
=======
# from .models.orders import Order
from .models.connection import ConnectionRequest
from .models.notifications import Notification
from .models.chat import Message
from .models.meetings import Meeting
from .models.roommembers import RoomMember
from .models.customer_ratings import CustomerRating
>>>>>>> Stashed changes



admin.site.site_header = "SkillXchange"
admin.site.site_title = "SkillXchange"
admin.site.index_title = "Welcome to the Admin Panel"
# Register your models here.
admin.site.register(Customer)


