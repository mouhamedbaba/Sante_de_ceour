from django.urls import path
from .views import *

urlpatterns = [
    # pages
    path('', home, name ='home'),
    path('admins', admins, name = 'admins'),
    path('collects/', collects, name='collects'),
    path('collect/<int:collect_pk>', details_collect, name='details_collect'),
    
    #  functions
    path('admin/<int:admin_pk>/<str:action>', admins_actions, name='actions'),
    path('adduser/', addUser, name='adduser'),
    path('collect/<int:collect_pk>/<str:action>', action_collects, name = 'collect_action'),
    path('addcollect', addCollect, name = 'addcollect'),
    path('add_don', donCollect, name = 'add_don')
]
