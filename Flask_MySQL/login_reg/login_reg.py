from flask import Flask, render_template, request, redirect, session, flash
import md5
import os, binascii
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'login_reg')
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
  else: 
    email_exists = "SELECT * FROM users where email = :email"
    data = {  "email": request.form["email"] }
    found_user = mysql.query_db(email_exists, data)
    userlength = len(found_user)    
    for x in range(0, userlength):
      if found_user[x]["email"] == request.form["email"]:
        flash("This email already exists.")
        is_valid = False
  
  #first name validation
  if len(request.form["first"]) < 2:
    flash("First Name of 2 or more characters is required")
    is_valid = False
  elif not request.form["first"].isalpha():
    flash("First Name is invalid. A-Z / a-z only.")
    is_valid = False

  #last name validation
  if len(request.form["last"]) < 2:
    flash("Last Name of 2 or more characters is required")
    is_valid = False
  elif not request.form["last"].isalpha():
    flash("Last Name is invalid")
    is_valid = False
  
  #password validation
  password = request.form["pw"]
  salt = binascii.b2a_hex(os.urandom(15))
  hashed_password = md5.new(password + salt).hexdigest()
  if len(request.form["pw"]) < 1:
    flash("Password is required")
    is_valid = False
  elif len(request.form["pw"]) < 8:
    flash("Password must be 8 or more characters in length")
    is_valid = False

  #password confirmation validation
  if len(request.form["pwconfirm"]) < 1:
    flash("Password Confirmation is required")
    is_valid = False
  elif request.form["pwconfirm"] != request.form["pw"]:
    flash("This does not match the password you entered above")
    is_valid = False

  if is_valid:  #redirect to a new page, if not valid redirect to a different page
    flash("Thank you {} for submitting your information!".format(request.form["first"]))
    add_user = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first, :last, :email, :hashed_pw, :salt, NOW(), NOW())"
    user_data = { "first": request.form["first"],
                  "last" : request.form["last"],
                  "email": request.form["email"],
                  "hashed_pw": hashed_password,
                  "salt": salt,
                      }
    user_id = mysql.query_db(add_user, user_data)
    session["name"] = request.form["first"]
    session["user_id"] = user_id
    return redirect('/login_reg')

  return redirect('/')


@app.route('/login', methods=["POST"])
def login(): 
  password = request.form["pw"]
  salt = binascii.b2a_hex(os.urandom(15))
  hashed_password = md5.new(password + salt).hexdigest()

  find_user = "SELECT * FROM users where email = :email AND password = :hashed_pw"
  data = {  "email": request.form["email"],
            "hashed_pw": hashed_password,
            }
  found_user = mysql.query_db(find_user, data)
  userlength = len(found_user)    

  if len(found_user) == 0:
    flash("No user registered with that email")
  else:  #the found_user[0] is the index of 0 in the found user list (aka array / dictionary); checking first element of list returned by query
    for x in range(0, userlength):
      if found_user[x]["email"] == request.form["email"]:
        flash("This email already exists.")
        is_valid = False
      elif found_user[x]["hashed_password"] != request.form["pw"]:
        flash("The password is incorrect")
      else: 
        session["name"] = found_user[x]["first_name"]
        session["found_user"] = found_user[x]["id"]
      return redirect('/login_reg')

  return redirect('/')

#super important - do NOT remove!
@app.route('/login_reg')  
def show_wall():

  return render_template('login_reg.html')
'''
@app.route('/add', methods=["POST"])
def add_message():
  add_message_query = "INSERT INTO messages (message, created_at, updated_at) VALUES (:message, NOW(), NOW())"
  msg_data = {  "message": request.form["message"],
                   }
  msg_added = mysql.query_db(add_message_query, msg_data)
  flash("Your message has been posted")

   
  return redirect('/wall')
'''
@app.route('/logoff')
def logoff():
  session.clear()
  return redirect('/')

app.run(debug=True) 