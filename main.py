from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

my_url = 'https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DSamsung'
uClient = uReq(my_url) #opening the connection and grabbing the page
page_html = uClient.read() #Store the whole raw html file in page_html
uClient.close()

##html parsing
page_soup = soup(page_html,"html.parser")

a = page_soup.findAll("div",{"class":"_1UoZlX"}) ##grabs all the mobile divs

f = open('phone_list.csv','w',encoding="utf-8")
fu = csv.writer(f)

fu.writerow(["TITLE","PRICE","RATING"])

#iterating through all elemennts
for i in a:
    title = i.find("div",{"class":"_3wU53n"}).text ##get the title elements
    #print(title)
    rating = i.find("div",{"class":"hGSR34"}).text
    #print(rating)
    price = i.find("div",{"class":"_1vC4OE _2rQ-NK"}).text[1:]
    print(price)

    fu.writerow([title,price,rating])

f.close()
