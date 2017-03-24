from django.conf.urls import url
from  . import views


urlpatterns = [
    # /balance/
    url(r'^$', views.index, name ='index'),

    # /balance/add_transaction
    # url(r'add/$', views.create_new_transaction, name ='add'),

    url(r'register/^$', views.UserFormView.as_view(), name='user_register'),


    # /balance/details <id number>
    url(r'^(?P<transaction_id>\w+)/$', views.detail, name='detail'),
]

