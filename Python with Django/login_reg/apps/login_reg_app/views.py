# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
  return render(request, "login_reg_app/index.html")

def register(request):
  results = User.objects.reg_validate(request.POST)

  if results['status'] == False:
    for error in results['errors']:
      messages.error(request, error)
    return redirect('/')

  request.session["first_name"] = results["user"].first_name
  request.session["email"] = results["user"].email   ###remove if not working
  messages.success(request, 'You have successfully registered!')
  return redirect('/success')

def login(request):
  results = User.objects.log_validate(request.POST)

  if results["status"] == False:
    messages.error(request, "Please check your email and password and try to login again.")
    return redirect('/')
  request.session["email"] = results["user"].email
  request.session["first_name"] = results["user"].first_name  
  request.session["id"] = results["user"].id
  messages.success(request, "You have successfully logged in!")
  return redirect('/success')

def success(request):
  try:
    request.session['email']
  except KeyError:
    return redirect('/')

  return render(request, "login_reg_app/success.html")

def logout(request):
  request.session.flush()
  return redirect('/')

# Create your views here.
