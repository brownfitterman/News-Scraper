import json
# from unicodedata import name
from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from geopy.geocoders import Nominatim 
from selenium.webdriver.common.by import By
from tkinter import *
from news_scrape import main
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="MyApp")

window = Tk()
wiki_url=Variable()



def get_neighborhood():

    driver=webdriver.Chrome("chromedriver")
    url=wiki_url.get()
    driver.get(url)
    # try:
    #     all_links=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/ul/li')
    # except:
    name=[]
    Latitude=[]
    Longitude=[]
    all_links=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/ul/li')
    for a in all_links:
        name.append(a.text) 
    if len(name)<30:
        name=[]
        print("in")
        all_links=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr')
        for a in all_links:
            name.append(a.text)
    for n in name:
        try:
            location = geolocator.geocode(n)
            print("latitude = " +location.latitude)
            print("longitude = " + location.longitude)
            Latitude.append(location.latitude)
            Longitude.append(location.longitude)
        except:
            Latitude.append("")
            Longitude.append("")
    df= pd.DataFrame({
        "Name":name,
        "Latitude":Latitude,
        "Longitude":Longitude
    })
    city=wiki_url.get().split("/")[-1]
    df.to_csv(f"{city}.csv")
         



window.title("News Scrapper")
window.geometry('350x200')
lbl = Label(window, text="Put wikipedia url", font=("Arial Bold", 10))
lbl.grid(column=0, row=1, padx=10,pady=10)
entry1=Entry(window, textvariable=wiki_url).grid(column=1, row=1, padx=10,pady=10)

btn = Button(window, text="Get Csv", command=get_neighborhood)
btn.grid(column=1, row=2)


window.mainloop()
