# This program takes in the result of a json file that is the result of
    # a Guardian API search query. It produces a spreadsheet containing the
    # following columns: the article title, the date, the url, and the full
    # text of the article

import json
import csv
import requests
from bs4 import BeautifulSoup

# load and parse the json file
query_json = open("query_result.json")
parsed_query = json.load(query_json)

# create a list containing the individual result json bits
results = parsed_query["response"]["results"]

# open the csv file so that we can write to it
with open("guardian_results.csv", "w") as file:
    # Create a writer
    writer = csv.writer(file)
    # Create a header row
    writer.writerow([
        "title",
        "date",
        "url",
        "full text"
    ])

    # iterate through each entry, adding it to the csv and fetching the
    # full text of its article.
    for result in results:
        # assign data from json to variables
        title = result["webTitle"]
        date = result["webPublicationDate"]
        date = date[:10] #trim off extra time information
        url = result["webUrl"]

        # Go and Scrape the article's text
        # set up an object to visit the page
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
        response = requests.get(url, headers=headers)
        page_soup = BeautifulSoup(response.content, features="lxml")

        # add the contents of the new article to collected
        full_text = ""

        for x in page_soup.find_all('p'):
            full_text = full_text + x.get_text() + "\n"

        # write the variables to the spreadsheet as a new row
        writer.writerow([
            title,
            date,
            url,
            full_text
        ])

print("Done Scraping!")
