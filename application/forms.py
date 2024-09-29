from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_uploads import UploadSet

photos = UploadSet('photos', extensions=('jpg', 'png'))

class UploadForm(FlaskForm):
    photo = FileField("Picture" ,validators=[FileAllowed(photos, 'Image Only!'), FileRequired('Choose a file!')])
    submit = SubmitField('Upload')