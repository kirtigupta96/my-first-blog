"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
import signup.views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^login/', login, name=login),
    '''url(r'^logout/$', signup.views.logout_page, name=signup.views.logout_page),
    #url(r'^accounts/login/$',login, name=login),  # If user is not login it will redirect to login page
    url(r'^register/$', signup.views.register, name=signup.views.register),
    url(r'^register/success/$', signup.views.register_success, name=signup.views.register_success),
    url(r'^home/$', signup.views.home, name=signup.views.home),

    # url(r'^signup/$', register),
'''
]
