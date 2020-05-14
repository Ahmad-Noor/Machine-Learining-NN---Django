from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from MyAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyAPI.urls')),

]
