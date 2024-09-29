import time
from application import app
from flask import render_template, redirect, url_for, request, flash
from flask_uploads import UploadSet, configure_uploads, patch_request_class
from application.forms import UploadForm, photos
from application.secrets import upload_path, secret_key #set upload path as appropriate
from application.utils import *
from model.load import predict

app.config['UPLOADS_DEFAULT_DEST'] = upload_path
app.config['SECRET_KEY'] = secret_key

configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

@app.route("/")
@app.route("/index")
@app.route("/usage")
def index():

	#get rid of previous images and create uploads
	clear_uploads()

	return render_template("index.html", index=True)

@app.route("/application", methods=['GET', 'POST'])
def application():

	#get rid of previous images
	clear_uploads()

	form = UploadForm()
	animal = None 
	file_url = None

	if form.validate_on_submit():
		for filename in request.files.getlist('photo'):

			name = str(time.time()).replace(".","")
			photos.save(filename, name=name + ".")
			extension = filename.filename.split(".")[-1]
			assert (2 < len(extension) < 5)
		upload = True
		file_url = photos.url(name + "." + extension)
		animal = which_animal(predict(photos.path(name + "." + extension)))
		flash("Image uploaded successfully!", category="success")
	else:
		upload = False

	return render_template('application.html', form=form, upload=upload, animal=animal, file_url=file_url, application=True)
