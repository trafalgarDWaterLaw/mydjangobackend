"""myserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^userinfo/', views.user_list),
    url(r'^productinfo/', views.product_list),
    url(r'productdetail', views.product_detail),
    url(r'^product/(?P<product_id>\d+)/$', views.getproduct),
    url(r'^component/p/(?P<p_id>\d+)/$', views.getcomponentfromproductid),
    url(r'component/c/(?P<c_id>\d+)/$', views.getcomponentfromcomponentid),
]
