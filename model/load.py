import efficientnet.tfkeras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from model.secrets import model_path

model = load_model(model_path + "/trained-model.h5")

def predict(img_file_path):
	img = keras_image.load_img(img_file_path, target_size=(150, 150)) #dimensions as defined in model
	x = keras_image.img_to_array(img)
	x = x.reshape((1,) + x.shape)
	x /= 255.
	result = model.predict([x])[0]
	
	return {"cat": result[0], "dog": result[1]}