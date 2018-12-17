from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.select_computer, name='select_computer'),
    url(r'^new/$', views.add_computer, name='add_computer'),
    url(r'^results/(?P<computer_pk>\d+)/$', views.wol_results, name='wol_results'),
    url(r'^ping/(?P<computer_pk>\d+)/$', views.ping_computer, name='ping_computer'),
]