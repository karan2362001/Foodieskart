from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def landing(request):
    
    return render(request,"landing.html")

def pricing(request):
    
    return render(request,"pricing.html")
    
    