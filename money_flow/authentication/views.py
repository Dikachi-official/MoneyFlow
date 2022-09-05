from genericpath import exists
from django.shortcuts import render
from django.views import View
import json 
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username must be alphanumeric '}, status=400)
        return JsonResponse({'username_valid': True})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username already exist'}, status=400)
        return JsonResponse({'username_valid': True})

class SigninView(View):
    def get(self, request):
        return render(request, 'authentication/sign-in.html')


class SignupView(View):
    def get(self, request):
        return render(request, 'authentication/sign-up.html')