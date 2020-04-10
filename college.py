
import pandas as pd

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
h = str(input("enter country of your choice "))
url = "https://www.worldometers.info/coronavirus/country/"+h
url2 = "https://www.worldometers.info/coronavirus/country/"+h+"/#coronavirus-deaths-linear"
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_= "maincounter-number")
print("Total cases : ",data[0].text.strip())
print("Total Deaths : ",data[1].text.strip())
print("Total recovered : ",data[2].text.strip())
g = requests.get(url2)
j = BeautifulSoup(g.text,"html.parser")

