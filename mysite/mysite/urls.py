from django.contrib import admin
from django.urls import path

from mysite.contollers.default_controller_file import defalt_point

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/default", defalt_point)
]
