from django.contrib import admin
from django.urls import path

from django.conf.urls.static import*
from django.conf import settings

from . views import *

admin.site.site_header = "CEFA MB-FC"
admin.site.site_title = "CEFA MB-FC"
admin.site.index_title = "CEFA MB-FC | Centre d'Etucation de Formation et d'Apprentissage - Metiers du batîment, froid et climatisation"

urlpatterns = [
    path('cefa-admin/', admin.site.urls),

    # Les routes côté utilisateur
    path('', accueil_view, name = "accueil_url"),
    path('actualites/', actualites_view, name = "actualites_url"),
    path('actualite-detail/<int:id>/', actualite_detail_view, name = "actualite_detail_url"),
    path('inscription/', inscription_view, name = "inscription_url"),
    path('contacts/', contact_view, name = "contact_url"),
    path('a-propos/', about_view, name = "about_url"),
    path('add-newsletter/', addNewsLetter, name = "addNewsLetter"),
    path('message-dg/<int:id>', detail_message_view, name = "detail-message"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)