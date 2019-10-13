"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from defaults import views as d_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', d_views.home, name='home'),
	url(r'^signup/$', d_views.signup, name='signup'),
	url(r'^contact/$', d_views.contact, name='contact'),
	url(r'^search/$', d_views.search, name='search'),
    path('admin/', admin.site.urls),
	#url(r'^$', defalut_view.home, name='home'),
]
