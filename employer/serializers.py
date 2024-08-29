from rest_framework import serializers
from .models import JobPosting


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['id','title', 'description', 'company', 'category','salary','working_hours','posting_date','expiry_date','image']
        read_only_fields = ['posting_date','id']