"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cms_users_put import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.mostrar_todo, name='Mostrar paginas almacenadas'),
    url(r'^(\d+)$', views.mostrar_id, name='Acceso a page por id'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout', logout, {'next_page': '/'}),
    url(r'^login', login),
    # url(r'^(\w+)$', views.contenido, name='Accede y modifica contenido'),
    url(r'^(.+)', views.contenido, name='Accede y modifica contenido'),
]
