from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'admn/admin_login.html')

def home(request):
    return render(request,'admn/home.html')
