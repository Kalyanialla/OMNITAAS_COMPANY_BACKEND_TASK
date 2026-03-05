from django.urls import path
from .views import LoginView, SignupView, WelcomeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('welcome/', WelcomeView, name='welcome'),
]