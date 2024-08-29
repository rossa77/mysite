from django.urls import path
from .views import UserCreateView,JobSeekerUpdateView,JobApplicationCreateView

urlpatterns = [
    path('', UserCreateView),
    path('resume/<str:username>/', JobSeekerUpdateView.as_view()),
    path('aply/', JobApplicationCreateView.as_view()),
]