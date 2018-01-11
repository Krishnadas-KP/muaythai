from django.shortcuts import render,get_object_or_404
from Database.models import Student
from datetime import date
def calculate_age(d):
    today = date.today()
    age= today.year - d.year - ((today.month, today.day) < (d.month, d.day))
    return age

# Category 1 : Sub-junior 10-11
# Category 2 : Sub-junior 12-13
# Category 3 : Junior 14-15
# Category 4 : Junior 16-17
# Category 5 : Senior 18-37
def index(request):
   source = Student.objects.all()
   for i in source:
   	date=i.dob
   	cat=0
   	age=calculate_age(date)
   	if age<10 :
   	     cat=0
   	elif age==10 or age==11 :
   	     cat=1
   	elif age==12 or age==13 :
   	     cat=2
   	elif age==14 or age==15 :
   	     cat=3
   	elif age==16 or age==17 :
   	     cat=4
   	elif age>=18 and age<=37 :
   	     cat=5
   	elif age>37 :
   	     cat=6
   	q=get_object_or_404(Student,id=i.id)
   	q.age=age
   	q.category=cat
   	q.save()
   source = Student.objects.all()
   context = {'list' : source,}
   return render(request,'list/list.html',context)