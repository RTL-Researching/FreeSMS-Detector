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

number_query = "441823711087"

#print(number_query)

for i in phonenumbers:
    print(i['phonenumber'])
    if number_query in i['phonenumber']:
        print("yes")
    else:
        print("no")