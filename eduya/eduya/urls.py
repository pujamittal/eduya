"""eduya URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
=======
from django.contrib.auth.views import password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from students import views as student_views
>>>>>>> c576ab931976ad0304130c12a26f08c82102bf4c
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^account/password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^account/reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^register/$', views.register, {'sign_up': '/templates/sign_up.html'}, name='register'),
	url(r'^login/$', views.login, name='login'),
	url(r'^reset/$', view.reset, name='reset'),
]

=======
    url(r'^$', views.index),
    url(r'^account/password-change/$', password_change, name='password_change'),
    url(r'^account/password-change/done/$', password_change_done, name='password_change_done'),
    url(r'^account/password-reset/$', password_reset, name='password_reset'),
    url(r'^account/password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^account/reset-password/confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^account/reset/done/$', password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', student_views.register, name='register'),
    url(r'^login/$', student_views.login, name='login'),
    url(r'^reset/$', student_views.reset, name='reset')
]
>>>>>>> c576ab931976ad0304130c12a26f08c82102bf4c
