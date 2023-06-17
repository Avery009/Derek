from . import views
from django.urls import path, include

urlpatterns = [
	path('', views.home, name = 'Home'),
	path('contact/', views.contact, name = 'Contact'),
	path('about/', views.about, name = 'About'),
]
