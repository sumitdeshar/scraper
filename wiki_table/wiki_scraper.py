from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page_to_scrape = requests.get(url)
print(page_to_scrape)

soup = BeautifulSoup(page_to_scrape.text, features='html.parser')
tables = soup.find('table', attrs={'class': 'wikitable sortable jquery-tablesorter'})

print(tables)