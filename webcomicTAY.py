#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import sys
import geocoder
import gmplot
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('test5.csv', 'wb')
writer = csv.writer(f)
writer.writerow(('Latitude', 'Longitude', 'Time',
                 'arrested', 'Age', 'Here there are from', 'Name'))
n = 0
la = []
ln = []
mainpage = 'https://www.hayspost.com/category/community/hays-police-department-arrest-log/'
gmap = gmplot.GoogleMapPlotter(38.88029, -99.320974, 14)


for nextpages in mainpage:
    page = requests.get(mainpage).content
    soup = BeautifulSoup(page, "html5lib")
    MainBlock = soup.find_all("header", {"class": "entry-header"})
    for x in MainBlock:
        Atag = x.find("a")
        URL = Atag['href']
        print Atag.string
        page = requests.get(URL).content
        soup = BeautifulSoup(page, "html5lib")
        MainBlock = soup.find("div", {"class": "entry-content"})
        Atag = MainBlock.find_all("p")
        for x in Atag:
            st = x.string
            try:
                location = re.findall(r'in the(.*?) on ', st)
                print location
                try:
                    g = geocoder.google(location[n] + 'hays,ks')
                    age = re.findall(r', (.*?),', st)
                    city_Person = re.findall(r', (.*?), was arrested at', st)
                    city_Person = city_Person[0]
                    city_Person = city_Person[4:]
                    Time = re.findall(r'was arrested at (.*?) in the', st)
                    arrested_log = re.findall(r'suspicion of (.*?)\.', st)
                    Name = re.findall(r'(.*?),', st)
                    print Name
                    print g.latlng
                    la.append(g.latlng[0])
                    ln.append(g.latlng[1])
                    writer.writerow((g.latlng[0], g.latlng[1], Time[
                                    0], arrested_log[0], age[0], city_Person, Name[0]))
                except IndexError:
                    continue
            except TypeError:
                continue
    page = requests.get(mainpage).content
    soup = BeautifulSoup(page, "html5lib")
    Main_Block = soup.find("li", {"class": "pagination-next"})
    try:
        A_tag = Main_Block.find("a")
        mainpage = A_tag['href']
    except AttributeError:
        break

f.close()
gmap.scatter(la, ln, '#3B0B39', size=40, marker=False)
gmap.draw("mymap.html")
