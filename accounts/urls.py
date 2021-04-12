from django.conf.urls import url, include
from accounts import views


urlpatterns = [
    url(r"^$", views.index, name="home"),
]
