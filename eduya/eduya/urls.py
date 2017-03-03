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
from django.contrib.auth import views as reset_views

from students import views as student_views
from home import views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.index),
    url(r'^reset-password/$', reset_views.password_reset, name='password_reset'),
    url(r'^reset-password/done/$', reset_views.password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', reset_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password-complete/$', reset_views.password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', student_views.registerUser, name='register'),
    url(r'^login/$', student_views.loginUser, name='login'),
    url(r'^logout/$', student_views.logoutUser, name='logout'),
    url(r'^reset/$', student_views.reset, name='reset'),
    url(r'^posts/', include('posts.urls')),
    url(r'^tutors/$', student_views.all_tutors, name='all_tutors'),
    url(r'^tutors/(?P<tutor_id>[0-9]+)/$', student_views.individual_tutor, name='individual_tutor'),
    url(r'^profile/edit/$', student_views.update_profile, name='update_profile'),
    url(r'^profile/$', student_views.my_profile, name='my_profile')
]
