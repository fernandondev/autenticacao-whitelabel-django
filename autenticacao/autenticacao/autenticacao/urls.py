
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.template.response import TemplateResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('usuarios.urls')),

]
