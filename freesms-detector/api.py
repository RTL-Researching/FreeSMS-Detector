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

app.run()