from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    url(r'^', include('rule_manager.urls')),
]
