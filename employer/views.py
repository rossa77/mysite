from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.request import Request
from .models import JobPosting
from rest_framework.decorators import api_view
from .serializers import  JobPostingSerializer
from rest_framework import generics

class JobPostingView(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
