from django.urls import path
from . views import SigninView, SignupView, UsernameValidationView, EmailValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = {
    path('sign-in/', SigninView.as_view(), name="sign-in"),
    path('sign-up/', SignupView.as_view(), name="sign-up"),
    path('validate-username/', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email/', csrf_exempt(EmailValidationView.as_view()), name="validate-email"),
}