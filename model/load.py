from efficientnet.layers import Swish, DropConnect
from efficientnet.model import ConvKernalInitializer
from tensorflow.keras.utils import get_custom_objects
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image

get_custom_objects().update({
    'ConvKernalInitializer': ConvKernalInitializer,
    'Swish': Swish,
    'DropConnect':DropConnect
})

model = load_model("trained-model.h5")

def predict(img_file_path):
	img = keras_image.load_img(img_file_path, target_size=(150, 150)) #dimensions as defined in model
	x = keras_image.img_to_array(img)
	x = x.reshape((1,) + x.shape)
	x /= 255.
	result = model.predict([x])[0]
	
	return {"cat": result[0], "dog": result[1]}