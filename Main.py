import numpy as np
from flask import Flask, request, jsonify, render_template
from API import get_prediction

app = Flask(__name__)


from tensorflow.keras.models import load_model

# Load the model
model_path = "model/Prediction_model.h5"
model = load_model(model_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    global model_path
    # Get the URL from the form data
    url = request.form['inputUrl']
    
    # Get the prediction
    prediction = get_prediction(url, model_path)
    
    # Return the prediction as a JSON response
    #return jsonify({'prediction': prediction})
    return render_template('home.html', Result=f"There is {prediction}% chance that url is malicious")

if __name__ == '__main__':
    app.run(debug=True)
