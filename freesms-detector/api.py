import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#test data.  replace with database

phonenumbers = [
    {'id': 0,
     'phonenumber': '14167891234',
     'timestamp': '2018-08-11',
     'md5': 'c8ca4a0780d2028db2cd3439f805a040',
     'origin_url': ''},
    {'id': 1,
     'phonenumber': '441823711087',
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
def api_pn():
    # Check if an phonenumber  was provided as part of the URL.
    # If yes, assign it to a variable.
    # If no display error.
    if 'phonenumber' in request.args:
        number_query = request.args['phonenumber']
    else:
        return "Error: No phone number field provided. Please specify a phone number."

    # Create an empty list for our results
    #results = []

    # Loop through the data and match results that fit the requested phone number.
    for i in phonenumbers:
        if number_query in i['phonenumber']:
            answer = "yes"
        else:
            answer = "no"

    return answer

    #sample URL for Query
    #http: // 127.0.0.1: 5000 / api / v1 / resources / phonenumbers?phonenumber = 14167891234  <- returns no, even though it is in the list
    #http: // 127.0.0.1: 5000 / api / v1 / resources / phonenumbers?phonenumber = 441823711087  <- returns yes (as it should)


app.run()