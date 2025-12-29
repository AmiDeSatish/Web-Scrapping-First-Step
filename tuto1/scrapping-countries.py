import requests
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"

# Google Chrome User Agents : 
# - Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
# - Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
# - Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36

user_agents1 = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
]

headers1 = {"User-Agent" :  random.choice(user_agents1)}

# ==== fake_useragent solution ==== :
ua = UserAgent()
headers2 = {"User-Agent" : ua.random}

# ==== Envoi de la requete ==== : 
response = requests.get(URL, headers=headers2)
status = response.status_code

# ==== Création du .html en local
with open('scrapethiswebsite.html',"wb") as f:
  f.write(response.content)

# ==== Utilisation de beautifulsoup, qui deande un string ====
html = response.text
soup = BeautifulSoup(html,"html5lib")

title = soup.find("title")
all_pays = soup.find_all("h3", class_ = "country-name")
for pays in all_pays :
  print("PAYS", pays.text.strip())


print("TITLE :", title.text)
#print(html)