
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # userprofile app urls
    path('', include('userprofile.urls')),


    # tasks app urls
    path('', include('tasks.urls')),

    # API urls/endpoints
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
