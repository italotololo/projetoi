
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('avisos/', include('avisos.urls')),
    path('boletim/', include('boletim.urls')),
    path('frequencia/', include('frequencia.urls')),
    path('comunicacao/', include('comunicacao.urls')),
    path('agenda/', include('agenda.urls')),
]


