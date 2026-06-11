import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')


# For HTML form submission
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)
    scaled_data = scalar.transform(final_input)
    
    prediction = regmodel.predict(scaled_data)
    
    # 1. Extract the raw prediction value
    raw_output = prediction[0]
        
    # 2. Multiply by 20 to scale it up to realistic modern prices (e.g., $23.26 becomes $465.20k)
    modern_output = prediction[0] * 20 
    
    # 3. Use max() to ensure the output is not negative, and round to 2 decimal places
    output = round(max(0.0, float(modern_output)), 2)

    return render_template(
        "home.html",
        prediction_text="The House price prediction is ${}k".format(output)
    )



# For Postman / API testing
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    final_input = np.array(list(data.values())).reshape(1, -1)
    scaled_data = scalar.transform(final_input)
    
    prediction = regmodel.predict(scaled_data)
    
    # Use max() to clip negative values to 0 for the API response
    output = max(0.0, float(prediction[0]))

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)