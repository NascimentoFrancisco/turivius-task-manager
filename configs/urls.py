from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('application.urls.auth_urls')),
    path('api/v1/task/', include('application.urls.task_urls')),
]
