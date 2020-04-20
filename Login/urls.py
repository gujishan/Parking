from django.conf.urls import url

from Login import views

urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'register/', views.register, name='register'),
    url(r'root/', views.root, name='root'),
    url(r'ul/', views.ul, name='ul'),
    url(r'welcome/', views.welcome, name='welcome'),
    url(r'getall/',views.get_all,name='get_all'),
]
