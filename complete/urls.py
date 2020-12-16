from django.urls import path
from complete import views
from django.conf.urls import url

app_name = 'complete'
urlpatterns = [
    path('', views.complete, name="complete"),
]