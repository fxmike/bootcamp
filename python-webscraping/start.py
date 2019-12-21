from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.find_all("div", {"class" : "item-container"}) #szeroka klasa
container = containers[0]

filename = 'products.csv'
f = open(filename, 'w')
headers = 'brand, product_name, shipping\n'
f.write(headers)

for container in containers:
    item_branding = container.find('div', {'class' : 'item-branding'})
    brand = item_branding.a.img['title']
    print('Brand:', brand )

    title_container = container.findAll("a", {'class': 'item-title'})
    product_name = title_container[0].text
    print('Product name:', product_name)

    shipping_container = container.findAll("li", {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()
    print('Shipping:', shipping)

    f.write(brand + "," + product_name.replace(',', '|') + ',' + shipping + '\n')

f.close()

#to jest niesamowite!!!!
