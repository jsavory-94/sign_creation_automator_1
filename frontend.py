from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST"])
def home():
    if request.method == 'POST':
        print(request.form)
        form_description = request.form["description"]
        print(form_description)
        form_points = request.form["points"].lower()
        print(form_points)

        return render_template('home.html')