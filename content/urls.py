from django.urls import path
from . import views

urlpatterns = [
    # TV Brands
    path('brands/', views.BrandListAPI.as_view(), name='brands'),
    
    # Firmware
    path('firmware/', views.FirmwareListAPI.as_view(), name='firmware-list'),
    path('firmware/<int:pk>/', views.FirmwareDetailAPI.as_view(), name='firmware-detail'),
    
    # Schematics
    path('schematics/', views.SchematicListAPI.as_view(), name='schematics-list'),
    path('schematics/<int:pk>/', views.SchematicDetailAPI.as_view(), name='schematics-detail'),
    
    # Download (محمي بتوكن)
    path('download/<str:token>/', views.DownloadFileAPI.as_view(), name='download-file'),
    path("add-firmware/", views.add_firmware_page, name="add-firmware"),
    path("firmware/create/", views.FirmwareCreateAPI.as_view(), name="firmware-create"),
]
# إضافة سوفتوير (صفحة HTML)
path('add-firmware/', views.add_firmware_page, name='add-firmware'),
path('add-firmware/api/', views.FirmwareCreateAPI.as_view(), name='firmware-create'),
