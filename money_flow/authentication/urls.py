from django.urls import path
from . views import SigninView, SignupView

urlpatterns = {
    path('sign-in/', SigninView.as_view(), name="sign-in"),
    path('sign-up/', SignupView.as_view(), name="sign-up"),
}