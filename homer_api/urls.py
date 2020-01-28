
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from core import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.url')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
