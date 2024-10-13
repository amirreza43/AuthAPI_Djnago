from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

class CustomRegisterSerializer(RegisterSerializer):
    username = None  # Remove username field

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name']  # Add or remove fields as necessary

class CustomLoginSerializer(LoginSerializer):
    username = None  # Remove username field

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']  # Only use email and password
