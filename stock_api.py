import requests
import csv
import urllib.request
import json

from bs4 import BeautifulSoup
#FANG Stocks FB-AAPL-NFLX-GOOGL
#All of FB data
#FB data in JSON
headers = []
def fb_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    fb_scrape = result.content
    f = open('/Users/basillatif/Desktop/Stock Data Scrape/fb_data.csv', "w")
    f.write(result.text)
    f.close()
    # with open('fb_data.csv', mode='w') as fb_scrape:
    #     fb_writer = csv.writer(fb_scrape, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     fb_writer.writerow(['Date', 'Open', 'High'])
    print(fb_scrape)
fb_data()

#for current error
#https://stackoverflow.com/questions/38855641/writing-api-results-to-csv-in-python
