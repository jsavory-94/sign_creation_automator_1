from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        print(request.form)
        form_description = request.form["description"]
        print(form_description)
        form_points = request.form["points"]
        print(form_points)
        wine_label = request.files["wine-label"].lower()
        print(wine_label)
        print(type(wine_label))
        review_site = request.files["review-site"].lower()
        print(review_site)

        # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # file = request.files['file']
        # # if user does not select file, browser also
        # # submit an empty part without filename
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('uploaded_file',
        #                             filename=filename))


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