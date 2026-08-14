from django.contrib import admin
from django import forms
from .models import TVBrand, Firmware, Schematic, DownloadToken
import cloudinary.uploader

class CloudinaryUploadForm(forms.ModelForm):
    upload_file = forms.FileField(label='رفع ملف إلى Cloudinary', required=False)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if self.cleaned_data.get('upload_file'):
            file = self.cleaned_data['upload_file']
            result = cloudinary.uploader.upload(
                file,
                folder='serialcotv',
                resource_type='auto',
                format='webp',  # ← تحويل إلى WebP
                transformation=[
                    {'quality': 'auto'},
                    {'fetch_format': 'webp'}
                ]
            )
            instance.file_url = result['secure_url']
        
        if commit:
            instance.save()
        return instance

@admin.register(TVBrand)
class TVBrandAdmin(admin.ModelAdmin):
    form = CloudinaryUploadForm
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    form = CloudinaryUploadForm
    list_display = ('brand', 'model_number', 'version', 'token_cost', 'downloads_count', 'is_active')
    list_filter = ('is_active', 'brand')
    search_fields = ('model_number', 'brand__name', 'version')

@admin.register(Schematic)
class SchematicAdmin(admin.ModelAdmin):
    form = CloudinaryUploadForm
    list_display = ('brand', 'model_number', 'title', 'schematic_type', 'token_cost', 'downloads_count', 'is_active')
    list_filter = ('schematic_type', 'is_active', 'brand')
    search_fields = ('title', 'model_number', 'brand__name')

@admin.register(DownloadToken)
class DownloadTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'file_name', 'customer', 'used', 'created_at', 'expires_at')
    list_filter = ('used',)
    search_fields = ('token', 'file_name', 'customer__email')
    readonly_fields = ('token', 'created_at', 'expires_at')

admin.site.site_header = 'SerialCo TV Admin'
admin.site.site_title = 'SerialCo TV'
admin.site.index_title = 'Dashboard'