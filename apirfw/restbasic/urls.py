from django.urls import path,include
from restbasic.views import *
from . import views

urlpatterns = [
	path('custom_user',UserView.as_view()),
	path('login',LoginView.as_view()),
	path('Allprofile',AllProfileView.as_view()),
	path('logout',LogoutView.as_view()),
	#path('update',ProfileUpdateView.as_view())
		
]
