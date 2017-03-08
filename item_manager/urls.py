from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_item$', views.create_item, name='create_item'),
    url(r'^get_item$', views.get_item, name='get_item'),
    url(r'^update_item$', views.update_item, name='update_item'),
    url(r'^delete_item$', views.delete_item, name='delete_item'),
]
