# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):

  return render(request, 'course_app/index.html', { "Courses": Course.objects.all() })

def add(request):
  errors = Course.objects.validate(request.POST)
  if errors:
    for err in errors:
      error(request, err)
  else:
    x = Course.objects.create()
    x.name = request.POST["name"]
    x.desc = request.POST["desc"]
    x.save()

    print x
  return redirect('/')

def destroy(request, id):

 return render(request, 'course_app/delete.html', { "Course": Course.objects.get(id = id)})

def permdelete(request, id):
  if request.POST["delbut"] == "Yes! I want to delete this.":
    Course.objects.get(id = id).delete()

    return redirect('/')

  else:

    return redirect('/') 

# Create your views here.
