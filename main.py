''' Watch: https://www.youtube.com/watch?v=_AeudsbKYG8 for more context '''

# Import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# This is used to get urls
driver = webdriver.Chrome()

# Create the url with the given search term
def get_url(search_term):
    """Generate a url from search term"""
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

# Search the url with a given search term
url = get_url('intel cpu')
driver.get(url)

# Use BS4 to scrape the data of each item from the the search results
soup = BeautifulSoup(driver.page_source, 'html.parser')
responses = soup.find_all('div', {'data-component-type': 's-search-result'})

print(len(responses))

for item in responses:
    # Item name
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://hwww.amazon.com' + atag.get('href')

    # Item Price
    price_parent = item.find('span', 'a-price')
    price = price_parent.find('span', 'a-offscreen').text
    print(description + " : " + price)