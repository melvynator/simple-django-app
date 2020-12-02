from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views._form_view, name='form'),
]