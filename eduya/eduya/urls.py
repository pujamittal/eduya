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
from courses import views as courses_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.index),
    url(r'^test$', student_views.temp),
    url(r'^reset-password/$', reset_views.password_reset, name='password_reset'),
    url(r'^reset-password/done/$', reset_views.password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', reset_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password-complete/$', reset_views.password_reset_complete, name='password_reset_complete'),
    url(r'^register/$', student_views.registerUser, name='register'),
    url(r'^login/$', student_views.loginUser, name='login'),
    url(r'^logout/$', student_views.logoutUser, name='logout'),
    url(r'^reset/$', student_views.reset, name='reset'),
    url(r'^posts/', include('posts.urls')), #previously student_views.posts,
    url(r'^tutors/$', student_views.view_tutors, name='view_tutors'),
    url(r'^tutors/(?P<tutor_id>[0-9]+)/$', student_views.individual_tutor, name='individual_tutor'),
    url(r'^tutors/(?P<tutor_id>[0-9]+)/review/(?P<tutor_id2>[0-9]+)$', student_views.reviewTutor, name='review_tutor'),
    url(r'^profile/edit/$', student_views.update_profile, name='update_profile'),
    url(r'^profile/become_tutor/$', student_views.become_tutor, name='become_tutor'),
    url(r'^profile/$', student_views.my_profile, name='my_profile'),
    url(r'^my-courses/$', student_views.my_courses, name='my_courses'),
    url(r'^my-listings/$', student_views.my_listings, name='my_listings'),
    url(r'^subjects/$', courses_views.all_subjects, name='all_subjects'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/$', courses_views.all_courses, name='all_courses'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/$', courses_views.course, name='course'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/comment/$', courses_views.course_comment, name='course_comment'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/professors/(?P<professor_id>[0-9]+)/$', courses_views.professor, name='professor'),
    url(r'^professors/(?P<professor_id>[0-9]+)/$', courses_views.professor_direct, name='professor_direct'),
    url(r'^professors/(?P<professor_id>[0-9]+)/comment/$', courses_views.professor_direct_comment, name='professor_direct_comment'),
    url(r'^professors/$', courses_views.professors, name='professors'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/become_tutor_for_course/$', courses_views.become_tutor_for_course, name='become_tutor_for_course'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/add_course_to_student/$', student_views.add_course_to_student, name='add_course_to_student'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/remove_course_from_student/$', student_views.remove_course_from_student, name='remove_course_from_student'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/contribute_information/$', courses_views.contribute_information, name='contribute_information'),
    url(r'^subjects/(?P<subject_id>[A-Z]+)/courses/(?P<course_id>[0-9]+)/contributed_information/$', courses_views.contributed_information, name='contributed_information'),
]
