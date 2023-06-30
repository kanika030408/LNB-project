from tensorflow import keras
from Feature_Extractor import extract_features

#return probability value that url is fake or not

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")
    prediction = model.predict([url_features])

    i = prediction[0][0] * 100
    i = round(i,3)
    print(f"There is {i}% chance,the url is malicious !")

    return i
