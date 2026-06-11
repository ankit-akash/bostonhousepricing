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

    output = round(prediction[0], 2)

    return render_template(
        "home.html",
        prediction_text="The House price prediction is {}".format(output)
    )


# For Postman / API testing
@app.route('/predict_api', methods=['POST'])
def predict_api():

    data = request.json['data']

    final_input = np.array(list(data.values())).reshape(1, -1)

    scaled_data = scalar.transform(final_input)

    output = regmodel.predict(scaled_data)

    return jsonify(float(output[0]))


if __name__ == "__main__":
    app.run(debug=True)