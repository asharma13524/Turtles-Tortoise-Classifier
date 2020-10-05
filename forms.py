from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField


class UploadForm(FlaskForm):
    picture = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'Images Only!'])])
    submit = SubmitField('Submit')