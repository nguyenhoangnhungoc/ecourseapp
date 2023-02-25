from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/static/%Y/%m', null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # nếu có khoá học thì không cho xoá danh mục#

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='courses/static/%Y/%m', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # nếu xoá course thì xoá luôn lesson#
    tags = models.ManyToManyField('Tag',related_name='lessons') #giúng href á#

    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
