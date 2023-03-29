from django.shortcuts import render
from auth import forms
# Create your views here.
def login(request):
    loginForm = forms.LoginForm()
    context = {
        'form': loginForm,
    }
    return render(request, 'auth/login.html', context)