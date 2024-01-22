
from django.urls import path
from .views import login_admin, logout_admin

urlpatterns = [
    path('login/', login_admin, name = 'login'),
    path('logout/', logout_admin, name = 'logout')
]

