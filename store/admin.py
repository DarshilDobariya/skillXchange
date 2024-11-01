from django.contrib import admin

from .models.customer import Customer



admin.site.site_header = "SkillXchange"
admin.site.site_title = "SkillXchange"
admin.site.index_title = "Welcome to the Admin Panel"
# Register your models here.
admin.site.register(Customer)


