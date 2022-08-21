import  re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=5, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# session.get(url)
from config import BASE_URL
import uuid
def insertUser(name,img):

    # biography = re.sub("([#@])\\w+", "", userData["biography"] or "")
    reqjsn = {
        "FullName":name,
        'Name': uuid.uuid1(),
        'MigratedProfileImage':img,
        'UserDescription': "News",
        "InstagramPk":name,
        "Age": 0,
        "Sex": "News agency",
        "Race": "News agency",
        "Interests": "News agency",
        "NativePlace": "India",
    }
    #sex: News agency
    # race: News agency
    # interests: News agency
    # isStatusOpen: false
    # NativePlace: India
    print(reqjsn)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    res = requests.post(BASE_URL+"/api/v1/users/instagramuser", data=reqjsn, headers=headers, verify=False)
    print('time', 'message', 'inserted users :- ' + res.text)
    return res.text
def news_insert(Headlines,images,Lat,Long,date,user_id):
    reqjsn = {
                'InLocation':True,
                'Text':Headlines ,
                'MigratedImage': images,
                'Latitude': Lat,
                'Longitude': Long,
                'BatchName': "News: Crime",
                "Hashtag1": "news",
                "Hashtag2": "crime",
                'userId': user_id,
                "Emoji":"1F4F0",
                "MigratedDate": date,
                "Hide": True,
               
            }
    print(reqjsn)
    res = requests.post(BASE_URL+"/api/v1/Comment/Insert", json=reqjsn)
    print('time', 'message',  'inserted comment :- ' + res.text)