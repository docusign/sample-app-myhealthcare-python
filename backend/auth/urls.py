from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check),
    path('get_status', views.get_status),
    path('logout', views.logout),
    path('code_grant_auth', views.code_grant_auth, name='code_grant_auth'),
    path('jwt_auth', views.jwt_auth, name='jwt_auth'),
    path('callback', views.callback),
]
