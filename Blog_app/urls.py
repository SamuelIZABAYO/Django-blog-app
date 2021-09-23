import django.conf
from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.post_delete, name='post_delete'),
    path('confirm_delete/<int:pk>', views.confirm_delete, name='confirm_delete'),
    path('<int:pk>', views.post_update, name='post_update'),
    # url('post.new/', views.post_create(), name='post_new'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('', views.post_list, name='home'),
]
# <slug:slug>
# post/<int:pk>/<slug>/
