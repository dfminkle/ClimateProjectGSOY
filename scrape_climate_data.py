# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script designed to scrape and download multiple csv files from a directory-like website.
"""

# %% Import packages and explore with soup
from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests

climate_data = "https://www.ncei.noaa.gov/data/global-summary-of-the-year/access/"
page = urllib2.urlopen(climate_data)
soup = BeautifulSoup(page)

# for link in soup.find_all('a'):
#     print(link.get('href'))


# print(soup)


# %% Download using wget and beautiful soup

import wget
from time import sleep
from datetime import datetime

link_list = [link.get('href') for link in soup.find_all('a') if link.get('href').find('.csv') != -1]
main_url = "https://www.ncei.noaa.gov/data/global-summary-of-the-year/access/"
index = 23112

for x in range(0,4):
    for link in link_list[index:]:
        try:
            url = main_url+link
            local_file = link
            #wget.download(url, local_file) # This code snippet kept timing out
            urllib2.urlretrieve(url, local_file)
            index += 1
            sleep(0.1)
            print('current time =', datetime.now().strftime("%H:%M:%S"))
        except:
            print(f'encountered an error, but soldiering on. Iteation {x} of 4')
            sleep(60)
            print('done sleeping')
            continue
#Yay this works

# %% Stuff that didn't work

# %% Script to get CSVS

# for link in soup.select(soup):
#     href = link.get('href')
#     if not any(href.endswith(x) for x in ['.csv', '.fileformatetcetc']):
#         continue
    
# # %% Try to download 

# url = "https://www.ncei.noaa.gov/data/global-summary-of-the-year/access/AJ000037907.csv"
# print(requests.get(url).text)
