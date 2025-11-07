from django.urls import path
from contacts.views import ContactView
from .views import profile_edit

urlpatterns = [
    path('', ContactView.as_view(), name='contacts'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]