import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#test data.  replace with database

phonenumbers = [
    {'id': 0,
     'phonenumber': '+14167891234',
     'timestamp': '2018-08-11',
     'md5': 'c8ca4a0780d2028db2cd3439f805a040',
     'origin_url': ''},
    {'id': 1,
     'phonenumber': '+441823711087',
     'timestamp': '2018-08-11',
     'md5': 'c8ca4a0780d2028db2cd3439f805a044',
     'origin_url': ''},

]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>FreeSMS-Detector</h1>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/phonenumbers/all', methods=['GET'])
def api_all():
    return jsonify(phonenumbers)


@app.route('/api/v1/resources/phonenumbers', methods=['GET'])
def api_phonenumber():
    # Check if phone number was provided as part of the URL.
    # If yes, assign it to a variable.
    # If no, display an error in the browser.
    if 'phonenumber' in request.args:
        phonenumber = int(request.args['phonenumber'])
    else:
        return "Error: No phone number provided. Please specify one."

    # Create an empty list for our results
    results = []

    #
    for phonenumber in phonenumbers:
        if phonenumber['phonenumber'] == phonenumber:
            results.append(phonenumber)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()