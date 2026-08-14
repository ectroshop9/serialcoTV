from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from serials.views import chargily_webhook

def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html dir="rtl" lang="ar">
    <head><meta charset="UTF-8"><title>SerialCo TV API</title></head>
    <body>
        <h1>SerialCo TV API</h1>
        <p>Serial System</p>
    </body>
    </html>
    """)

def health(request):
    return JsonResponse({
        'status': 'ok',
        'service': 'SerialcoTV',
        'version': '1.0'
    })

urlpatterns = [
    path('', home, name='home'),
    path('health/', health, name='health'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/content/', include('content.urls')),
    path('api/serials/', include('serials.urls')),
    path('api/webhook/chargily/', chargily_webhook, name='chargily-webhook'),
]