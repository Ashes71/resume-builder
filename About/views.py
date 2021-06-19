from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request,"About.html")
def Contact_Us(request):
    return render(request,"Contact_us.html")
