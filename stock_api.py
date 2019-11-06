import requests
from bs4 import BeautifulSoup
#FANG Stocks FB-AAPL-NFLX-GOOGL
#All of FB data
#FB data in JSON
def fb_data():
    #url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/metadata.json?api_key=e4GhL94a1or42eyT5bTz'
    #url = 'https://www.quandl.com/api/v3/databases/YC/data?download_type=partial?api_key=e4GhL94a1or42eyT5bTz'
    url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?api_key=e4GhL94a1or42eyT5bTz'
    result = requests.get(url)
    fb_scrape = result.content
    #soup = BeautifulSoup(fb_scrape, 'html.parser')
    #print(soup.prettify())
    print(fb_scrape)
fb_data()
