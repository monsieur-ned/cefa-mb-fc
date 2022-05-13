from django.contrib import admin
from django.urls import path

from django.conf.urls.static import*
from django.conf import settings

from . views import accueil_view, actualites_view, actualite_detail_view, inscription_view, contact_view

urlpatterns = [
    path('cefa-admin/', admin.site.urls),

    # Les routes côté utilisateur
    path('', accueil_view, name = "accueil_url"),
    path('actualites/', actualites_view, name = "actualites_url"),
    path('actualite-detail/<int:id>/', actualite_detail_view, name = "actualite_detail_url"),
    path('inscription/', inscription_view, name = "inscription_url"),
    path('contacts/', contact_view, name = "contact_url"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)