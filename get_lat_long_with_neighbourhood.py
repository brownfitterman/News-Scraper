from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from geopy.geocoders import Nominatim
url=input("Enter the url here :-  ")
driver=webdriver.Chrome("chromedriver.exe")
driver.get(url)
all_links=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/ul/li')
names=[]
url=[]
for i in all_links:
    names.append(i.text)
latitudes=[]
longitudes=[]
for i in names:
    try:
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode( f'{i} Hyderabad ')
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
        print(location.latitude , location.longitude ) 
        print("found")
    except:
        print(" not found")
        latitudes.append("")
        longitudes.append("")
df=pd.DataFrame({
    "Name":names,
    "lat":latitudes,
    "lang":longitudes
})

df.to_csv("locations.csv")






