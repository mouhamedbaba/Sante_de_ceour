from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name ='home'),
    path('admins', admins, name = 'admins'),
    path('collection/', collections, name='collects'),
    
    
    #  functions
    path('actions/<int:admin_pk>/<str:action>', admins_actions, name='actions'),
    path('adduser/', addUser, name='adduser'),
    path('collect/<int:collect_pk>/<str:action>', action_collects, name = 'collect_action'),
    path('addcollect', addCollect, name = 'addcollect')
]
