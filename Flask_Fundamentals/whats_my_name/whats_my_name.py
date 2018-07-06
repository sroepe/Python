from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def new_form():
   return render_template("index.html")

@app.route('/process', methods=["POST"])
def process_form():
   print request.form["name"]
   return redirect("/")

app.run(debug=True)