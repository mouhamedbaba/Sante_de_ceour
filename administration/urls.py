from django.urls import path
from .views import *
urlpatterns = [
    # pages
    path('', home, name ='home'),
    path('admins', admins, name='admins'),
    path('profile', profile, name='profile'),
    path('collects/', collects, name='collects'),
    path('collect/<int:collect_pk>', details_collect, name='details_collect'),
    path('events/', events, name='events'),
    path('event/<int:event_pk>', event_details, name='event_details'),
    path('contacts/', list_contacts, name='contacts'),
    path('messages/<str:message_pk>', list_messages, name='messages_url'),
    path('newsletters/', list_newsletters, name='newsletters'),
    
    #  functions
    path('admin/<int:admin_pk>/<str:action>', admins_actions, name='actions'),
    path('adduser/', addUser, name='adduser'),
    path('edit/<int:pk>', editUser, name='edituser'),
    path('collect/<int:collect_pk>/<str:action>', action_collects, name = 'collect_action'),
    path('addcollect', addCollect, name = 'addcollect'),
    path('add_don', donCollect, name = 'add_don'),
    path('event/create', create_event, name = "create_event"),
    path('newsletters/delete/<int:pk>', delete_newsletters, name = "delete_newsletters"),
    path('avatar/<int:pk>/delete', delete_avatar, name ="delete_avatar"),
    path('password/change', change_password, name="change_pwd"),
    
    # export 
    path('newsletters/export/<str:type>', exportEmails, name = "export_emails"),
    
]
