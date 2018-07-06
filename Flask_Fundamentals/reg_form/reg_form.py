from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key= "ThisIsSecret"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/register', methods=["POST"])
def register():
  is_valid = True  
  
  #email validation
  if len(request.form["email"]) < 1:
    flash("Email is required")
    is_valid = False
  elif not EMAIL_REGEX.match(request.form["email"]):
    flash("This is not a valid email format")
    is_valid = False
  
  #first name validation
  if len(request.form["first"]) < 1:
    flash("First Name is required")
    is_valid = False
  elif not request.form["first"].isalpha():
    flash("First Name is invalid")
    is_valid = False

  #last name validation
  if len(request.form["last"]) < 1:
    flash("Last Name is required")
    is_valid = False
  elif not request.form["last"].isalpha():
    flash("Last Name is invalid")
    is_valid = False
  
  #password validation
  if len(request.form["pw"]) < 1:
    flash("Password is required")
    is_valid = False
  elif len(request.form["pw"]) < 9:
    flash("Password must be 9 or more characters in length")
    is_valid = False

  #password confirmation validation
  if len(request.form["pwconfirm"]) < 1:
    flash("Password Confirmation is required")
    is_valid = False
  elif request.form["pwconfirm"] != request.form["pw"]:
    flash("This does not match the password you entered above")
    is_valid = False

  if is_valid:
    flash("Thank you {} for submitting your information!".format(request.form["first"]))

  return redirect('/')


app.run(debug=True) 