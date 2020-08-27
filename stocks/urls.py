from django.urls import path
from . import views

urlpatterns = [
	path('',views.stock, name='stock'),
	path('api',views.api, name='api'),
]
