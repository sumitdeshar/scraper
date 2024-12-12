from bs4 import BeautifulSoup  # type: ignore
import requests  # type: ignore
import csv

url = 'https://quotes.toscrape.com/'
page_to_scrape = requests.get(url)

soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags_collection = []

for quote in quotes:
    tags = quote.find_next('div', attrs={'class': "tags"})
    tags_collection.append(list(tags.strings))
        # tags_collection.append([tag.strip() for tag in tags.text.split('\n') if tag.strip()])

def collection_tags(tags: list):
    res_list = []
    if tags:
        for tag_list in tags:
            temp_list = []
            for item in tag_list:
                formatting_item = item.strip().replace(':','').lower()
                if formatting_item not in ['tags', 'tag', '\n']:
                    if formatting_item: 
                        temp_list.append(item.strip())
            res_list.append(temp_list)
    return res_list


# print('input', tags_collection) 
# print('result',collection_tags(tags_collection))

refined_tags = collection_tags(tags_collection)

file = open('scraped_quotes.csv', 'w')
writer = csv.writer(file)

writer.writerow(['Quotes', 'Authors', 'Tags'])

for quote,author,tag in zip(quotes,authors,refined_tags):
    # print(f'{quote.string} by {author.string}')
    writer.writerow([quote.string,author.string,tag])

print('written')    
file.close()
