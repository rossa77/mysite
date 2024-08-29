from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

CATEGORY_CHOICES = [
        ('WEB_DEV', 'Web Development'),
        ('MOBILE_DEV', 'Mobile Development'),
        ('DATA_SCIENCE', 'Data Science'),
        ('GAME_DEV', 'Game Development'),
        ('SYSTEM_ADMIN', 'System Administration'),
        ('DEV_OPS', 'DevOps'),
        ('OTHER', 'Other'),
    ]

ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'JobSeeker'),
    ]


class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employer')
    def __str__(self):
        return self.username


class Employer(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    description = models.TextField()
    def __str__(self):
        return self.company



class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    working_hours = models.CharField(max_length=100)
    posting_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


