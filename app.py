from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open('model/aqi_model.pkl', 'rb'))
except:
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pm25 = float(request.form['pm25'])
        pm10 = float(request.form['pm10'])
        
        # Make prediction
        features = np.array([[temperature, humidity, pm25, pm10]])
        prediction = model.predict(features)[0]
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
