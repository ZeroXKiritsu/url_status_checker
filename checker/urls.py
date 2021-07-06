from django.urls import path
from django.urls.resolvers import URLPattern
import checker.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("check_url", views.check_url, name="check_url"),
    path("update_url", views.update_url, name="update_url"),
]