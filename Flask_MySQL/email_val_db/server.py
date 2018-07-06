from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validations')


@app.route('/')
def index():
  #query = "SELECT * FROM friends"
  #friends = mysql.query_db("SELECT * FROM friends")
  #all_friends = mysql.query_db(get_all_friends_query)
  #print friends
  return render_template('index.html')

app.run(debug=True)
