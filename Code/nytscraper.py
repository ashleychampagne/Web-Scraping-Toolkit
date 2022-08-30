import requests
import csv
from bs4 import BeautifulSoup

# if your file has a different name, replace "nytlinks" with its name
with open('nytlinks.csv', 'r') as fil1:
    articles = [line.rstrip('\n') for line in fil1]

    articles_text = []

    for article in articles:
        # set up an object to visit the page
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
        response = requests.get(article, headers=headers)
        page_soup = BeautifulSoup(response.content, features="lxml")

        # add the contents of the new article to collected
        full_text = ""
        for x in page_soup.find_all('p'):
            full_text = full_text + x.get_text() + "\n"
        articles_text.append(full_text)

    with open('articlefulltext.csv', 'w') as fil2:
        # Create a writer
        writer = csv.writer(fil2)
        # Create a header row
        writer.writerow(['Date', 'Article Url', 'Article Full Text'])

        # Populate the spreadsheet
        i = 0
        for article in articles:
            # Get the date from the url
            date = article[24:34]

            writer.writerow([date, article, articles_text[i]])
            i = i + 1

print("Done Scraping!")
