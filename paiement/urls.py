from django.urls import path
from .views import *

urlpatterns = [
    path('redirect/', paiement_view, name="redir"),
    path('success/', sucess, name = 'sucess'),
    path('cancel/', cancel, name = 'cancel'),
    path('ipn/', ipn, name = 'ipn'),
]
