from django.contrib import admin
from django.urls import path
from translate.views import translate_text
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', translate_text, name='translate_text'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

