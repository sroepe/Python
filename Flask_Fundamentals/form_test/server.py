from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "notyourkey"

@app.route('/')
def index():
  return render_template("index.html", name ="Sara", email="abc@123.com")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   
   session["name"] = request.form['name']
   session["email"] = request.form['email']
   sec
   return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('users.html', name=session["name"], email=session["name"])

app.run(debug=True) 

print request.form
