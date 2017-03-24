from django.conf.urls import url
from  . import views


urlpatterns = [
    # /balance/
    url(r'^$', views.index, name ='index'),
    # /balance/add_transaction
    # url(r'^$', views.index, name ='index'),

    # /balance/details <id number>
    url(r'^(?P<transaction_id>\w+)/$', views.detail, name='detail'),
]

