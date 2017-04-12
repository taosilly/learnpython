from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	#ex: /polls/
	#url(R'^$', views.index, name='index'),
	#ex: /polls/5/
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	#ex: /polls/5/result/
	#url(R'^(?P<question_id>[0-9]+)/results$', views.result, name='results'),
	#ex: /polls/5/vote/
	#url(R'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote')

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
