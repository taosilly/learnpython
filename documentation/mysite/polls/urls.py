from django.conf.urls import url
from . import views

urlpatterns = [
	url(R'^$', views.index, name='index'),
]
