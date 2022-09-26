from distutils.command.upload import upload
from email.policy import default
from re import S
from unicodedata import category
import django
from ckeditor.fields import RichTextField


from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser): #Ke thua bang user cua chinh no 
    avatar = models.ImageField(upload_to= "upload/%Y/%m")
    
class ItemBase(models.Model):
    class Meta: 
        abstract = True #Meta options abstract tao ra model truu tuong
    subject = models.CharField(max_length= 100 ,null=False, unique= True) #Khong de trong va khong trung nhau
    create_date = models.DateTimeField(auto_now_add= True) #Tu dong cap nhat ngay khi Course duoc tao
    update_date = models.DateTimeField(auto_now=True) #Tu dong cap nhat ngay khi Course duoc update
    image = models.ImageField(upload_to= "courses/%Y/%m", default = None)
    active = models.BooleanField(default=True) #Tu dong bat khi them 
    def __str__(self):
        return self.subject

class Category(models.Model): #myapp_Category
    name = models.CharField(max_length= 100 ,null=False, unique= True) #Khong de trong va khong trung nhau
    def __str__(self):
        return self.name

class Course(ItemBase): #myapp_Course #khoa hoc
    class Meta: 
        unique_together = ('subject','category') # trong 1 category khong duoc trung ten subject
        ordering = ["id"]
    description = models.TextField(null = True, blank= True) 
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null= True)# Khoa ngoai tro? toi category, khi xoa catagory thi truong category se thanh null 

class HashTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Lesson(ItemBase): #Bai hoc
    class Meta: 
        unique_together = ('subject','course')
    content = RichTextField()
    course = models.ForeignKey(Course, related_name="Lesson",on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(HashTag, blank= True , null= True)

