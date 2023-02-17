from django.contrib import admin
from .models import Category, Course
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)


class Meta:
    model = Course
    fields = '__all__'


class CouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'category']
    search_fields = ['subject']
    list_filter = ['category']
    form = CourseForm


# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CouseAdmin)
