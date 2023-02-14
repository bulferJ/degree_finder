from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
import random, requests, re

ua_list = ['Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    ,'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36']

HEADERS = {
    'user-agent' : random.choice(ua_list),
    'Accept-Language': 'en-US, en;q=0.5'
}


url = "https://catalog.dsu.edu/preview_program.php?catoid=35&poid=2677&returnto=1625"

page = requests.get(url, headers = HEADERS)

def page_status():
    if page.status_code != 200:
        print('\nFail to retrieve page.\n')
    else:
        print('\nRetrieved page succesfully.\n')

soup = BeautifulSoup(page.content, "lxml")

tag = soup.find_all(class_ = 'acalog-course')
text = tag[1].span.text 

credits_match = re.search(r"(\d+)\s*credits", text)
credits = credits_match.group(1)


name_match = re.search(r"^(.*?)(\d+\s*credits)", text)
name = name_match.group(1)
stripped_name = name.replace(" ", "")

code_match = re.match(r"^(.+?)-(.+)$", stripped_name )
code = code_match.group(1)

title_match = code_match.group(1)
title = re.sub(r"([a-z])([A-Z])", r"\1 \2", code_match.group(2))

page_status()
print("\n"+ code)
print(title)
print(credits+" credits" "\n")
# print(credits)







    # for x in card:
    #     if "Sold Out" not in x.div.text:
    #         title = (x.h3.text)
    #         type = (x.span.text)
    #         price = (x.div.text.strip())
    #         info = (title,type,price)
    #         writer.writerow(info)
# with open('gorrillamind.csv','w', encoding = 'utf-8', newline = '') as f:
#     writer = csv.writer(f)
#     header = ['Product Name','Type','Price']
#     writer.writerow(header)
