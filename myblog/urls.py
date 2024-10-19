# myblog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # myblog/urls.py
    path('accounts/', include('allauth.urls')),

]
