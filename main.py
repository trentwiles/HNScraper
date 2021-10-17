from bs4 import BeautifulSoup
import requests
import random
import json
import time

links = []

id = random.randrange(10000,10000000)

headers = {"User-agent": "Riverside Rocks (+https://riverside.rocks/projects/"}

pages = 6

for x in range(pages):

    r = requests.get('https://news.ycombinator.com/news?p=' + str(x), headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.find_all('a'):
        if link.get('href').startswith("https") and link.get('href') != "https://github.com/HackerNews/API" and link.get('href') != "https://news.ycombinator.com/news":
            links.append(link.get('href'))

f = open("top-" + str(id) + ".json", "w")
f.write(json.dumps(links))
f.close()

print("Link scrape done, going to scan each link...")
time.sleep(1)

content = []

size = len(links)

part = 0

for l in links:
    part = part + 1
    r = requests.get(l, headers=headers)
    resp = r.text
    percen = part/size
    percent = round(percen*100)
    content.append(resp)
    print("[" + str(percent) + "%] Scanned " + l + " (site returned HTTP " + str(r.status_code) + ")")

f = open("top-" + str(id) + "-html.json", "w")
f.write(json.dumps(content))
f.close()

ljson = "top-" + str(id) + ".json"
htmljson = "top-" + str(id) + "-html.json"

print("\n ======= OVERVIEW =======")
print("\n Scanned " + str(size) + " links from " + str(pages) + " HN pages.")
print("\n Saved links to '"+ ljson + "' and HTML to '" + htmljson + "'")
