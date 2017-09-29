from django.conf.urls import url
from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^spot/$', views.spot_price, name='spot'),
        url(r'^simple/$', views.simple, name='simple'),
        url(r'^name/$', views.get_name, name='name'),
        url(r'^fut/$', views.fut_curve, name='fut'),
        url(r'^test-upload/$', views.test_upload, name='test_upload')
        ]