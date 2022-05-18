"""leveTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from api import views as user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'users', user.UserListViewSet.as_view(), name='user-list'),
    path(r'users/<str:pk>/', user.UserEditViewSet.as_view(), name='user-detail'),
    path(r'salaries', user.SalariesListViewSet.as_view(), name='salaries-list'),
    path(r'salaries/<str:pk>/', user.SalariesEditViewSet.as_view(),
         name='salaries-detail'),
    path(r'salaries-average', user.SalaryAverageViewset.as_view(),
         name='salaries-average'),
    path(r'salaries-average/<str:pk>/',
         user.SalaryAverageUserView.as_view(), name='salaries-average'),
    path(r'discount-average', user.AverageDiscountViewset.as_view(),
         name='discount-average'),
    path(r'discount-average/<str:pk>/',
         user.AverageDiscountUserView.as_view(), name='discount-average'),
    path(r'bigest-salary', user.BigestSalaryViewset.as_view(),
         name='bigest-salary'),
    path(r'bigest-salary/<str:pk>/',
         user.BigestSalaryUserView.as_view(), name='bigest-salary'),
    path(r'lowest-salary', user.LowestSalaryViewset.as_view(),
         name='lowest-salary'),
    path(r'lowest-salary/<str:pk>/',
         user.LowestSalaryUserView.as_view(), name='lowest-salary'),
]
