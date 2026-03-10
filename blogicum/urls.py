from django.contrib import admin
from django.urls import path, include  # ← Важно: include должна быть здесь!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
]