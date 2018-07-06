
from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'wall')
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
    add_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first, :last, :email, :pw, NOW(), NOW())"
    user_data = { "first": request.form["first"],
                  "last" : request.form["last"],
                  "email": request.form["email"],
                  "pw": request.form["pw"]
    }
    user_id = mysql.query_db(add_user, user_data)
    session["name"] = request.form["first"]
    session["user_id"] = user_id

    return redirect('/wall')

  return redirect('/')


@app.route('/login', methods=["POST"])
def login(): 
  find_user = "SELECT * FROM users where email = :email"
  data = {  "email": request.form["email"] }
  found_user = mysql.query_db(find_user, data)
  userlength = len(found_user)

  if len(found_user) == 0:
    flash("No user registered with that email")
  else:  #the found_user[0] is the index of 0 in the found user list (aka array / dictionary); checking first element of list returned by query
    for x in range(0, userlength):  
      if found_user[x]["password"] != request.form["pw"]:
        flash("The password is incorrect")
      else: 
        session["name"] = found_user[x]["first_name"]
        session["found_user"] = found_user[x]["id"]
        return redirect('/wall')

  return redirect('/')

@app.route('/wall')  
def show_wall():

  messages = mysql.query_db("SELECT * from messages JOIN users on messages.user_id = users.id")
  #CONCAT(users.first_name, ' ', users.last_name) AS name, messages.created_at, messages.message FROM users JOIN messages on users.id = messages.user_id")
  messages.reverse()


  comments = mysql.query_db("SELECT * from comments JOIN users on comments.user_id = users.id")
  #SELECT CONCAT(users.first_name, ' ', users.last_name) AS name, message_id,comments.created_at, #comments.comment FROM users JOIN comments on users.id = comments.user_id JOIN messages on #comments.message_id = messages.id")
  
  return render_template('wall.html', messages = messages, comments = comments)

@app.route('/add', methods=["POST"])
def add_message():
  add_message_query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :id)"
  msg_data = {  "message": request.form["message"],
                "id": session["found_user"],
                   }
  msg_added = mysql.query_db(add_message_query, msg_data)

  return redirect('/wall')

@app.route('/comment', methods=["POST"])
def add_comment():

  add_comment_query = "INSERT INTO comments (message_id, comment, created_at, updated_at, user_id) VALUES (:mid, :comment, NOW(), NOW(), :uid)"
  comment_data = {  "mid": request.form["msg_id"],
                    "comment": request.form["comment"],
                    "uid": session["found_user"],
                   }

  comment_added = mysql.query_db(add_comment_query, comment_data)

  return redirect('/wall')

@app.route('/logoff')
def logoff():
  session.clear()
  return redirect('/')

app.run(debug=True) 