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

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj:
            return obj.owner == request.user
        return super().has_change_permission(request, obj)

admin.site.register(Employer,EmployerAdmin)



