from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("printblog.urls"), name="printblog-urls"),
    path('admin/', admin.site.urls),
]
