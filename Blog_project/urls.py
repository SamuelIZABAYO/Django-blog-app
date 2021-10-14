"""Blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Blog_app.sitemaps import PostSitemap
from django.conf.urls import include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

app_name = 'blog'
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', include(('admin_honeypot.urls', 'admin_honeypot'), namespace='admin_honeypot')),
    path('admin-panel/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
    path('blog/', include('Blog_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
