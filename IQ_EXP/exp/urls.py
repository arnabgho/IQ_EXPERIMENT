from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^set_1/$',views.set_1,name='set_1'),
]
