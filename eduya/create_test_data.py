import django
import datetime
django.setup()

from students.models import Student
from posts.models import Post

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