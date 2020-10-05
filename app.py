from flask import Flask, render_template, request
import os
from forms import UploadForm
from werkzeug.utils import secure_filename
from fastai.vision import *


app = Flask(__name__, instance_relative_config=False)
app.config.from_object("config.DevConfig")
model = load_learner('.')


@app.route('/')
def home():
    form = UploadForm()
    return render_template("index.html", form=form)


@app.route('/upload', methods=["GET", "POST"])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        picture = form.picture.data
        filename = secure_filename(picture.filename)
        print(app.config['UPLOAD_FOLDER'])
        picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img = open_image("static/uploads/" + filename)
        pred_class, _, _ = model.predict(img)
        return render_template("success.html", pred_class=pred_class)


if __name__ == "__main__":
    app.run()
