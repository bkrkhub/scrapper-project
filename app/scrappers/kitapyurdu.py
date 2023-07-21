#pip install requests
#pip install bs4
#pip install pandas
#pip install pymongo

from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import pandas as pd

mongo_url = "mongodb://root:password@localhost:27017"
mongo_db = MongoClient(mongo_url)
db = mongo_db["smartmaple"]
collKitapyurdu = db.create_collection("kitapyurdu")


url = "https://www.kitapyurdu.com/index.php?route=product/search&filter_name=python&filter_in_stock=1&fuzzy=0&limit=100"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
title = soup.find_all("div", attrs = {"class":"name"})
publisher = soup.find_all("div", attrs = {"class": "publisher"})
writer = soup.find_all("div", attrs = {"class": "author compact ellipsis"})
oldPrice = soup.find_all("div", attrs = {"class": "price-old price-passive"})
kitapyurduPrice = soup.find_all("div", attrs = {"class": "price-new"})

bookListforKitapyurdu = list()

for i in range(len(title)):
    title[i] = (title[i].text).strip("\n").strip()
    publisher[i] = (publisher[i].text).strip("\n").strip()
    writer[i] = (writer[i].text).strip("\n").strip()    
    oldPrice[i] = (oldPrice[i].text).strip("\n").strip("Üretici Liste Fiyatı:").replace(",",".")
    kitapyurduPrice[i] = (kitapyurduPrice[i].text).strip("\n").strip("Kitapyurdu Fiyatı:").replace(",",".")
    
    bookListforKitapyurdu.append([title[i], publisher[i], writer[i], oldPrice[i], kitapyurduPrice[i]])
    dfKitapyurdu = pd.DataFrame(bookListforKitapyurdu, columns = ["Titles", "Publishers","Authors","Manufacturer Price","Kitapyurdu Price"])
    

dfKitapyurdu.reset_index(inplace=True)
data_dict = dfKitapyurdu.to_dict("records")
# Insert collection
collKitapyurdu.insert_many(data_dict)

print(collKitapyurdu)

# for show data.
for x in collKitapyurdu.find({}, {"_id":0,"Titles":1,"Publishers":1,"Manufacturer Price":1,"Kitapyurdu Price":1}):
    print(x)