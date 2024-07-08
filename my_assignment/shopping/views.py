from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'about.html')
def Services(request):
    return render(request,'Services.html')
def Contactus(request):
    return render(request, 'Contactus.html')
