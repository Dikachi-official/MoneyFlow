from django.shortcuts import render
from django.views import View

# Create your views here.

class SigninView(View):
    def get(self, request):
        return render(request, 'authentication/sign-in.html')


class SignupView(View):
    def get(self, request):
        return render(request, 'authentication/sign-up.html')