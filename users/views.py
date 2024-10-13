from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRegisterView(RegisterView):
    pass  # You can extend this if needed

class CustomLoginView(LoginView):
    pass  # You can extend this if needed

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    
    def get_response(self):
        # Get the default response from the adapter (the authenticated user)
        response = super().get_response()

        # Generate a JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        response.data['access'] = str(refresh.access_token)
        response.data['refresh'] = str(refresh)

        return response