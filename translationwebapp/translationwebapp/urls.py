from django.contrib import admin
from django.urls import path
from translate.views import translate_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', translate_text, name='translate_text'),
]
