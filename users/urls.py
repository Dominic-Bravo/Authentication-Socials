from django.urls import path, include
from .views import GoogleLogin

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # Social Login Endpoint
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
]