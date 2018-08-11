import phonenumbers
import sqlite3
import hashlib
import os
import re

def get_clean_phonenumber(phonenumber):
    # Tries to clean up a phonenumber according to the E.164 format.
    # When succeeded, returns the E.164 formatted phonenumber;
    # if not: returns a 'None' object

    try:
        pn = phonenumbers.parse(phonenumber, None)
    except phonenumbers.phonenumberutil.NumberParseException:
        #print("Not a valid phone number: ", phonenumber)
        return None

    pn = phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164)

    return pn


def create_connection(db_file="phonebook.sqlite"):
    # Establish a connection with the SQLite db.

    package_dir = os.path.abspath(os.path.dirname(__file__))
    db_full_path = os.path.join(package_dir, "..", "data", db_file)
    print(db_full_path)
    try:
        conn = sqlite3.connect(db_full_path)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def insert_phonenumber(phonenumber, originurl=""):
    # Try to insert a phonenumber in the database
    # This takes 'dirty' phonenumbers too and tries to clean them up

    pn = get_clean_phonenumber(phonenumber)

    if pn is not None:
        md5 = hashlib.md5(pn.encode('utf-8')).hexdigest()

        values = (pn, md5, originurl)
        sql = ''' INSERT INTO phonenumbers(phonenumber,md5,originurl) VALUES(?,?,?) '''

        con = create_connection()

        cur = con.cursor()
        cur.execute(sql, values)

        con.commit()
        con.close()


def check_phonenumber(phonenumber):
    # Checks whether a phonenumber is known in the database
    # This takes 'dirty' phonenumbers too and tries to clean them up
    # It returns 'True' when found; 'False' when not present

    result = False
    pn = get_clean_phonenumber(phonenumber)

    if pn is not None:
        values = (pn,)
        sql = ''' SELECT COUNT(*) FROM recent_phonenumbers WHERE phonenumber=? '''

        con = create_connection()

        cur = con.cursor()
        cur.execute(sql, values)
        count = cur.fetchone()[0]

        if count > 0:
            result = True

        con.close()

    return result


def check_phonenumber_hash(md5):
    # Checks whether a phonenumber hash is known in the database
    # It returns 'True' when found; 'False' when not present

    result = False

    if re.match(r"(^[a-fA-F\d]{32}$)", md5.lower()) is not None:
        values = (md5.lower(),)
        sql = ''' SELECT COUNT(*) FROM recent_phonenumbers WHERE md5=? '''

        con = create_connection()

        cur = con.cursor()
        cur.execute(sql, values)
        count = cur.fetchone()[0]

        if count > 0:
            result = True

        con.close()

    return result

