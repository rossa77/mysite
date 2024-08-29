from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from .serializers import UserSerializer,JobSeekerSerializer,JobApplicationSerializer
from .models import JobPosting,JobSeeker
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import os


@api_view(['POST'])
def UserCreateView(request:Request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class JobSeekerUpdateView(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer
    parser_classes = (MultiPartParser, FormParser)
    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(JobSeeker, user__username=username)

    def perform_update(self, serializer):
        username = self.kwargs['username']
        job_seeker = get_object_or_404(JobSeeker, user__username=username)
        if job_seeker.resume and os.path.isfile(job_seeker.resume.path):
            os.remove(job_seeker.resume.path)
        serializer.save()
    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return Response(self.get_serializer(self.get_object()).data, status=status.HTTP_200_OK)

class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = JobApplicationSerializer

    #زمانی که از pk استفاده نمیکنیم
    # def post(self, request, *args, **kwargs):
    #     try:
    #         job_posting_title = self.kwargs['job_posting_title']
    #         job_seeker_username = self.kwargs['job_seeker_username']
    #         job_posting = get_object_or_404(JobPosting, title=job_posting_title)
    #         job_seeker = get_object_or_404(JobSeeker, user__username=job_seeker_username)
    #         data = request.data.copy()
    #         data['job_posting'] = job_posting
    #         data['job_seeker'] =   job_seeker
    #         serializer = self.get_serializer(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #
    #     except Exception as e:
    #         print(f"Error occurred: {e}")
    #         raise