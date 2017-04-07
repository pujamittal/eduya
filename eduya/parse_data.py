import requests
import os
import json
import re

CURRENT_TERM = '41be50df-312c-440f-8bae-edd993c675b2' # FALL 2017
CAMPUS = '983c3fdc-f3f0-4f0b-a31c-c6f417e186fd' # WEST LAFAYETTE

buildings = {}
with open('Buildings') as f:
    buildings_json = json.load(f)
    for b in buildings_json['value']:
        if b['CampusId'] == CAMPUS:
            buildings[b['BuildingId']] = {'BuildingCode': b['ShortCode'], 'BuildingName':b['Name']}
    f.close()

rooms = {}
with open('Rooms') as f:
    rooms_json = json.load(f)
    for r in rooms_json['value']:
        if r['BuildingId'] in buildings:
            rooms[r['RoomId']] = buildings.get(r['BuildingId'])
            rooms[r['RoomId']]['RoomNumber'] = r['Number']
    f.close()

subjects = {}
with open('Subjects') as f:
    subjects_json = json.load(f)
    for s in subjects_json['value']:
        subjects[s['SubjectId']] = {'SubjectName': s['Name'], 'SubjectAbbreviation': s['Abbreviation']}
    f.close()

courses = {}
with open('Courses') as f:
    courses_json = json.load(f)
    for c in courses_json['value']:
        courses[c['CourseId']] = {'CourseNumber': c['Number'], 'Title': c['Title'], 'Subject': subjects.get(c['SubjectId']) }
    f.close()

purdue_unique_courses = {}
classes = {}
with open('Classes') as f:
    classes_json = json.load(f)
    for c in classes_json['value']:
        if c['TermId'] == CURRENT_TERM and c['CampusId'] == CAMPUS:
            if purdue_unique_courses.get(c['CourseId']) is None:
                purdue_unique_courses[c['CourseId']] = {'Course': courses.get(c['CourseId']), 'Sections': {}}
                classes[c['ClassId']] = {'Course': courses.get(c['CourseId']), 'Sections': {}}
    f.close()

sections = {}
with open('Sections') as f:
    sections_json = json.load(f)
    for s in sections_json['value']:
        if s['ClassId'] in classes:
            classes[s['ClassId']]['Sections'][s['SectionId']] = ({'ClassId': s['ClassId'], 'CRN': s['CRN'], 'Type': s['Type'], 'Meetings': {}})
            sections[s['SectionId']] = {'ClassId': s['ClassId'], 'CRN': s['CRN'], 'Type': s['Type'], 'Meetings': {}}
    f.close()

meetings = {}
with open('Meetings') as f:
    meetings_json = json.load(f)
    for m in meetings_json['value']:
        if m['SectionId'] in sections:
            my_class = classes[sections[m['SectionId']]['ClassId']]
            my_class['Sections'][m['SectionId']]['Meetings'][m['MeetingId']] = {'DaysOfWeek': m['DaysOfWeek'], 'StartTime': m['StartTime'], 'Room': rooms.get(m['RoomId'])}
    f.close()

with open('subjects.txt', 'w') as outfile:
    json.dump(classes, outfile)

with open('classes.txt', 'w') as outfile:
    json.dump(classes, outfile)
