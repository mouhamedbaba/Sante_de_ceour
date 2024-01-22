from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index , name="task"),
    path('workspace/<str:user>/<int:pk>', workspace , name="workspace"),
    
    #add 
    path('card/add/', addCard, name="add_card"),
    path('column/add', addColumn, name="add_column"),
    path('update/title/<int:card_pk>', update_card_title, name="update_card_title"),
    path('column/update', update_column, name="update_card_title"),
    # path('edit/<int:pk>', edit_card, name="edit_card"),
]
