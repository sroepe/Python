from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "ThisIsSecret"

@app.route('/')
def index():
  if "totalCount" not in session:
    session["totalCount"] = 0
  session["totalCount"] += 1
  return render_template("index.html", totalCount = session["totalCount"])

@app.route('/count', methods=["POST"])
def count():
  session["totalCount"] += 0
  if request.form["count2"] == "plus2":
    session["totalCount"] += 2
  return render_template("index.html", totalCount = session["totalCount"])

@app.route('/reset', methods=["POST"])
def reset():
  session.clear()
  return redirect('/')

app.run(debug=True) 
  


