from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    offer = models.FloatField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    APP_STATUS = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=8, choices=APP_STATUS)
    app_date = models.DateField()
    interview_date = models.DateTimeField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    site_applied_from = models.CharField(max_length=50)


class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    questions_asked = models.TextField()
