from django.urls import path
from .views import RegisterView

urlpatterns = [
    # Register endpoint
    path('register/', RegisterView.as_view()),
]