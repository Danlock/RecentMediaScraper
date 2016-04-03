from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # name=movies
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # name=anime
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # name=tvshow
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]