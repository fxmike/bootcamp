from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://risk.ostc.com/Members/Calendar.aspx"

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
rend_table = page_soup.findAll("table", {"class" : "dxscRendererTable dxscClientRendering dxscWeekView dxsc-adaptivity-desktop"}) #szeroka klasa
print(rend_table)



