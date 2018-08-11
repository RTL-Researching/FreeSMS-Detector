import flask
from flask import jsonify
from runner import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
# Example query:
# http://127.0.0.1:5000/
def home():
    return '''<h1>FreeSMS-Detector</h1>'''


@app.route('/api/v1/resources/phonebook/all', methods=['GET'])
# Example query:
# http://127.0.0.1:5000/api/v1/resources/phonebook/all
def api_all():
    return jsonify(get_complete_phonebook())


@app.route('/api/v1/resources/phonebook/number/<pn>', methods=['GET'])
# Example query:
# http://127.0.0.1:5000/api/v1/resources/phonebook/number/%2B14165555555
#
# Make sure that the phonenumber is "urlencoded": a '+' becomes a '%2B', etc...
def api_pn(pn):
    return str(check_phonenumber(pn))


@app.route('/api/v1/resources/phonebook/hash/<pnh>', methods=['GET'])
# Example query:
# http://127.0.0.1:5000/api/v1/resources/phonebook/hash/85e0c15377c5e0b4aac56743596968a4
def api_pnh(pnh):
    return str(check_phonenumber_hash(pnh))


app.run()
