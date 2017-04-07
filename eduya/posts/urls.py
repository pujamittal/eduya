from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='posts'),
    url(r'^new/$', views.new_post, name='new_post'),
    url(r'(?P<post_id>[0-9]+)/$', views.post, name='post')
]