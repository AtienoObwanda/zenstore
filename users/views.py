from django.shortcuts import render


def shipping(request):
    return render(request,'shipping.html')

def cart(request):
    return render(request,'cart.html')

def payment(request):
    return render(request,'payment.html')

def profile(request):
    return render(request,'profile.html')

def favorites(request):
    return render(request,'favorites.html')

def edit_profile(request):
    return render(request,'edit_profile.html')