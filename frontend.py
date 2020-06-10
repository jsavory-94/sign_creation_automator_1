import os
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from flask_weasyprint import HTML, render_pdf
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
            points = request.form['points']
            description = request.form['description']

            print(f'wine_label : {wine_label}')
            print(f'review site : {review_site}')
            print(f'points : {points}')
            print(f'description : {description}')

            wine_label_filename = secure_filename(wine_label.filename)
            wine_label.save(os.path.join(app.config['UPLOAD_FOLDER'], wine_label_filename))
            # wine_label.save(os.path.join(r" C:\Users\Setup\Desktop\PycharmProjects - Mar30\sign_creation_automator\uploads", wine_label_filename))

            review_site_filename = secure_filename(review_site.filename)
            review_site.save(os.path.join(app.config['UPLOAD_FOLDER'], review_site_filename))

            description_padding = 'Lorem ipsum dolor sit amet, con sit amet' #filler text to prevent partial text cutoff in desription box
            print(f"wine label filename: {wine_label_filename}")
            print(f"wine label filename: {review_site_filename}")

            return render_template(
                'results.html',
                points=points,
                points_length = len(points),
                description=description,
                wine_label=wine_label_filename,
                review_site=review_site_filename,
                star='thick-star.png',
                padding = description_padding,
                blank='blank.jpg'
            )

    return render_template('home.html', logo='GS_logo.png')


@app.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/uploads/<wine_label>/<review_site>')
def upload_file(wine_label, review_site):
    # wine_label = send_from_directory(app.config['UPLOAD_FOLDER'], wine_label)
    # review_site = send_from_directory(app.config['UPLOAD_FOLDER'], review_site)

    wine_label_filename = wine_label
    review_site_filename = review_site

    return render_template('sign.html', wine_label=wine_label_filename, review_site_file=review_site_filename)


@app.route('/pdf')
def render_pdf():
    html = render_template('results.html')
    return render_pdf(string=HTML(html))