import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY")
	UPLOADED_PHOTOS_DEST = os.environ.get("UPLOADED_PHOTOS_DEST")