# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

def index(request):
  try:
    request.session["totalCoins"]
    request.session["log"]
  except KeyError:
    request.session["totalCoins"] = 0
    request.session["log"] = []

  log = request.session["log"]
  loglength = len(request.session["log"])
  log.reverse()

  return render(request, "ninja_gold_app/index.html")

def process(request):
  if request.POST["building"] == "farm":
    farmMoney = random.randrange(10,21)
    request.session["totalCoins"] += farmMoney
    myStr = "Found " + str(farmMoney) + " gold at the farm"
  if request.POST["building"] == "cave":
    caveMoney = random.randrange(5,11)
    request.session["totalCoins"] += caveMoney
    myStr = "Found " + str(caveMoney) + " gold in the cave"
  if request.POST["building"] == "house":
    houseMoney = random.randrange(2,6)
    request.session["totalCoins"] += houseMoney
    myStr = "Found " + str(houseMoney) + " gold in the house"
  if request.POST["building"] == "casino":
    casinoMoney = random.randrange(-50,51)
    request.session["totalCoins"] += casinoMoney
    if casinoMoney < 0:
      myStr = "Lost " + str(abs(casinoMoney)) + " gold at the casino:("
    else:
      myStr = "Won " + str(casinoMoney) + " gold at the casino! :O"

  request.session["log"].append(myStr)

  return redirect("/")
# Create your views here.
