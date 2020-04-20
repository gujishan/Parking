from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'hello/', views.hello, name='hello'),
    url(r'addparking/', views.add_parking, name='add_parking'),
    url(r'getparking/', views.get_parking, name='get_parking'),
    url(r'reparking/(\d+)/', views.re_parking, name='re_parking'),
    url(r'updatepa/(\d+)/', views.update_parking, name='update_parking'),
    url(r'showincar/', views.show_incar, name='show_incar'),
    url(r'showallcar/', views.show_allcar, name='show_allcar'),
    url(r'money/', views.money, name='money'),
    url(r'tu/', views.tu, name='tu'),
    url(r'find/', views.find, name='find'),
    url(r'findall', views.find_all,name='find_all'),
    url(r'tumoney', views.tu_money,name='tu_money'),
    # url(r'test2/', views.test2),
]
