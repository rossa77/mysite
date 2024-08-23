from django.db import models
from employer.models import User
from employer.models import JobPosting


STATUS_CHOICES = [
        ('rejected', 'REJECTED'),
        ('accepted', 'ACCEPTED'),
        ('under_review', 'UNDER REVIEW'),
]


class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class JobApplication(models.Model):
    job_seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='under_review')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_seeker.user.username} - {self.job_posting.title} : {self.status}"



