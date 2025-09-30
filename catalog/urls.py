from django.urls import path
from catalog import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("contacts/", views.contacts_view, name="contacts"),
]
