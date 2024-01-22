
# from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django import urls
from sante_coeur import settings


urlpatterns = [
    # path('django/', admin.site.urls, name='admin'),
    path('auth/', include('authentication.urls')),
    path('', include('landing.urls')),
    path('sante/', include('administration.urls')),
    path('paiement/', include('paiement.urls')),
    
]

# if settings.DEBUG :
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)