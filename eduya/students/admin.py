from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from students.models import *
from courses.models import Subject, Course, CourseSection, TeachingAssistant, Professor, TeachingAssistantCourse, ProfessorCourse


admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CourseSection)
admin.site.register(TeachingAssistant)
admin.site.register(Professor)
admin.site.register(TeachingAssistantCourse)
admin.site.register(ProfessorCourse)
admin.site.register(Tutor)