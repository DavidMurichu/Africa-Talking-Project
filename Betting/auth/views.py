from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import africastalking
from .serializers import USSDCallbackSerializer
from env import config

username = config.USERNAME    # use 'sandbox' for development in the test environment
api_key = config.API_key      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)
class USSDCallbackView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = USSDCallbackSerializer(data=request.data)
        if serializer.is_valid():
            session_id = serializer.validated_data.get('sessionId', None)
            service_code = serializer.validated_data.get('serviceCode', None)
            phone_number = serializer.validated_data.get('phoneNumber', None)
            text = serializer.validated_data.get('text', None)

            # response='END Error'

            # if text == None:
            #     # Initial request
            #     response = "CON Welcome! Please choose an option:\n"
            #     response += "1. Login\n"
            #     response += "2. Register\n"
            # elif text == '1':
            #     # Login option
            #     response = "CON Please enter your phone number:\n"
            # elif text == '1*' + phone_number:
            #     # Handle login
            #     response = "CON Enter your password:\n"
            # elif text.startswith('1*' + phone_number + '*'):
            #     # Handle login password
            #     password = text.split('*')[-1]
            #     # Add login logic here (e.g., authenticate user)
            #     response = "END Login successful!"
            # elif text == '2':
            #     # Register option
            #     response = "CON Please enter your phone number to register:\n"
            # elif text.startswith('2*'):
            #     # Handle registration phone number
            #     phone_number = text.split('*')[-1]
            #     response = "CON Enter your password:\n"
            # elif text.startswith('2*' + phone_number + '*'):
            #     # Handle registration password
            #     password = text.split('*')[-1]
            #     # Add registration logic here (e.g., create user)
            #     response = "END Registration successful!"
            # else:
            #     response = "END Invalid input. Please try again."

            return HttpResponse('End Hey', content_type='text/plain')
        else:
            return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)