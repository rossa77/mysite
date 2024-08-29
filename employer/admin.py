from django.contrib import admin
from django.http import HttpResponseForbidden
from .models import User, Employer, JobPosting
from job_seeker.models import JobSeeker

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('owner','company', 'company_logo', 'description')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj:
            return obj.owner == request.user
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request, obj=None):
        return True
    def has_module_permission(self, request, obj=None):
        return True
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'category', 'salary', 'posting_date', 'expiry_date')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company__owner=request.user)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.company = Employer.objects.get(owner=request.user)
        obj.save()
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        try:
            if request.user.is_authenticated:
               Employer.objects.get(owner=request.user)
               return True
        except Employer.DoesNotExist:
            return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj:
            return obj.company.owner == request.user
        return super().has_change_permission(request, obj)
    def has_view_permission(self, request, obj=None):
        return True
    def has_module_permission(self, request, obj=None):
        return True
admin.site.register(JobPosting, JobPostingAdmin)
admin.site.register(Employer,EmployerAdmin)
admin.site.register(User)