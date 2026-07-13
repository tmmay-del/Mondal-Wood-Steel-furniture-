from django.shortcuts import render
from .models import*
def furniture(request):
    stocks=Stock.objects.all()
    return render(request,'f_index.html',{'products':stocks})

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # This triggers your custom PhoneAuthBackend!
        user = authenticate(request, username=phone, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home') # Redirect to your home page after success
        else:
            messages.error(request, 'Invalid phone number or password.')
            
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
# views.py (Add these imports at the top if you don't have them)
from django.contrib.auth.models import User
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password') # The user number
        address = request.POST.get('address')
        
        # 1. Check if the phone number is already registered
        if UserProfile.objects.filter(ph_no=phone).exists():
            messages.error(request, 'An account with this phone number already exists.')
            return redirect('furniture_page')
            
        try:
            # 2. Create the standard Django User
            # We use the phone number as the hidden 'username' behind the scenes
            user = User.objects.create_user(username=phone, password=password)
            
            # 3. Create the linked UserProfile with the extra data
            UserProfile.objects.create(
                user=user,
                ph_no=phone,
                user_no=password,
                address=address
            )
            
            # 4. Automatically log the user in after they sign up!
            # We have to specify the backend since we have a custom one
            login(request, user, backend='furniture.backends.PhoneAuthBackend')
            
            return redirect('furniture_page') # Send them to the home page
            
        except Exception as e:
            messages.error(request, f'Error creating account. Please try again.')
            return redirect('signup')

    return render(request, 'signup.html')