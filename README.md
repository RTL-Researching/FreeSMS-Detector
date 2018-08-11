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

### Components
This script consists of a few components:

* Crawler: populates the database
* API: allows a user to look up the presence of a phone number with a HTTP GET

##### Crawler

##### API
