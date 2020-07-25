"""bill_split URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bill_split_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('create_members/',views.create_members,name="create_members"),
    path('register',views.register,name="register"),
    path('bill/',views.bill,name="bill"),
    path('add_expenditure/<int:member_id>',views.add_expenditure,name="add_expenditure"),
    path('calculate/',views.calculate,name="calculate"),
    path('result/',views.result,name="result"),
]