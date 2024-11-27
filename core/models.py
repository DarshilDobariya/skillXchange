from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=150)
    # experience_level = models.IntegerField(default=0)  # Define experience level, e.g., in years or 0–10 scale

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/users/images/', blank=True, null=True)
    position = models.CharField(max_length=100,default="N/A")
    address = models.TextField(default="N/A")
    experience_years = models.IntegerField(default=0)
    
    # Social links, default to "N/A" if not provided
    linkedin = models.URLField(blank=True, default="N/A")
    twitter = models.URLField(blank=True, default="N/A")
    instagram = models.URLField(blank=True, default="N/A")
    facebook = models.URLField(blank=True, default="N/A")

    # Many-to-many relationship with Skill
    skills = models.ManyToManyField(Skill, blank=True)

    # Save method
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()
