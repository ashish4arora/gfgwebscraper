import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.geeksforgeeks.org/dynamic-programming"
page = requests.get(URL)
soup = BeautifulSoup(page.content , "html.parser")
easy = soup.find_all("div", class_ = "basicProblems")
medium = soup.find_all("div", class_ = "mediumProblems")
hard = soup.find_all("div", class_ = "hardProblems")
easy, medium, hard = easy[0], medium[0], hard[0]

easylist = easy.find_all("a")
mediumlist = medium.find_all("a")
hardlist = hard.find_all("a")
easyprobs = []
mediumprobs = []
hardprobs = []
c = 1
for e in easylist:
    title = e.text
    link = e['href']
    x = [c, title, "", "Easy",  link]
    easyprobs.append(x)
    c += 1
for e in mediumlist:
    title = e.text
    link = e['href']
    x = [c, title, "", "Medium" , link]
    mediumprobs.append(x)
    c += 1
for e in hardlist:
    title = e.text
    link = e['href']
    x = [c, title, "", "Hard" , link]
    hardprobs.append(x)
    c += 1

header = ["S.No" , "Problem", "Status", "Diffculty" , "Link"]

with open("dpques" , 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(easyprobs)
    writer.writerow(["","","","",""])
    writer.writerows(mediumprobs)
    writer.writerow(["","","","",""])
    writer.writerows(hardprobs)
    
