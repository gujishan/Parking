from django.conf.urls import url

from InOut import views

urlpatterns = [
    url(r'hello', views.hello, name='hello'),
    url(r'carin/', views.car_in, name='car_in'),
    url(r'carout/', views.car_out, name='car_out'),
    url(r'pay/', views.pay, name='pay'),
]
