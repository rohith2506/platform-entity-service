from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_item$', views.create_item, name='create_item'),
]
