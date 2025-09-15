import requests 
from bs4 import BeautifulSoup
response = requests.get('https://bbc.com')
soup = BeautifulSoup(response.content,"html.parser")
titles = soup.find_all('h2')                       
for title in titles:
  print(title.get_text()) 

import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.aljazeera.com')
soup=BeautifulSoup(response.content,"html.parser")
titles=soup.find_all('h2')
for title in titles:
   print(title.get_text())

