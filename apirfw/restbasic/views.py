from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from restbasic.models import Register
from .serializers import UserSerializer
from datetime import datetime
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserView(APIView):
	def post(self,request):
		try:
			first_name = request.data.get('first_name')
			last_name = request.data.get('last_name')
			email = request.data.get('email')
			mobile_number = request.data.get('mobile_number')
			password = request.POST["password"]
			date_of_birth = request.POST.get("dateofbirth")
			received_datetime = datetime.strptime(date_of_birth, '%d/%m/%Y')
			profile_pic = request.FILES.get("Profilepic")
			user = User(first_name=first_name,last_name=last_name,email=email,username=email)
			user.set_password(password)
			user.save()
			custom_user = Register(user=user,mobile_name=mobile_number,profile_pic=profile_pic,date_of_birth=received_datetime)
			custom_user.save()
			payload = jwt_payload_handler(user)
			token = jwt_encode_handler(payload)
			content = {
				'message': 'Registration is successfully done',
				'token': token
			}
			return JsonResponse(content,safe=False)
		except Exception as e:
			print(e)


class LoginView(APIView):
	def post(self,request):
		try:
			username = request.data.get('username')
			password = request.data.get('password')
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				content = {
					'message': 'login successfully'
				}
				return JsonResponse(content,safe=False) 
			else:
				content = {
					'message': 'login failed'
				}
				return JsonResponse(content,safe=False)
		except Exception as e:
			print(e)


class AllProfileView(APIView):
	def get(self,request,*args, **kwargs):
		try:
			profile =  Register.objects.all()
			print(profile)
			serializer = UserSerializer(profile)
			print(serializer.data)
			return Response(serializer)
		except Exception as e:
			print(e)

"""class ProfileUpdateView(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)
	serializer_class = UserSerializer
	def get_object(self):
		return AllProfile.objects.get(user=self.request.user)"""


class LogoutView(APIView):
	def post(self, request):
		return self.logout(request)
	def logout(self, request):
		try:
			request.user.auth_token.delete()
		except (AttributeError, ObjectDoesNotExist):
			pass
		logout(request)
		return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)