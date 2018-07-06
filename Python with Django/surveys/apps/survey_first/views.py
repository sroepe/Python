# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):

  return render(request, "survey_first/index.html")

def process(request):
  try:
    request.session["number"]
  except KeyError:
    request.session["number"] = 0
  
  request.session["name"] = request.POST["name"]
  request.session["city"] = request.POST["city"]
  request.session["language"] = request.POST["language"]
  request.session["description"] = request.POST["description"]
  request.session["number"] += 1

  return redirect("/result")

def result(request):

  return render(request, "survey_first/result.html")  

def goback(request):
  del request.session["number"]
  del request.session["name"] 
  del request.session["city"] 
  del request.session["language"] 
  del request.session["description"] 
  
  return redirect('/')
# Create your views here.
