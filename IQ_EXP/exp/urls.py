from django.conf.urls import url
from . import views
import utils.calculate_score

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^set/(\d{1,2})/$',views.set,name='set'),
	# url(r'^result/$',views.result,name='result'),
	url(r'^result/(\d{1,2})$',views.result,name='result'),
	url(r'^result/scores/(\d{1,2})/$',views.scores,name='scores'),
]
