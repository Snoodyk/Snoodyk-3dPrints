from django.contrib import admin
from django.urls import path, include
from gallery import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('gallery/', include('gallery.urls'), name='gallery'),
    path('', include('printblog.urls'), name='printblog-urls'),
]
