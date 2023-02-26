from django.urls import path, include
from .views import login_view, logout_view, registration_view

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', registration_view, name='registration_view'),
]
