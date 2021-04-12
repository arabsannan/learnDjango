from django.conf.urls import url,include
from todoapp import views


urlpatterns = [
    url(r"^$",views.onboarding, name="home"),
    url(r"^app/$",views.index, name="home"),

    url(r"^api/v1/create-task/$",views.create_task, name="create-task"),
]