import django.conf
from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    path('confirm_delete/<int:pk>', views.confirm_delete, name='confirm_delete'),
    path('post_update/<int:pk>', views.post_update, name='post_update'),
    # url('post.new/', views.post_create(), name='post_new'),
    path('post_detail/<slug:slug>', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='home'),
]
# <slug:slug>
# post/<int:pk>/<slug>/
