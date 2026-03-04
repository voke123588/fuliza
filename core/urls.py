from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agent/<int:request_id>/', views.agent, name='agent'),
    path('check-status/<int:request_id>/', views.check_status, name='check_status'),
    path('success/<int:request_id>/', views.success, name='success'),
    path('rejected/<int:request_id>/', views.rejected, name='rejected'),
]