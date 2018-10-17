from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    pass
    # id = models.AutoField(primary_key=True)
    # company_name = models.CharField(max_length=100)
    # offer = models.FloatField()
    # contact = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=25)
    # phone_number = models.CharField(max_length=15)
    # user_id = models.ForeignKey(User, related_name="user_companies", on_delete=models.CASCADE, default=1)
    #
    # def __str__(self):
    #     return self.company_name


class Application(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    APP_STATUS = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=8, choices=APP_STATUS)
    app_date = models.DateField()
    interview_date = models.DateTimeField()
    site_applied_from = models.CharField(max_length=50, default='')
    company_name = models.CharField(max_length=100)
    company_offer = models.FloatField()
    company_contact = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_city = models.CharField(max_length=50)
    company_state = models.CharField(max_length=25)
    company_phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name


class Interview(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    application_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    questions_asked = models.TextField()

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    application_id = models.ForeignKey(Application, related_name="application_notes", on_delete=models.CASCADE, default=1)
    note = models.TextField()

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name="user_todos", on_delete=models.CASCADE, default=1)
    task = models.TextField()
