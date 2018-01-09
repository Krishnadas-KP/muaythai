from django.shortcuts import render,redirect,get_object_or_404

from Database.models import Student,Referee

from .forms import FilterForm

def index(request):
	form=FilterForm(request.POST or None)
	context={
	"form" : form
	}
	if form.is_valid():
		cat = form.cleaned_data.get('category')
		sex = form.cleaned_data.get('sex')
		weight_cat = form.cleaned_data.get('weight_cat')
		minw = form.cleaned_data.get('weight_min')
		maxw = form.cleaned_data.get('weight_max')
		iminw=int(minw)
		imaxw=int(maxw)
		cat=int(cat)
		event = ''
		if cat==1:
			event='Sub Junior (Cadet) 10-11'
		elif cat==2:
			event='Sub Junior (Cadet) 12-13'
		elif cat==3:
			event='Junior (Youth) 14-15'
		elif cat==4:
			event='Junior (Youth) 16-17'
		elif cat==5:
			event='Senior 18-37'
		event=event+' '+sex+' '+weight_cat
		instance = Student.objects.filter(category=cat).filter(sex=sex).filter(weight__gte=iminw).filter(weight__lte=imaxw)
		data = {
			'category' : event,
			'student' : instance,
		}
		return render(request, 'filter/print.html',data)
		
	return render(request, 'filter/filter.html',context)

def referee(request):
	instance = Referee.objects.all()
	c = {
	    'ref' : instance,
	}
	return render(request,'filter/referee.html',c)
	
