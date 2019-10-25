from IPython.display import HTML
from IPython.display import Image
import numpy as np
import urllib.request
import bs4 #this is beautiful soup
import time
import operator
import socket
import _pickle as cPickle
import re # regular expressions
from pandas import Series
import pandas as pd
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")
sns.set_style("white")
#from secret import *
import requests

#OPEC data from for 6 days in March
#url = 'https://www.quandl.com/api/v3/datasets/OPEC/ORB.csv?start_date=2003-01-01&end_date=2003-03-06'
#All of APPL data
#url = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv'
#All of FB data
#url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv'
#FB data in JSON
url = 'https://www.quandl.com/api/v3/datasets/WIKI/FB/metadata.json'
result = requests.get(url)
print(result.status_code)

c = result.content
print(c)
