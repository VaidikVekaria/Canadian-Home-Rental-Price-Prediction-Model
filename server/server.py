from flask import Flask, request, jsonify
from artifacts import util
app = Flask(__name__)

@app.route('/get_furnishing_names')
def get_furnishing_names():
    response = jsonify({'furnishing': util.get_furnishing_names()})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_type_names')
def get_type_names():
    response = jsonify({'type':util.get_type_names()})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


@app.route('/predict_home_price', methods= ['POST'])
def predict_home_price():
    latitude = float(request.form['latitude'])
    sq_feet = float(request.form['sq_feet'])
    longitude = float(request.form['longitude'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    type_ = request.form['type']
    furnishing = request.form['furnishing']

    response = jsonify({
        'estimated_price': util.get_estimated_price(latitude, longitude, sq_feet, bedrooms,bathrooms,type_, furnishing)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/hello')
def greeting():
    return 'Jay Shree Swaminarayan'

if __name__ == "__main__":
    print("Starting Python Flask Server for Canadian Home Rental Prediction!")
    app.run()

