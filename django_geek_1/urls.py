from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('painel/', admin.site.urls),
    path('core/', include('core.urls')),
    
]
