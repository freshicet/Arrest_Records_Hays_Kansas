
import requests
import re
from bs4 import BeautifulSoup
import sys
import geocoder
import gmplot
import csv

mainpage = 'https://www.hayspost.com/category/community/hays-police-department-arrest-log/'
page = requests.get(mainpage).content
soup = BeautifulSoup(page, "html5lib")
Main_Block = soup.find("li", {"class": "pagination-next"})
A_tag = Main_Block.find("a")
mainpage = A_tag['href']

print mainpage
