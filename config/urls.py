from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secure-control-panel-921/', admin.site.urls),
    path('', include('core.urls')),
]