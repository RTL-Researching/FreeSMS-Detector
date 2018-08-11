import requests
from bs4 import BeautifulSoup
from runner import insert_phonenumber

#urls = ["https://receive-a-sms.com/", "https://sms-online.co/receive-free-sms", "https://www.receive-sms-online.info/"]


def scrape_site1():
    url = "https://receive-a-sms.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id="maintable")
    links = table.find_all('a', href=True)
    for link in links:
        print(link.text)
        insert_phonenumber(link.text, url)


def scrape_site2():
    url = "https://sms-online.co/receive-free-sms"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    numbers = soup.select('h4.number-boxes-item-number')
    for number in numbers:
        print(number.text)
        insert_phonenumber(number.text, url)


def main():
    print("Scraping some sites")
    print("scraping site 1")
    scrape_site1()
    print("scraping site 2")
    scrape_site2()

main()