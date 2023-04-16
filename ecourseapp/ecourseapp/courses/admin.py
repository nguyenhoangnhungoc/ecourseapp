from django.contrib import admin
from .models import Category, Course, Lesson, Tag, User
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


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class LessonTagInlineAdmin(admin.StackedInline):  # nhúng zô để sửa (kiểu như chọn nhiều tag khác nhao á)
    model = Lesson.tags.through  # phải lấy model trung gian ga#


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date']
    search_fields = ['subject', 'tags']
    list_filter = ['tags', 'course']
    form = LessonForm
    inlines = [LessonTagInlineAdmin]


# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CouseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
admin.site.register(User)
