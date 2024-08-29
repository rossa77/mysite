from django.urls import path
from .views import JobPostingView

urlpatterns = [
    path('', JobPostingView.as_view()),
]