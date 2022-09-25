from django.urls import path

from . import views


urlpatterns = [
	path('', views.main),
	path('login/', views.login),
	path('register/', views.register),
	path('history/', views.history),
	path('payment/', views.payment)
]