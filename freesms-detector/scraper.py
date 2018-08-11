import requests
import re
from bs4 import BeautifulSoup

#urls = ["https://receive-a-sms.com/", "https://sms-online.co/receive-free-sms", "https://www.receive-sms-online.info/"]

url = "https://receive-a-sms.com/"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', id="maintable")
links = table.find_all('a',href=True)
for link in links:
        print(link.text)

