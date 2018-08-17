from django.conf.urls import url
from first_app import views

urlpatterns = [
    url('help/', views.help, name="help"),
    url('users/', views.users, name="users"),
]
