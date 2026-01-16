import requests
from bs4 import BeautifulSoup
a = requests.get("https://www.google.com/")
print(a.text)
url = "https://www.google.com/"
r=requests.get("https://www.google.com/")
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())