from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/ninjas')
def tmnt():
   return render_template("ninjas.html")

@app.route('/ninjas/<color>/')
def show_ninja(color):
    
  return render_template("ninja_color.html", color=color)  

app.run(debug=True)