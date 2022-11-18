from tensorflow import keras
from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
import json

model = keras.models.load_model('static/model_1.h5')
def make_prediction(file):

    image = Image.open(BytesIO(file.read()))
    im2 = ImageOps.grayscale(image)
    img_28 = np.array(im2.resize((28, 28)))
    numpydata = np.asarray(img_28)
    #t = np.reshape(numpydata, [-1, 784])
    t  = numpydata.reshape((1,28,28,1))
    prediction = model.predict(t)
    if  prediction[0][np.argmax(prediction)] > 0.1:
        result = np.argmax(prediction)
        result = str(result)
    else:
        return "NA"
    json_dictionary = {ind:i for ind, i in enumerate(prediction[0].tolist())}
    pred_list = [i*100 for i in prediction[0].tolist()]
    return {"response" : result,"keys":list(json_dictionary.keys()), "values" :pred_list }
