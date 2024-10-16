from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.api.viewsets import *


router = routers.DefaultRouter()

router.register(r'requisicoes-recebidas', RequisicoesRecebidasViewSet, basename='requisicoes-recebidas')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

