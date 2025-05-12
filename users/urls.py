from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import UserViewSet, LogoutViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename='')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('login/', views.obtain_auth_token, name='login'),
    path('logout/', LogoutViewSet.as_view(), name='logout'),
    path('', include(router.urls)),
]
