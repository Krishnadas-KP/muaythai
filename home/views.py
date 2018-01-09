from django.shortcuts import render
from Database import models

def index(request):
   return render(request,'home/index.html',{})
