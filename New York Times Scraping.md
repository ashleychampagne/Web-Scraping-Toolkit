# Scraping NYT Using Requests and the NY Times Archive API

## Overview

This repository includes several examples of fetching data via an API using Python 3 and the Requests module, 
illustrating basic code for making requests and saving responses, as well as specific details for 
working with each of the API sources.

This section now includes [Frank Donnelly's updated code](https://github.com/Brown-University-Library/geodata_api_tutorials/tree/main/nytimes) for interacting with the New York Times 
(NYT) Archive API with abstraction. This abstraction improves code maintainability, readability, and ease of reuse.

## 1. Requirements
This workflow requires you to run pre-written python programs in order to search and then collect article data from the NYT archives. In order to run these programs, you will need:

### Python and Python Packages
To install python if you have not already. Download a recent version from this link. This tutorial was written as of version 3.10.5.
To install a few python modules to help these programs run. Rather than downloading anything from a website, this requires you to go into the Terminal (if you are on Mac) or Command Prompt (on Windows) and enter some commands. First, search for the relevant program on your device (Terminal or Command Prompt, depending on which type of computer you have) and open it. You will see a screen that looks like this: empty terminal
Since you have already installed python in the first step above, you can begin installing the relevant packages. Type (or copy) in the command python3 -m pip install requests and press enter. It may take a moment to complete (you will see text appearing and scrolling by, listing the progress of the download), but eventually the command line will reappear with the flashing cursor, like so: after first command You will have different text between the first command (highlighted in blue in the image) and the new command line (at the bottom, where the grey box cursor now is), because you are downloading these packages for the first time.
In the same way you entered this command and then waited for it to finish, enter the following commands:
python3 -m pip install bs4
python3 -m pip install lxml
Now you have everything set up to run these scripts!


## 2. Get an API key:
    - You will also need an API key from the NYT. Follow the sign up process [here](https://developer.nytimes.com/) to create a developer account. Once you are signed in, go to the "My Apps" page [here.](https://developer.nytimes.com/my-apps) 
    - Click the "+ New App" button in the top right corner. Give your project a name and make sure to Enable the Article Search API. Click save, and you should be brought to a screen that looks like this: 
    ![NYT site](Images/NYT/nytsite.png)
    - Take note of any restrictions on the number of requests you can make.

## 3. **Save your API key**:
    - Store your API key in a plain text file (`nyt_key.txt`), as the script will read it from this file.
    
## 4. Searching

The abstracted code can be found in the [`nyt_archives_api`](https://github.com/Brown-University-Library/geodata_api_tutorials/tree/main/nytimes) folder in Frank Donnelly's API tutorials repository. Below is a brief explanation of the code structure:

### nyt_archives_api

This script demonstrates:

1. **Reading an API key**: Stored in a `nyt_key.txt` file and read into the script for secure use.
2. **Making an API request**: Fetching metadata for articles published in a given month and year.
3. **Searching through complex JSON data**: Filtering results by specific terms found in article abstracts or leads.
4. **Saving output**: Exporting filtered results, including metadata and article URLs, to a CSV file for further analysis.

**Instructions**

1. **Download the repository**: Click on the green `Code` button at the top and download the entire repository as a ZIP file.
2. **Extract the contents**: After downloading, extract the folder to your desired location.
3. **Run the Python script**: 
    - Open Terminal (macOS/Linux) or Command Prompt (Windows).
    - Navigate to the folder containing the Python script.
    - Run the script by typing:
      ```bash
      python nyt_archives_api.py
      ```
    - Ensure that the `nyt_key.txt` file with your API key is in the same directory.
  
## 5. Setting up for Scraping
After you have created a spreadsheet with the results of your NYT search, you may want to find the full text of these articles.

To do this, first select the column that contains the article urls. Copy the column and paste it into a new, empty spreadsheet. The new file will have just the one column containing the urls you want to visit. It should look like this:

single column

Using either Export or Save As, save this file as a .csv file with the name nytlinks.csv. Put it in a new, empty folder called "NYT Scraping", which can live on your Desktop.

Download the following file titled nytscraper.py into that folder as well: nytscraper.py.

To complete the setup, open a text editor (TextEdit will work fine) and save an new, empty file with the name articlefulltext.csv. (Once this file is populated with information, you can rename it and move it elsewhere. For now though it has to have this specific name so that the program can find it.) Make sure it is also saved to the "NYT Scraping" folder. At this point, the folder should look like this:

folder set up

##6. Scraping
Navigate in the terminal to the "NYT Scraping" folder, either by right clicking and selecting "New Terminal at Folder" or by using cd commands to navigate to it. (For example, if it was in your documents folder, you would start with the command cd Documents and then type cd "NYT Scraping").

Now type or paste into the Terminal or Command Prompt this command to run the program:

python3 nytscraper.py
and press enter. It may take a moment for the program to run. You'll know it's done when the terminal prints "Done Scraping!"

Now open the file articlefulltext.csv. You should see it populated with three columns: date, url, and full text, like this:

complete sheet

You can now save this file with a new name and proceed as you want with it!

Next Steps
To explore possible uses of the new article text data you've extracted, check out the libary's resources on text mining.

## Special Credits

This project is based on the original work by Frank Donnelly, GIS and Data Librarian at Brown University Library. The current version includes abstractions to ensure easier management and extensibility.
