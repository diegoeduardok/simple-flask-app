from glob import glob
import os
import time
from application import app
from flask import render_template, redirect, url_for, request, flash
from flask_uploads import UploadSet, configure_uploads, patch_request_class
from application.forms import UploadForm, photos
from application.secrets import upload_path #set upload path as appropriate
from model.load import predict

configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

def which_animal(prediction):
	if prediction['cat'] > 0.8:
		return "cat"
	elif prediction['dog'] > 0.8:
		return "dog"
	else:
		return "non-identified animal :/"

def clear_updates(path=upload_path):
	if not os.path.exists(path):
		os.makedirs(path)

	previous = glob(path + '/*')
	for f in previous:
		os.remove(f)

@app.route("/")
@app.route("/index")
@app.route("/usage")
def index():

	#get rid of previous images and create uploads
	clear_updates()

	return render_template("index.html", index=True)

@app.route("/application", methods=['GET', 'POST'])
def application():

	#get rid of previous images
	clear_updates()

	form = UploadForm()
	animal = None 
	file_url = None

	if form.validate_on_submit():
		for filename in request.files.getlist('photo'):
			name = str(time.time()).replace(".","")
			photos.save(filename, name=name + ".")
		upload = True
		file_url = photos.url(name + ".jpg")
		animal = which_animal(predict(photos.path(name + ".jpg")))
		flash("Image uploaded successfully!", category="success")
	else:
		upload = False

	return render_template('application.html', form=form, upload=upload, animal=animal, file_url=file_url, application=True)
