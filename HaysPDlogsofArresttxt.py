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
text_file = open("Output.txt", "w")

n = 0
la = []
ln = []
mainpage = 'https://www.hayspost.com/category/community/hays-police-department-arrest-log/'


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
                    x = g.housenumber + ' ' + g.street_long + ' ' + 'Hays,ks'
                    age = re.findall(r', (.*?),', st)
                    city_Person = re.findall(r', (.*?), was arrested at', st)
                    city_Person = city_Person[0]
                    city_Person = city_Person[4:]
                    Time = re.findall(r'was arrested at (.*?) in the', st)
                    arrested_log = re.findall(r'suspicion of (.*?)\.', st)
                    Name = re.findall(r'(.*?),', st)
                    text_file.write('%r{%r}\n' % (x.encode("utf-8"), arrested_log[0].encode("utf-8")))
                    # text_file.write(/n)
                    # text_file.close()
                    # break
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

# f.close()
# gmap.scatter(la, ln, '#3B0B39', size=40, marker=False)
# gmap.draw("mymap.html")
