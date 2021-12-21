# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:51:58 2021

@author: Jumpsus
"""

import requests
from bs4 import BeautifulSoup

url = 'https://pumpmygas.xyz' #url for request data
read = requests.get(url) #request data from web inthis process you need to connect internet

soup = BeautifulSoup(read.content,'lxml')

result = [] # list that store dict that contain each platform gas fee.
for x in soup.find_all('button'):
    name = x.p.contents[0]
    gas = [] # gas consist of Sell gas fee [0] , Buy gas fee [1].
    for y in x.find_all('span'):
        if y.contents[0] == '—':
            gas.append(0)
        try:
            gas.append(float(y.contents[0]))
        except:
            continue
        if len(gas) == 2:
            print("Platform: {0} (Gas fee)".format(name)) 
            print("Sell: {0} usd".format(gas[0]))
            print("Buy: {0} usd".format(gas[1]))
            print(" ")
            result.append({"name" : name, "sell" : gas[0], "buy" : gas[1]})
