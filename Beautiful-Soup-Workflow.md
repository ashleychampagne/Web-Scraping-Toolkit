# Beautiful Soup Workflow
_This workflow will help you use beautiful soup in Python to put together useful data sets. This workflow will cover some of the basics of Beautiful Soup by working through the example of scraping data from http://example.webscraping.com/. This workflow will not be comprehensive by any means, but the goal is to cover enough to get you through a simple data collection project or to get you started with a larger project. It will assume some very basic Python programing knowledge such as how for loops and if statements work._
_Last updated April 2020_
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
##### Compiling a list of URLs
Often, you will want to scrape data from a number of pages which are all linked to from a homepage. The first step is to scrape a list of links from the home page.
* Here is a screenshot of the homepage we are scraping for reference
    ![homepage](/Images/BeautifulSoup/homepage)
* Create the soup: The first step to any application of beautiful soup is to create a beautiful soup object.
    ~~~
    # Define the homepage url
    homepage_url = "http://example.webscraping.com/"
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
##### Scraping data from each page
Now we want to scrape data from each page that the homepage linked to. This process will look very similar to the way we scraped the homepage, but we will do it for each link in a loop. Notice that each url we printed was just a subdirectory with no domain. We will remedy this by simply adding the domain back to each url
* Create a Beautiful Soup object for each linked page:
    ~~~ 
    for link in links:
        # Load each page
        page = requests.get(''link.get('href'))
        # Create a Beautiful Soup object for each page
        soup = BeautifulSoup(page.content, features='lxml')
    ~~~
* Looking at the website we are scraping, we see that there are several data points for each country. Let's get the area and population of each country. We start by printing the html so we know what we're looking for
    ~~~
    print(soup.prettify())
    ~~~
    For Afganistan we get:
    !(Afganistan)[Images/BeautifulSoup/Afganistan]
        

