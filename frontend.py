import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        wine_label = request.files["wine-label"]
        print(wine_label)
        print(type(wine_label))
        wine_label_secure = secure_filename(wine_label.filename)
        print(type(wine_label_secure))
        # wine_label_secure_1 = secure_filename(wine_label)
        # print(type(wine_label_secure_1))
        wine_label.save(os.path.join(app.config['UPLOAD_FOLDER'], wine_label_secure))

        # review_site = request.files["review-site"]
        # review_site_secure = secure_filename(review_site.filename)
        # review_site_secure.save(os.path.join(app.config['UPLOAD_FOLDER'], review_site_secure))

        description = request.form['description']
        points = request.form['points']

        return redirect(url_for('upload_file',
                                wine_label=wine_label_secure
                                ))


        # return redirect(url_for('view_sign', description=form_description, points=points,
        #                         wine_label=wine_label, review_site=review_site))

    return render_template('home.html')

@app.route('/uploads/<wine_label>')
def upload_file(wine_label):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               wine_label)



@app.route('/view-sign/<description>/<points>/<wine_label>/<review_site>', methods=["GET","POST"])
def view_sign(description, points,wine_label,review_site):
    description_var = description
    points_var = points
    wine_label_var = wine_label
    review_site_var = review_site


    return render_template('sign.html', description=description_var, wine_label=wine_label_var,
                           review_site=review_site_var, points=points_var)