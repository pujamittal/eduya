import django
import requests
import os
import json
import re
from courses.models import Subject, Course, CourseSection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eduya.settings")
django.setup()

# save all subjects
with open('subjects.txt') as f:
    subjects_json = json.load(f)
    for subject in subjects_json:
        s = Subject()
        s.name = subjects_json[subject]['SubjectName']
        s.abbreviation = subjects_json[subject]['SubjectAbbreviation']
        s.save()

# save all courses and courses
with open('classes.txt') as f:
    classes_json = json.load(f)
    for c in classes_json:
        course = classes_json[c]['Course']
        new_course = Course()
        new_course.subject = Subject.objects.filter(abbreviation=course['Subject']['SubjectAbbreviation'])[0]
        new_course.title = course['Title']
        new_course.number = course['CourseNumber']
        new_course.save()
    
        sections = classes_json[c]['Sections']
        for s in sections:
            new_course_section = CourseSection()
            new_course_section.course = new_course
            new_course_section.section_type = sections[s]['Type']
            new_course_section.crn = sections[s]['CRN']
            new_course_section.meetings = sections[s]['Meetings']
            new_course_section.save()
