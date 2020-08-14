from django.contrib import admin
from django.urls import path, include

from myapp.views import mainPage, logout_view

urlpatterns = [
    path("", mainPage, name="main"),
    path("logout/", logout_view, name="logout"),
    path('oauth/', include('social_django.urls'), name="oauth"),
    path('admin/', admin.site.urls),
]
