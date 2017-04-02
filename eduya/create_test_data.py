import django
import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eduya.settings")
django.setup()

from students.models import Student
from posts.models import Post
from courses.models import Subject, Course, CourseSection, TeachingAssistant, Professor, Review

# Create 3 Test Students
s1 = Student(email="hallendo2@purdue.edu", password="terminated54", first_name="Hans", last_name="Allendorfer", is_tutor=False)
s2 = Student(email="ankit2@purdue.edu", password="yuh1235BBB", first_name="Ankit", last_name="Pancakes", is_tutor=True)
s3 = Student(email="usmann2@purdue.edu", password="usmannrocks96", first_name="Usmann", last_name="Khan", is_tutor=True)
s1.save()
s2.save()
s3.save()

# Create 3 Test Posts
p1 = Post(student=s1, subject="CS", course="CS307", location="Hicks Library", datetime=datetime.datetime.now(), price=8.50, notes="N/A")
p2 = Post(student=s1, subject="CS", course="CS348", location="Krannert", datetime=datetime.datetime.now(), price=10.00, notes="My phone number is 1-888-812-1245")
p3 = Post(student=s2, subject="CS", course="CS354", location="Hicks Library", datetime=datetime.datetime.now(), price=8.50, notes="1 hr session")
p1.save()
p2.save()
p3.save()

# Create 3 Test Subjects
ts1 = Subject(name='CHM')
ts2 = Subject(name='EAPS')
ts3 = Subject(name='CS')
ts1.save()
ts2.save()
ts3.save()

# Create Test Courses
c1 = Course(subject=ts3, title='Introduction To The Analysis Of Algorithms', course_id='CS38100')
c2 = Course(subject=ts3, title='Data Structures and Algorithms', course_id='CS25100')
c3 = Course(subject=ts3, title='Computer Architecture', course_id='CS25000')
c4 = Course(subject=ts1, title='Intro Inorganic Chem', course_id='CHM24100')
c5 = Course(subject=ts1, title='General Chemistry II', course_id='CHM11600')
c6 = Course(subject=ts2, title='Planet Earth', course_id='EAPS10000')
c7 = Course(subject=ts2, title='Oceanography', course_id='EAPS10400')
c8 = Course(subject=ts2, title='Climate, Science and Society', course_id='EAPS32700')
c9 = Course(subject=ts2, title='Structural Geology', course_id='EAPS35200')
c1.save()
c2.save()
c3.save()
c4.save()
c5.save()
c6.save()
c7.save()
c8.save()
c9.save()

# Create Test Course Sections
cs1 = CourseSection(course=c6, rooms='Wetherill Lab of Chemistry 200', times='12:00 pm - 1:15 pm, TR')
cs2 = CourseSection(course=c6, rooms='Wetherill Lab of Chemistry 250', times='12:00 pm - 1:15 pm, TR')
cs3 = CourseSection(course=c6, rooms='Lawson Building 300', times='12:30 pm - 1:20 pm, MWF')
cs4 = CourseSection(course=c2, rooms='Lawson B136', times='12:30 pm - 1:20 pm, MWF')
cs5 = CourseSection(course=c1, rooms='Lawson B137', times='12:30 pm - 1:20 pm, MWF')
cs6 = CourseSection(course=c3, rooms='Lawson B138', times='12:30 pm - 1:20 pm, MWF')
cs1.save()
cs2.save()
cs3.save()
cs4.save()
cs5.save()
cs6.save()


