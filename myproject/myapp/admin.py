import imp
from operator import imod
import re
from unicodedata import category
from attr import field
from django.contrib import admin
from django.contrib.auth.models import Permission 
from django import forms
from .models import Category, Course, Lesson, HashTag, User
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count

class LessonForm(forms.ModelForm): # Tao bo cong cu soan thao van ban, xuat ra file html
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = "__all__"
class LessonAdmin(admin.ModelAdmin): #Custom cho trang admin
    list_display = ["id","subject","create_date","active","course"] #Chi hien thi cac thong tin co trong list
    search_fields = ["subject","create_date","course__subject"] #Tao ra o tim kiem va chi dinh  truong muon tim kiem trong list
    list_filter = ["subject","course__subject"] #Tim kiem theo bo chu de
    readonly_fields = ["avatar"]
    def avatar(self,lesson): #Hien thi anh trong trang admon
        return mark_safe("<img src='/static/{img_url}'alt = {alt}'>".format(img_url=lesson.image.name, alt = lesson.subject))
    class Media:
        css ={
            'all': ('/static/css/test.css',)
        }
    form = LessonForm
class CourseAppAdminSite(admin.AdminSite):
    site_header = "HE THONG QUAN LY KHOA HOC"
    def course_stats(self,request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count = Count("Lesson")).values("id","subject","lesson_count") #Cau lenh quenry dem so luong
        return TemplateResponse(request, 'admin/course-stats.html',{
            'course_count': course_count,
            'stats' : stats
        })
    def get_urls(self): 
        return[
            path("course-stats/",self.course_stats)
        ]+super().get_urls()
# admin_site = CourseAppAdminSite("mycourse") # "mycourse" la Ten cua doi tuong admin_site
# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(User)
admin.site.register(Permission)
# Register your models here.
# admin_site.register(Category)
# admin_site.register(Course)
# admin_site.register(Lesson,LessonAdmin)