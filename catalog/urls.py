from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
]
