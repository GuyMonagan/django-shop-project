from django.urls import path
from .views import RegisterView
from .views import profile_edit
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', profile_edit, name='profile_edit'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
