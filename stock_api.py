import requests
import csv
import urllib.request
import json
from bs4 import BeautifulSoup
#FANG Stocks FB-AAPL-NFLX-GOOGL
#All of FB data-Get recent 2019 fb data
headers = []
def fb_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?start_date=2007-11-01&end_date=2019-11-01&api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    fb_scrape = result.content
    f = open('/Users/basillatif/Desktop/Stock Data Project/fb_data.csv', "w")
    f.write(result.text)
    f.close()
def aapl_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL/data.csv?start_date=2007-11-01&end_date=2019-11-01&api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    aapl_scrape = result.content
    f = open('/Users/basillatif/Desktop/Stock Data Project/aapl_data.csv', "w")
    f.write(result.text)
    f.close()
def amzn_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/AMZN/data.csv?start_date=2007-11-01&end_date=2019-11-01&api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    amzn_scrape = result.content
    f = open('/Users/basillatif/Desktop/Stock Data Project/amzn_data.csv', "w")
    f.write(result.text)
    f.close()
def nflx_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/NFLX/data.csv?start_date=2007-11-01&end_date=2019-11-01&api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    nflx_scrape = result.content
    f = open('/Users/basillatif/Desktop/Stock Data Project/nflx_data.csv', "w")
    f.write(result.text)
    f.close()
def googl_data():
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/GOOGL/data.csv?start_date=2007-11-01&end_date=2019-11-01&api_key=e4GhL94a1or42eyT5bTz'
    headers = {"Date":"Open" , "High":"Low", "Close":"Volume", "Ex-Dividend":"Split Ratio", "Adj.":"Open,Adj.", "High,Adj.":"Low,Adj.", "Close,Adj.":"Volume"}
    result = requests.get(url, headers = headers)
    googl_scrape = result.content
    print(googl_scrape)
    f = open('/Users/basillatif/Desktop/Stock Data Project/googl_data.csv', "w")
    f.write(result.text)
    f.close()


fb_data()
aapl_data()
amzn_data()
nflx_data()
googl_data()

#for current error
#https://stackoverflow.com/questions/38855641/writing-api-results-to-csv-in-python
