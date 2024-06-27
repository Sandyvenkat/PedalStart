from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_management_system_app.urls')),  # Include your app's URLs
]
