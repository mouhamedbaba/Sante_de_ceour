from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('newsletter', newsletter, name = 'add_newsletter'),
    path('message', message, name = 'add_message'),
    path('volunteer', volunteer, name = 'add_volunteer'),
    
    # path('blog/', blog, name='blog')
]
