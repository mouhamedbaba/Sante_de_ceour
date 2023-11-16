"""
URL configuration for sante_coeur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django import urls
from sante_coeur import settings
from task.views import forbiden

urlpatterns = [
    path('forbiden', forbiden , name="forbiden"),
    path('django/', admin.site.urls, name='admin'),
    path('auth/', include('authentication.urls')),
    path('', include('landing.urls')),
    path('sante/', include('administration.urls')),
    path('paiement/', include('paiement.urls')),
    path('task/', include('task.urls')),
    
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)