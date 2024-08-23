from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Employer
from job_seeker.models import JobSeeker

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'employer':
            Employer.objects.create(owner=instance)
            instance.is_staff = True
            instance.save()
        elif instance.role == 'jobseeker':
            JobSeeker.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'employer':
        instance.employer.save()
    elif instance.role == 'jobseeker':
        instance.jobseeker.save()