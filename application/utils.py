from glob import glob
import os
from application.secrets import upload_path

def which_animal(prediction):
    if prediction['cat'] > 0.8:
        return "cat"
    elif prediction['dog'] > 0.8:
        return "dog"
    else:
        return "non-identified animal"

def clear_uploads(path=upload_path):
    if not os.path.exists(path):
        os.makedirs(path)

    previous = glob(os.path.join(path, 'photos', '*'))
    for f in previous:
        os.remove(f)