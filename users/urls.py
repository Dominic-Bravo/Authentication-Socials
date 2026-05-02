from django import views
from django.urls import path, include

from users import consumers
from .views import FacebookLogin, GoogleLogin, NewsViewSet, ProfileViewSet

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # Social Login Endpoint
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    
    path('api/public/', NewsViewSet.as_view({'get': 'list'}), name='public-news'),
    path('api/private/', ProfileViewSet.as_view({'get': 'list'}), name='private-profile'),
    
]