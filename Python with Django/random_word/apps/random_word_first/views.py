# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
  try:
    request.session["number"]
  except KeyError:
    request.session["number"] = 0

  return render(request, "random_word_first/index.html")

def generate(request):
  request.session["number"] += 1
  request.session["word"] = get_random_string(length=14)

  return redirect('/')

def reset(request):
  del request.session["number"]
  del request.session["word"] 

  return redirect('/')
# Create your views here.
