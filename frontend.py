from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        print(request.form)
        form_description = request.form["description"]
        print(form_description)
        form_points = request.form["points"]
        print(form_points)
        wine_label = request.form["wine-label"].lower()
        print(wine_label)
        review_site = request.form["review-site"].lower()
        print(review_site)

        return redirect(url_for('view_sign', description=form_description, points=form_points,
                                wine_label=wine_label, review_site=review_site))

    return render_template('home.html')


@app.route('/view-sign/<description>/<points>/<wine_label>/<review_site>', methods=["GET","POST"])
def view_sign(description, points,wine_label,review_site):
    description_var = description
    points_var = points
    wine_label_var = wine_label
    review_site_var = review_site


    return render_template('sign.html', description=description_var, wine_label=wine_label_var,
                           review_site=review_site_var, points=points_var)