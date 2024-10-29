# Scraping NYT Using Requests and the NY Times Archive API


## Overview

This repository includes several examples of fetching data via an API using Python 3 and the Requests module, 
illustrating basic code for making requests and saving responses, as well as specific details for 
working with each of the API sources.

This section now includes [Frank Donnelly's updated code](https://github.com/Brown-University-Library/geodata_api_tutorials/tree/main/nytimes) for interacting with the New York Times 
(NYT) Archive API with abstraction. This abstraction improves code maintainability, readability, and ease of reuse.

## Prerequisites

To run these programs, you will need to:

1. **Install Python 3**:
    - You can either install Python directly from [python.org](https://www.python.org/downloads) or use a distribution like Anaconda.
    - The scripts have been tested with Python version 3.10.5.

2. **Install the Requests module**:
    - The Requests module is required for making API calls. Install it using pip:
      ```bash
      pip install requests
      ```
    - If using Anaconda, the Requests module may already be included.

3. **Get an API key**:
    - You will also need an API key from the NYT. Follow the sign up process [here](https://developer.nytimes.com/) to create a developer account. Once you are signed in, go to the "Apps" page dropdown under your username or [here.](https://developer.nytimes.com/my-apps) 
    - Click the "+ New App" button in the top right corner. Give your project a name and make sure to enable both the Archive and the Article Search APIs. Click save, and you should be brought to a screen that looks like this: 
    ![NYT site](Images/NYT/nytsite.png)
    - Take note of any restrictions on the number of requests you can make.

4. **Save your API key**:
    - Store your API key in a plain text file (`nyt_key.txt`), as the script will read it from this file. Store the API key in the same folder where you will download the python script (seee Instructions step 2.)

## Concepts Demonstrated in the Example

The updated code demonstrates the following procedures:

1. **Setting up variables**: Defining year, month, and search terms.
2. **Formatting API requests**: Creating the URL using the NYT Archive API.
3. **Reading an API key from a file**: Abstracted into a reusable function _read_api_key_.
4. **Making the API request**: Abstracted for flexibility in fetching data for various months and years.
5. **Filtering JSON data**: Parsing complex multi-level JSON and searching for specific terms.
6. **Writing results to a CSV file**: Saving the filtered data for further analysis.

## Example Scripts

The abstracted code can be found in the [`nyt_archives_api`](https://github.com/Brown-University-Library/geodata_api_tutorials/tree/main/nytimes) folder in Frank Donnelly's API tutorials repository. Below is a brief explanation of the code structure:

### nyt_archives_api

This script demonstrates:

1. **Reading an API key**: Stored in a `nyt_key.txt` file and read into the script for secure use.
2. **Making an API request**: Fetching metadata for articles published in a given month and year.
3. **Searching through complex JSON data**: Filtering results by specific terms found in article abstracts or leads.
4. **Saving output**: Exporting filtered results, including metadata and article URLs, to a CSV file for further analysis.

### Instructions

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

## Special Credits

This project is based on the original work by Frank Donnelly, Head of GIS and Data Services at Brown University Library. The current version includes abstractions to ensure easier management and extensibility.
