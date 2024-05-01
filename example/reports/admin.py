from django.contrib import admin
from .models import Report

admin.site.register(Report)

class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    actions = ['approve_reports', 'reject_reports']

    def approve_reports(self, request, queryset):
        queryset.update(status='approved')

    def reject_reports(self, request, queryset):
        queryset.update(status='rejected')

    approve_reports.short_description = 'Approve selected reports'
    reject_reports.short_description = 'Reject selected reports'