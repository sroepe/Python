from flask import Flask, render_template, request, redirect, session
import random
from datetime import time
app = Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def index():
  if "totalCoins" not in session:
    session["totalCoins"] = 0
  if "log" not in session:
    session["log"] = []
  
  loglength = len(session["log"])
  revList = list(reversed(session["log"]))

  return render_template("index.html", totalCoins = session["totalCoins"], log = revList, loglength = loglength)

@app.route('/process_money', methods=["POST"])
def process_money():
  if request.form["building"] == "farm":
    farmMoney = random.randrange(10,21)
    session["totalCoins"] += farmMoney
    myStr = "Found " + str(farmMoney) + " gold at the farm"
  if request.form["building"] == "cave":
    caveMoney = random.randrange(5,11)
    session["totalCoins"] += caveMoney
    myStr = "Found " + str(caveMoney) + " gold in the cave"
  if request.form["building"] == "house":
    houseMoney = random.randrange(2,6)
    session["totalCoins"] += houseMoney
    myStr = "Found " + str(houseMoney) + " gold in the house"
  if request.form["building"] == "casino":
    casinoMoney = random.randrange(-50,51)
    session["totalCoins"] += casinoMoney
    if casinoMoney < 0:
      myStr = "Lost " + str(abs(casinoMoney)) + " gold at the casino:("
    else:
      myStr = "Won " + str(casinoMoney) + " gold at the casino! :O"

  session["log"].append(myStr)

  return redirect('/')

@app.route('/newgame') 
def newgame():
  session.clear()
  return redirect('/')

app.run(debug=True) 