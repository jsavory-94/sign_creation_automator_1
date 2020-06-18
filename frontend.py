import os
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask_weasyprint import HTML, render_pdf, CSS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        wine_label = request.files['wine-label']
        review_site = request.files['review-site']
        if review_site.filename == '':
            return redirect(url_for('home'))

        points = request.form['points']
        description = request.form['description']

        wine_label_filename = secure_filename(wine_label.filename)
        wine_label.save(os.path.join(app.config['UPLOAD_FOLDER'], wine_label_filename))

        review_site_filename = secure_filename(review_site.filename)
        review_site.save(os.path.join(app.config['UPLOAD_FOLDER'], review_site_filename))

        return render_template(
            'results.html',
            points=points,
            points_length=len(points),
            description=description,
            wine_label=wine_label_filename,
            review_site=review_site_filename,
            star='thick-star.png',
            blank='blank.jpg'
        )

    return render_template('home.html', logo='GS_logo.png')


@app.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploads/<wine_label>/<review_site>')
def upload_file(wine_label, review_site):
    wine_label_filename = wine_label
    review_site_filename = review_site

    return render_template('sign.html', wine_label=wine_label_filename, review_site_file=review_site_filename)


@app.route('/label.pdf', methods=['GET', 'POST'])
def render_label_as_pdf():
    if request.method == 'POST':
        wine_label = request.form['wine-label']

        review_site = request.form['review-site']

        points = request.form['points']
        points_length = len(points)

        description = request.form['description']

        star = request.form['star']

        blank = request.form['blank']

        html = render_template('results.html', wine_label=wine_label, review_site=review_site, points=points,
                               description=description, star=star, blank=blank, points_length=points_length)

    return render_pdf(HTML(string=html))
