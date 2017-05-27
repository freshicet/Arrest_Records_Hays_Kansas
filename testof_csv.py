#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('testof_csv.csv', 'wb')
writer = csv.writer(f)
writer.writerow(('Latitude', 'Longitude', 'Time',
                 'arrested', 'Age', 'Here there are from'))
writer.writerow(('g.latlng[1]', 'g.latlng[1]', 'Time[0]', 'arrested_log[0]', 'age[0]', 'city_Person'))

f.close()
# gmap.scatter(la, ln, '#3B0B39', size=40, marker=False)
# # gmap.draw("mymap.html")
