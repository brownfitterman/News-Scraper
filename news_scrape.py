import json
from unicodedata import name
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from geopy.geocoders import Nominatim 
from selenium.webdriver.common.by import By
from functions import insertUser, news_insert
names=[]
images=[]
date=[]
urls=[]
Headlines=[]
News_user_img=[]
News_user=[]
Latitude=[]
Longitude=[]

def get_neighborhood(url):
    driver=webdriver.Chrome("chromedriver.exe")
    url=url
    driver.get(url)
    all_links=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/ul/li')

    for a in all_links:
        names.append(a.text) 
###########################################################################################

def get_news_and_details(city,tag):
    driver=webdriver.Chrome("chromedriver.exe")
    driver.get(f'https://news.google.com/search?q={city}%20{tag}&hl=en-IN&gl=IN&ceid=IN%3Aen&v2prv=1')
    data=driver.find_elements(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div')
    no=0                              #'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[8]/div/article/h3/a
    for i in data:
        print(no)
        try:
            images.append(i.find_element(By.XPATH,'a/figure/img').get_attribute('src'))
            # print("post image =="+images)
        except:
            images.append("http://www.middleweb.com/wp-content/uploads/2017/08/breaking-news-blue-600.jpg")
        try:
            url=i.find_element(By.XPATH,'div/article/a').get_attribute('href')
            urls.append(i.find_element(By.XPATH,'div/article/a').get_attribute('href'))
            print("post_url=="+i.find_element(By.XPATH,'div/article/a').get_attribute('href'))
        except:
            url=""
            urls.append("")
        try:
            date.append(i.find_element(By.XPATH,'div[1]/article[1]/div/div/time').get_attribute('datetime'))
            # print("date -- "+date)
        except:
            date.append("")
        try:
            Headlines.append(i.find_element(By.XPATH,'div/article/h3/a').text +" "+url )
        except:
            Headlines.append("")
        # print("headline== "+Headlines)
        try:
            News_user_img.append(i.find_element(By.XPATH,'div/article/div/img').get_attribute('src'))
            # print("news_image-- " +News_user_img)
        except:
            News_user_img.append("")
        try:
            News_user.append(i.find_element(By.XPATH,'div/article/div/img').get_attribute('alt'))
        except:
            News_user.append("")
        no+=1
    print(Headlines)
    for u in urls:
        try:
            print(u)
            driver.get(u)
            time.sleep(3)
            list=driver.find_element(By.XPATH,'html/body').text
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(f"city")
            Lat=location.latitude
            Long=location.longitude
            print(" searching neighborhood in article")
            for i in names:
                if i in list:
                    print("done")
                    try:
                        geolocator = Nominatim(user_agent="MyApp")
                        location = geolocator.geocode(f"{i} {city}")
                        Lat=location.latitude
                        Long=location.longitude
                    except:
                        pass
            Latitude.append(Lat)
            Longitude.append(Long)
        except Exception as err:
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(f"Hyderabad")
            Lat=location.latitude
            Long=location.longitude
            Latitude.append(Lat)
            Longitude.append(Long)
            print(err)
            pass
user_lists=[]
user_dict={}
try:
    main_list=open("user_list.txt","r").read()
    user_dict=open("user_dict.json","r").read().replace("'",'"')
    # print(user_dict)
    user_dict=json.loads(user_dict)
except:
    main_list=[]
def main(wiki_url,city,tag):
    get_neighborhood(wiki_url)           
    get_news_and_details(city,tag)      
    print(len(images))
    row=0
    for r in range(100):
        if News_user[row] in main_list:
            f=user_dict[News_user[row]]
            user_lists.append(News_user[row])
            print(" user already inserted")
        else:
            f=insertUser(News_user[row],News_user_img[row])
            user_lists.append(News_user[row])
            user_dict[News_user[row]]=f
        news_insert(Headlines[row],images[row],Latitude[row],Longitude[row],date[row],f)
        row+=1
    f1= open("user_list.txt","w")
    f1.write(str(user_lists))
    f2= open("user_dict.json","w")
    f2.write(str(user_dict))








