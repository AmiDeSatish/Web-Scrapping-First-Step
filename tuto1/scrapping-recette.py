import requests
from bs4 import BeautifulSoup

URL = "https://codeavecjonathan.com/scraping/recette/"

def isElementFound(e) :
  if e:
    return e.text.strip()
  return None


response = requests.get(URL)
bytes = response.content
#response.encoding = "UTF-8"

if response.status_code == 200 :
  html = response.text

  f = open("recette.html", "w")
  f.write(html)
  f.close()

  soup = BeautifulSoup(html,"html5lib")
  
  title = soup.find("h1").text
  #print(title)

  description = isElementFound(soup.find("p",class_ = "description"))
  #print(description)

  # Ingrédients :
  div_ingredients = soup.find("div",class_ = "ingredients")
  e_ingredients = div_ingredients.find_all("p")
  for e_ingredient in e_ingredients :
    print("INGREDIENT",isElementFound(e_ingredient))

  # Etapes :
  table = soup.find("table", class_ = "preparation")
  etapes = table.find_all("td", class_ = "preparation_etape")
  for etape in etapes : 
    print("ETAPE",etape.text)

else : 
  print("Erreur ", response.status_code)