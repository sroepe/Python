# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
  
  return render(request, "sw_first_app/index.html")

def add(request):
  word = {} 
    
  for key, value in request.POST.iteritems():
    if key != "csrfmiddlewaretoken" and key!= "show-big":
      word[key] = value
    if key == "show-big":
      word["big"]="big"
    else: 
      word["big"] = ""
  
  word["time"] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
  
  try:
    request.session["words"]
  except KeyError:
    request.session["words"] = []

  list = request.session["words"]
  list.append(word)
  request.session["words"] = list

  for key, val in request.session.__dict__.iteritems():
    print key, val

 
  return redirect('/')
     

def clear(request):
  for key in request.session.keys():
    del request.session[key]

  return redirect('/')