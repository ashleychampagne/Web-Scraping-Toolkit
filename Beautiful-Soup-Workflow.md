# Beautiful Soup Workflow
_This workflow will help you use beautiful soup in Python to put together useful data sets. Beautiful Soup is very open ended and much less user friendly than other tools in this toolkit; Beautiful Soup makes programmatic webscraping easier where as many other tools will do it for you. Unless you are quite comfortable with Python you should check for a more specific tool before you start using Beautiful Soup._
_This workflow will cover some of the basics of Beautiful Soup by working through the example of scraping data from http://example.webscraping.com/. This workflow will not be comprehensive by any means, but the goal is to cover enough to get you through a simple data collection project or to get you started with a larger project. It will assume some very basic Python programing knowledge such as how for loops and if statements work. To an extend, code in this workflow will sacrifice programming style to be as readible as possible for people with minimal Python experience._
_Last updated May 2020_
***
### Set up:
* The first step is to install some dependencies for Beautiful Soup. First make sure that you have Python 3 on your machine. Then, open a new terminal and type the commands:
    ~~~
    pip install requests
    pip install bs4
    pip install lxml
    ~~~
    If you get a _permission denied_ error preface each command with the word "sudo". This will prompt you to enter your password to install dependencies.
* Now, open a new document in a text editor of your choice. You should save the file as a Python document by using the extension ".py". I will refer to my document as "scraping.py."
* Include the folling at the begining of your document:
    ~~~
    import requests
    from bs4 import BeautifulSoup
    ~~~
### Using Beautiful Soup
#### 1. Compiling a list of URLs
Often, you will want to scrape data from a number of pages which are all linked to from a homepage. The first step is to scrape a list of links from the home page.
* Here is a screenshot of the homepage we are scraping for reference
    ![homepage](/Images/BeautifulSoup/homepage.png)
* Create the soup: The first step to any application of beautiful soup is to create a beautiful soup object.
    ~~~
    # Define the homepage url
    homepage_url = "http://example.webscraping.com"
    # Download the homepage
    homepage = requests.get(homepage_url)
    # Create a Beautiful Soup object 
    homepage_soup = BeautifulSoup(homepage.content, features="lxml")
    ~~~
* You can print the beautiful soup object and view the homepage's html by adding the line
    ~~~
    print(homepage_soup.prettify())
    ~~~
* Collect the links from the beautiful soup object. Note that links are "anchor tags" in HTML and are accordingly referenced by 'a'. 
    ~~~
    # Create a list of urls linked to from the homepage
    links = homepage_soup.find_all('a')
    ~~~

* To check your work so far you can instruct Python to print your list of urls by  adding the following loop.
    ~~~
    for link in links:
        # print just the url that the link links to
        print link.get('href')
    ~~~
    ![urls](/Images/BeautifulSoup/urls.png)
* Looking at the urls we have gathered we can make some observations. First of all, notice that each url we printed was just a subdirectory with no domain. We can remedy this by simply adding the domain (the homepage url) back to each url. Next, we notice that the first five urls (homepage, register, login, index, and search) are to pages we don't care about. The final link is to the next page of countries. The only urls we actually want to save are those which include "/places/default/view/". This step will look different for each project, because you will need to sort your urls in a way that is specific to the data you are looking for. For this website, we can simply sort for urls which contain "/places/default/view/". 
* We also need a loop which will search each "next" page until such a page does not exist. 
* Now that we are planning to scrape data from a website programatically there is one more important consideration. Some websites impose rate limits: a maximum request per second rate. If you go to http://example.webscraping.com/robots.txt you will find "Crawl-delay: 5" meaning that the site expects you to wait 5 seconds between requests. In fact, this website will block your IP address for about a minute to teach you a lesson if you exceed the maxiumum rate. To avoid this, we need to incorperate a delay in our loop. We will use Python's time.sleep() which delays the program for a given number of seconds.
* Let's start over with our code putting together everthing we have learned. This code should take some time to run because of the delay. It should print out a full list of page urls which are ready to be scraped.
    ~~~
    # Install dependencies 
    import requests
    from bs4 import BeautifulSoup
    import time
    
    # Define the homepage url 
    homepage_url = 'http://example.webscraping.com' 
    
    # Create a list of country page urls to build
    page_urls = []
    
    # Create a variable to store the url of the page we are searching
    url_to_search = homepage_url
    
    # Create a veriable to track whether a next link exists
    exists_next = True 
    
    # Run this loop until there is no "next" link
    while exists_next:
    	exists_next = False 
    	# pause for 5 seconds every time the loop repeats 
    	time.sleep(5)
    
    	# Download the page we are searching 
    	page_to_search = requests.get(url_to_search) 
    	# Create a Beautiful Soup object 
    	soup_to_search = BeautifulSoup(page_to_search.content, features="lxml")
    	# Get all the links which are linked to from the page we are searching
    	links = soup_to_search.find_all('a')
    
    	# Go through the links we have found
    	for link in links:
    
    		# add the homepage url to the subdirectory of the link
    		link_url = homepage_url + link.get('href')
    
    		# if the url is a page with data add it to our list
    		if 'places/default/view' in link_url:
    			page_urls.append(link_url)
    		# Otherwise, if this has text and that text includes 'Next', set url_to_search accordingly
    		elif link.string and 'Next' in link.text:
    			url_to_search = link_url
    			exists_next = True
    
    #Print each page url
    for page_url in page_urls:
    	print page_url
    ~~~
#### 2. Scraping data from each page
Now we want to scrape data from each page in page_urls. This process will look similar to the way we scraped the index pages. 
* Looking at the website we are scraping, we see that there are several data points for each country. Let's get the area and population of each country. We start by printing the html of a specific page so we know what we're looking for. We can do so with the code: 
    ~~~
    # define an example url
    afghanistan_url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
    # load page
    afghanistan_page = requests.get(afghanistan_url)
    # create soup
    soup = BeautifulSoup(afghanistan_page.content, features='lxml')
    # format and print html
    print soup.prettify()
    ~~~
    A portion of the resulting html found by searching for "population":
    ![html](/Images/BeautifulSoup/html.png)
* HTML is made up of tags which surround data. A tag generally opens with "<some_tag>" and closes with "</some_tag>." There is a lot more to know about HTML, but that is not in the scope of this workflow. As in most cases, the first thing we want to do is notice what kind of tags the data we're interested in is in. Looking at the above HTML we see that area is stored in a td tag (table data) of the class "w2p_fc" within a tr tag (table row) with the id "places_area__row". With beautiful soup, we can use the information about what kind of tag data is stored in to get that data. Let's start by getting the data about Afghanistan as an example.
    ~~~
    # for each tr tag
    for row in soup.find_all('tr'):
    	# for each data entry in that row
    	for entry in row.find_all('td'):
    		# check for the class of intrest
    		if (entry['class'][0] == 'w2p_fw'):
    			# print data if it is what we are looking for
    			if row['id'] == 'places_area__row':
    				print 'Area:'
    				print entry.text
    			elif row['id'] == 'places_population__row':
    				print 'Population:'
    				print entry.text
    			elif row['id'] == 'places_country__row':
    				print 'Country:'
    				print entry.text    
    ~~~
    This code prints out the data for Afghanistan: 
    ![Afghanistan](/Images/BeautifulSoup/Afghanistan.png)
* The next step would be to simply repeat this code in a loop as to scrape data for each country. However, printing data to the consol is not very useful. We will hold off on scraping ever country until we know how to store the data in a spreadsheet.

#### 3. Storing the data in a .csv file
Finally, we want to use a loop to scrape data from every page we found. 
* Add "import csv" to the dependecies at the beggining of your code
* Write csv rows one at a time using the writerow function. This function takes a row of values to be included in the row. 
* For our example site, the code looks like this. This code takes about 25 minutes to run due to the 5 second pause between scraping each page. 
    ~~~
    # Create an output csv file
    with open('output.csv', 'w') as file:
    	# Create a writer
    	writer = csv.writer(file)
    	# Create a header row
    	writer.writerow(['url', 'Country', 'Population', 'Area'])
    
    	# For each country page
    	for url in page_urls:
    		# pause as not to exceed the rate limit
    		time.sleep(5)
    		# load the page
    		page = requests.get(url)
    		# create soup
    		soup = BeautifulSoup(page.content, features='lxml')
    
    		# create variables for each data point
    		country = ''
    		area = ''
    		population = ''
    
    		# for each tr tag
    		for row in soup.find_all('tr'):
    			# for each data entry in that row
    			for entry in row.find_all('td'):
    				# check for the class of intrest
    				if (entry['class'][0] == 'w2p_fw'):
    					# save data if it is what we are looking for
    					if row['id'] == 'places_area__row':
    						area =  entry.text
    					elif row['id'] == 'places_population__row':
    						population =  entry.text
    					elif row['id'] == 'places_country__row':
    						country =  entry.text	
    		# Write the data to the csv
    		writer.writerow([url, country, population, area])
    ~~~
* The scraped data will be stored in a spreadsheet called output.csv:
    ![spreadsheet](/Images/BeautifulSoup/spreadsheet.png)

### Conclusion
Below is all of the code used in this workflow. It successfully scrapes area and population data from http://example.webscraping.com/ and writes it to a spreadsheet. This is a very specific case, but hopefully this example helps you to understand the tools that beautiful soup provides and gives you insight to how you might use them for your own project. 
~~~
# Install dependencies 
import requests
from bs4 import BeautifulSoup
import time
import csv

# Define the homepage url 
homepage_url = 'http://example.webscraping.com' 

# Create a list of country page urls to build
page_urls = []

# Create a variable to store the url of the page we are searching
url_to_search = homepage_url

# Create a veriable to track whether a next link exists
exists_next = True 

# Run this loop until we break it
while exists_next:
	exists_next = False 
	# pause for 5 seconds every time the loop repeats 
	time.sleep(5)

	# Download the page we are searching 
	page_to_search = requests.get(url_to_search) 
	# Create a Beautiful Soup object 
	soup_to_search = BeautifulSoup(page_to_search.content, features="lxml")
	# Get all the links which are linked to from the page we are searching
	links = soup_to_search.find_all('a')

	# Go through the links we have found
	for link in links:

		# add the homepage url to the subdirectory of the link
		link_url = homepage_url + link.get('href')

		# if the url is a page with data add it to our list
		if 'places/default/view' in link_url:
			page_urls.append(link_url)
		# Otherwise, if this has text and that text includes 'Next', set url_to_search accordingly
		elif link.string and 'Next' in link.text:
			url_to_search = link_url
			exists_next = True

	
# Create an output csv file
with open('output.csv', 'w') as file:
	# Create a writer
	writer = csv.writer(file)
	# Create a header row
	writer.writerow(['url', 'Country', 'Population', 'Area'])

	# For each country page
	for url in page_urls:
		# pause as not to exceed the rate limit
		time.sleep(5)
		# load the page
		page = requests.get(url)
		# create soup
		soup = BeautifulSoup(page.content, features='lxml')

		# create variables for each data point
		country = ''
		area = ''
		population = ''

		# for each tr tag
		for row in soup.find_all('tr'):
			# for each data entry in that row
			for entry in row.find_all('td'):
				# check for the class of intrest
				if (entry['class'][0] == 'w2p_fw'):
					# save data if it is what we are looking for
					if row['id'] == 'places_area__row':
						area =  entry.text
					elif row['id'] == 'places_population__row':
						population =  entry.text
					elif row['id'] == 'places_country__row':
						country =  entry.text	
		# Write the data to the csv
		writer.writerow([url, country, population, area])
~~~


