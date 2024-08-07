from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from adminTao.views import *

urlpatterns = [
    path('riswan/', admin.site.urls),
    path('', include('apps.urls')),
    path('register', register, name='register'),
    path('tao', include('adminTao.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)