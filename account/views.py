from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def hotel_owner(request):
    return render(request,"hotel_pages/hotel_homepage.html")


def captain(request):
    return render(request,"hotel_pages/hotel_captain.html")

def chef(request):
    return render(request,"hotel_pages/hotel_chef.html")

def receptionist(request):
    return render(request,"hotel_pages/hotel_reception.html")


def delivery_partner(request):
    return render(request,"delivery_pages/delivery_partner.html")


def supplier(request):
    return render(request,"supplier_pages/supplier.html")






def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'hotel_owner':
                return redirect('hotel_owner')
            elif user.role == 'delivery_partner':
                return redirect('delivery_partner')
            elif user.role == 'supplier':
                return redirect('supplier')
            elif user.role == 'captain':
                return redirect('captain')
            elif user.role == 'chef':
                return redirect('chef')
            elif user.role == 'receptionist':
                return redirect('receptionist')
        else:
            # Invalid credentials
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')


