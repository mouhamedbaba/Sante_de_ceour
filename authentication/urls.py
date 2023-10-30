
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_admin, name = 'login'),
    path('logout/', logout_admin, name = 'logout')
]

