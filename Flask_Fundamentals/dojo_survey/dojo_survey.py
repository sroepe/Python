from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")


@app.route('/result', methods=["POST"])
def result():
  name = request.form["name"]
  city = request.form["city"]
  language = request.form["language"]
  description = request.form["description"]
  return render_template("result.html", name = name, city = city, language = language, description = description)

app.run(debug=True)
