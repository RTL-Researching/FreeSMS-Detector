# FreeSMS-Detector
### Intro
There are numerous websites out there that allow you to read SMS messages of specific phone numbers they have listed.

A person can try to use one of these phone numbers to receive an activation SMS message when creating an account on a website.
This script detects whether a phone number belongs to a "receive-free-sms" service or not.

This script builds a database containing these phone numbers, and that database can then be queried through python or a web API.

### Requirements
* Python 3.x

### Installation
Clone the git repo
```
$ git clone https://github.com/RTL-Researching/FreeSMS-Detector.git
```

Install the pip requirements
```
$ pip install -r requirements.txt
```
### Usage

##### Python

Populate the database
```
>>> from runner import *
>>> scrape_all()
```

Check for the presence of a specific phone number
```
>>> from runner import *
>>> check_phonenumber("+14165555555")
True
```

Note: '+14165555555' has to be in the database in order to have 'True' returned.

##### Web API

Start up the Python API (uses Flask) webserver
```
(venv) $ python api.py
```

Do a HTTP GET (ex. with a web browser)
* Specific phone number '+14165555555':
```
http://127.0.0.1:5000/api/v1/resources/phonebook/number/%2B14165555555
```
* Hash of a phone number '85e0c15377c5e0b4aac56743596968a4':
```
http://127.0.0.1:5000/api/v1/resources/phonebook/hash/85e0c15377c5e0b4aac56743596968a4
```
* Get all entries:
```
http://127.0.0.1:5000/api/v1/resources/phonebook/all
```

Note: All data posted with a HTTP GET must be 'URL Encoded'!
Ex:
* '**+14165555555**' becomes '**%2B14165555555**'
* '**+1 (416) 555-5555**' becomes '**%2B1%20%28416%29%20555-5555**'

### Components
This script consists of a few components:

* Crawler: populates the database
* API: allows a user to look up the presence of a phone number with a HTTP GET
