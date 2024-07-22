from django.urls import path
from . import views
from .views import apply_tender

urlpatterns = [
    path('register/', views.register_vendor, name='register_vendor'),
    path('create_tender/', views.create_tender, name='create_tender'),
    path('create_tender/<int:tender_id>/', views.create_tender, name='create_tender_with_id'),
    path('tenders/', views.tender_list, name='tender_list'),
    path('apply_tender/<int:tender_id>/', views.apply_tender, name='apply_tender'),
    path('apply_tender/', apply_tender, name='apply_tender'),
]

