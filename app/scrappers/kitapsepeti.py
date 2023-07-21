#pip install requests
#pip install bs4
#pip install pandas
#pip install pymongo

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient


url = "https://www.kitapsepeti.com/arama?q=python&customerType=Ziyaretci&&stock=1"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

mongo_url = "mongodb://root:password@localhost:27017"
mongo_db = MongoClient(mongo_url)
db = mongo_db["smartmaple"]
collKitapsepeti = db.create_collection("kitapsepeti")

title = soup.find_all("a", attrs = {"class": "fl col-12 text-description detailLink"})
publisher = soup.find_all("a", attrs = {"class": "col col-12 text-title mt"})
writer = soup.find_all("a", attrs = {"class": "fl col-12 text-title"})
price = soup.find_all("div", attrs = {"class": {"col col-12 currentPrice"}})

bookListforKitapsepeti = list()

for i in range(len(title)):
    title[i] = (title[i].text).strip("\n").strip()
    publisher[i] = (publisher[i].text).strip("\n").strip()
    writer[i] = (writer[i].text).strip("\n").strip()
    price[i] = (price[i].text).strip("\n").strip("\nTL").replace(",",".")
    
    bookListforKitapsepeti.append([title[i], publisher[i], writer[i], price[i]])
    dfKitapsepeti = pd.DataFrame(bookListforKitapsepeti, columns = ["Title", "Publisher", "Authors", "Price"])

    
dfKitapsepeti.reset_index(inplace=True)
data_dict = dfKitapsepeti.to_dict("records")
# Insert collection
collKitapsepeti.insert_many(data_dict)

# for show data.
for x in collKitapsepeti.find({}, {"_id":0,"Title":1,"Publisher":1,"Price":1}):
    print(x)