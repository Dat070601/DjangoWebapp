import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, permissions
from .serializer import *

from myapp.models import Course
# cach su dung viewSet 1 cach co ban
class CourseViewSet(viewsets.ModelViewSet): #ModelViewSet ke thua APIView va APIView ke thua view chuan cua django
    queryset = Course.objects.filter(active = True)
    serializer_class = CourseSerializer
    #khi gan permissions nhu vay thi tat ca cac cau truy van phai duoc dang nhap
    # permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if(self.action == 'list'):
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    # Voi khai bao nhu tren thi se tao duoc 5 API
    # list (GET)-> xem danh sach khoa hoc
    # (POST) -> Them khoa hoc
    # detail -> xem chi tiet khoa hoc
    # (PUT) -> cap nhat
    # (DELETE) -> Xoa khoa hoc

# Create your views here.
def index(request):
    return render(request, 'index.html', context={'name':'Dat'})
def welcome(request,year):
    return HttpResponse("HELLO "+str(year))
def welcome2(request,year):
    return HttpResponse("HELLO "+str(year))

class TestView(View):
    def get(self,request):
        return HttpResponse("WELCOME TEST")
    def post(self,request):
        pass
