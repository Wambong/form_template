
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('form_templates/', include('form_templates.urls')),
    path('admin/', admin.site.urls),


]
