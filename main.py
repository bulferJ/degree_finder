# This is a small sample of code, although there is more, this software is in it's very early stages of planning.

from bs4 import BeautifulSoup #BS4 is a Python library which is used for simple web scraping tasks

from bs4 import BeautifulSoup
import random, requests, re #Random is used for the following user-agent list, requests is used to request the URL 

# Organizations usually don't like web crawlers, scrapers or bots on their website, so they often have filters. This is a dummy list of user agents 
# A user agent on a website is a string of characters that identifies the software or device used to access the website.
# This list represents various UAs which are chosen from at random, this bypasses the website's filter and bot detecting features.

ua_list = ['Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
    ,'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36']

HEADERS = {
    'user-agent' : random.choice(ua_list),  # The UA is included in the header of an HTTP request sent to the web server
    'Accept-Language': 'en-US, en;q=0.5'
}

# this is the sample URL of the 118 "entities" (defined in readme) aka the 118 webpages describing the various degrees, certiicates and minors awarded at DSU
url = "https://catalog.dsu.edu/preview_program.php?catoid=35&poid=2677&returnto=1625"  

page = requests.get(url, headers = HEADERS) # using the Python library Request we send an HTTP request using the UA

def page_status():
    if page.status_code != 200:
        print('\nFail to retrieve page.\n')   # This simply lets you know if the request was succesful or not in the terminal, the method above has never failed me
    else:
        print('\nRetrieved page succesfully.\n')

soup = BeautifulSoup(page.content, "lxml")  
# The "soup" is the entire HTML code of the website, lxml (not xml) a Python library for parsing and processing XML and HTML documents

# The class "acalog-coure" contains 3 bits of data: class_name, class_credits, and class_code which we will use re and regex to seperate these values into strings
tag = soup.find_all(class_ = 'acalog-course')
text = tag[1].span.text # there are 4-45 ish of these elements spread across the 118 webpages, we extract the first one, find the span, then the text 

credits_match = re.search(r"(\d+)\s*credits", text) # the following lines of code use re to seperate parts of the string and match those values
class_credits = credits_match.group(1)


name_match = re.search(r"^(.*?)(\d+\s*credits)", text)
name = name_match.group(1)
stripped_name = name.replace(" ", "") # remove the spaces in the string

code_match = re.match(r"^(.+?)-(.+)$", stripped_name )
class_code = code_match.group(1)

class_name_match = code_match.group(1)
class_name = re.sub(r"([a-z])([A-Z])", r"\1 \2", code_match.group(2))

page_status() # first print statement in the terminal which lets you know if the web request was succesful

print(soup.h1.text) # the first header in each of these webpages is the title of the entity, such as "Mathematics Education B.A"

print("\n"+ class_code)   # prints the data onto the terminal with new lines to format properly
print(class_name)
print(class_credits+" credits" "\n")






# Sample code from another webscraping project that I was using which extracted product data from a supplement website and created an excel file with that data.

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
