from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('ice_cream/', include('ice_cream.urls', namespace='ice_cream')),
    path('about/', include('about.urls', namespace='about')),
    path('admin/', admin.site.urls),
]
