import django
import requests
import os
import json
from courses.models import Subject, Course

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eduya.settings")
django.setup()

CURRENT_TERM = '41be50df-312c-440f-8bae-edd993c675b2' # FALL 2017
CAMPUS = '983c3fdc-f3f0-4f0b-a31c-c6f417e186fd' # WEST LAFAYETTE

subject_map = {}
subjects_request = requests.get('http://api.purdue.io/odata/Subjects')
subjects_request_data = dict(subjects_request.json())
for subject in subjects_request_data['value']:
    subject_map[subject['SubjectId']] = {'Name': subject['Name'], 'Abbreviation': subject['Abbreviation']}
    
# for subject in subject_map:
#     s = Subject()
#     s.abbreviation = subject_map[subject]['Abbreviation']
#     s.name = subject_map[subject]['Name']
#     s.save()

course_map = {}
courses_request = requests.get('http://api.purdue.io/odata/Courses')
courses_request_data = dict(courses_request.json())
for course in courses_request_data['value']:
    if subject_map.get(course['SubjectId']) is not None:
        course_map[course['CourseId']] = subject_map.get(course['SubjectId'])
        course_map[course['CourseId']]['Title'] = course['Title']
        course_map[course['CourseId']]['Number'] = course['Number']

    
current_term_courses = {}
current_term_classes = {}
classes_request = requests.get('http://api.purdue.io/odata/Classes')
classes_request_data = dict(classes_request.json())
for c in classes_request_data['value']:
    if c['TermId'] == CURRENT_TERM and c['CampusId'] == CAMPUS:
        current_term_classes[c['ClassId']] = course_map.get(c['CourseId'])
        current_term_classes[c['ClassId']]['CourseId'] = c['CourseId']
        if current_term_courses.get(c['CourseId']) is None:
            current_term_courses[c['CourseId']] = course_map.get(c['CourseId'])
        
f = open('courses.txt', 'w')
f.write(str(current_term_courses))
            
for course in current_term_courses:
    c = Course()
    c.subject = Subject.objects.get(abbreviation=current_term_courses[course]['Abbreviation'])
    c.title = current_term_courses[course]['Title']
    c.number = current_term_courses[course]['Number']
    c.save()