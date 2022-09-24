from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
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