from django.shortcuts import render

# Create your views here.
def common_home(request):
    return render(request,'common_app/common_home.html')

def parent_login(request):
    return render(request,'common_app/parent_login.html')

def teachers_login(request):
    return render(request,'common_app/teachers_login.html')