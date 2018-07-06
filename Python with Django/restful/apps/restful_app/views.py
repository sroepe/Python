# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):

  return render(request, "restful_app/index.html", { "Users": User.objects.all() })

def new(request):

  return render(request, "restful_app/new.html")

def create(request):

  if request.method == "POST":
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags=tag)
      return redirect('/users/{{User.id}}/edit')
    else:
      x = User.objects.create()
      x.first_name = request.POST["first_name"]
      x.last_name = request.POST["last_name"]
      x.email = request.POST["email"]
      x.save()
      #x.id = <id>
      #return redirect('/users')
      return redirect('/users')

def show(request, id):
  
  return render(request, "restful_app/show.html", { "User": User.objects.get(id = id)})

def edit(request, id):

  return render(request, "restful_app/edit.html", {"User": User.objects.get(id = id)})

def update(request, id):
  errors = User.objects.basic_validator(request.POST)
    
  if len(errors):
    for tag, error in errors.iteritems():
      messages.error(request, error, extra_tags=tag)
    return redirect('/users/{{User.id}}/edit')
    
  y = User.objects.get(id = id)
  y.first_name = request.POST["first_name"]
  y.last_name = request.POST["last_name"]
  y.email = request.POST["email"]
  y.save()

  return redirect('/users/{}'.format(id))

def destroy(request, id):
  User.objects.get(id = id).delete()

  return redirect('/users')

def goback(request):

  return redirect("/users")
