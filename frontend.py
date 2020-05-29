import os
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
            wine_label = request.files['wine-label']
            review_site = request.files['review-site']

            if wine_label and review_site:
                wine_label_filename = secure_filename(wine_label.filename)
                wine_label.save(os.path.join(app.config['UPLOAD_FOLDER'], wine_label_filename))

                review_site_filename = secure_filename(review_site.filename)
                review_site.save(os.path.join(app.config['UPLOAD_FOLDER'], review_site_filename))

            return redirect(url_for('upload_file', review_site=review_site_filename, wine_label=wine_label_filename))

    else:
        flash('No file part')

        # return redirect(url_for('view_sign', description=form_description, points=points,
        #                         wine_label=wine_label, review_site=review_site))

    return render_template('home.html')

@app.route('/uploads/<wine_label>/<review_site>')
def upload_file(wine_label, review_site):
    # wine_label = send_from_directory(app.config['UPLOAD_FOLDER'], wine_label)
    # review_site = send_from_directory(app.config['UPLOAD_FOLDER'], review_site)

    wine_label_filename = wine_label
    review_site_filename = review_site

    return render_template('sign.html', wine_label=wine_label_filename, review_site_file=review_site_filename)



@app.route('/view-sign/<description>/<points>/<wine_label>/<review_site>', methods=["GET","POST"])
def view_sign(description, points,wine_label,review_site):
    description_var = description
    points_var = points
    wine_label_var = wine_label
    review_site_var = review_site


    return render_template('ticket.html', description=description_var, wine_label=wine_label_var,
                           review_site=review_site_var, points=points_var)