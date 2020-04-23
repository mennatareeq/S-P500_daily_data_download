# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:13:52 2018

@author: Menna
"""

import urllib 
import datetime

infile = open("Path.txt", 'r')
firstLine = infile.readline()

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")

url = 'https://us.spindices.com/documents/additional-material/sp-500-eps-est.xlsx'  
urllib.urlretrieve(url, firstLine + '/sp-500-eps-est-' + date + '.xlsx') 

print(firstLine)
input("press close to exit") 

