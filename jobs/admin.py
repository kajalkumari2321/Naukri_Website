from django.contrib import admin
from .models import Job, UserProfile, JobApplication, Review

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'salary', 'posted_date', 'employer']
    search_fields = ['title', 'company', 'location']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'phone', 'company_name']
    list_filter = ['role']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job', 'applied_date', 'status']
    list_filter = ['status']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'rating', 'approved', 'created_at']
    list_filter = ['approved', 'rating']
    actions = ['approve_reviews']
    
    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
    approve_reviews.short_description = "Approve selected reviews"
