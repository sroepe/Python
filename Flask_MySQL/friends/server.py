from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')


@app.route('/')
def index():
  query = "SELECT * FROM friends"
  friends = mysql.query_db("SELECT * FROM friends")
  #all_friends = mysql.query_db(get_all_friends_query)
  print friends
  return render_template('index.html', all_friends=friends)

# an example of running a query
  #print mysql.queryd_b("SELECT * FROM users")

@app.route('/add_friend', methods=['POST'])
def add_friend():
  add_friend_query = "INSERT INTO friends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, :friend_since, NOW(), NOW())"

  data = {  'name': request.form["name"],
            'age': request.form["age"],
            'friend_since': request.form["friend_since"]  }

  mysql.query_db(add_friend_query, data)
  return redirect('/')

app.run(debug=True)
