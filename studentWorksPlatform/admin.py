from django.contrib import admin
from studentWorksPlatform import models

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'balance', 'university', 'faculty', 'group', 'created_at']
    search_fields = ['username', 'email']
    ordering = ['-created_at']


@admin.register(models.Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'status', 'created_at']
    search_fields = ['title', 'author__username']
    ordering = ['-created_at']


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['buyer',  'work', 'purchase_date']
    search_fields = ['buyer__username', 'work__title', 'work__author__username']
    ordering = ['-purchase_date']


@admin.register(models.FavoriteWork)
class FavoriteWorkAdmin(admin.ModelAdmin):
    list_display = ['user', 'work', 'created_at']
    search_fields = ['user__username', 'work__title']
    ordering = ['-created_at']


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message', 'created_at', 'is_read']
    search_fields = ['sender__username', 'receiver__username']
    ordering = ['-created_at']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer', 'user', 'rating', 'created_at', 'is_read']
    search_fields = ['reviewer__username', 'user__username']
    ordering = ['-created_at']


@admin.register(models.Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance_addition', 'created_at']
    search_fields = ['user__username']
    ordering = ['-created_at']


@admin.register(models.WorkReport)
class WorkReportAdmin(admin.ModelAdmin):
    list_display = ['sender', 'work', 'reason', 'status', 'created_at']
    search_fields = ['sender__username', 'work__title']
    ordering = ['-created_at']


@admin.register(models.UserReport)
class UserReportAdmin(admin.ModelAdmin):
    list_display = ['sender', 'user', 'reason', 'status', 'created_at']
    search_fields = ['sender__username', 'user__username']
    ordering = ['-created_at']


@admin.register(models.ReviewReports)
class ReviewReportsAdmin(admin.ModelAdmin):
    list_display = ['sender', 'review', 'reason', 'status', 'created_at']
    ordering = ['-created_at']

