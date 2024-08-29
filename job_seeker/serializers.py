from rest_framework import serializers
from employer.models import User
from .models import JobSeeker,JobApplication

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username', 'email','first_name','last_name','role']


class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model =JobSeeker
        fields = ['id','resume']
        read_only_fields = ['id']


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'job_seeker']