"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 登陆请求
    path("login/", views.check_login),

    # 获取表格请求
    path("show/books/", views.show_books),
    path("show/users/", views.show_users),
    path("show/orders/", views.show_orders),
    path("show/payments/", views.show_payments),
    path("show/shoppingcart/", views.show_shoppingcart),

    # 增加或删除订单请求
    path("change/addorder/", views.add_order),
    path("change/deleteorder/", views.delete_order),
    path("change/changeorder/", views.change_order),

    path("query/infoorder/", views.infoorder)

]
