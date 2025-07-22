from django.contrib import admin
from django.urls import include, path
from factures import views

urlpatterns = [
    path("", views.home, name="home"),  # page d'accueil
    path("factures/", include("factures.urls")),
    path("admin/", admin.site.urls),
]