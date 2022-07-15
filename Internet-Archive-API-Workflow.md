# Using APIs to Scrape Data in Bulk from the Internet Archive

If an online resource has an Application Programming Interface (or API), you can more easily collect information. This example will show you how to get articles from Archive.org, which has millions of resources available in full text. 

## In this example, we will:
1. Confirm or install a terminal emulator and wget
1. Create a list of archive.org item identifiers
1. Craft a wget command to download files from those identifiers
1. Run the wget command.

## Install wget:

Windows: Read the following tutorial “Installing Cygwin Tutorial.” Choose the wget module option when prompted.

MacOSX: MacOSX comes with a terminal installed. It’s probably in your Applications folder or in your Applications > Utilities > Terminal folder. This link may help you depending on your Mac version. If you are running a different version than High Sierra, google your version and “install wget.” This will probably populate information on how to install wget with your system: Wget installation for MacOS High Sierra

If you are unable to install the wget with the links above, install Xcode. Once Xcode is installed, there are tutorials online to guide you through installing wget.

## Use wget to download files you want

To get all our files, we’ll do the following things. This workflow goes through each step one by one, but this list shows you what you’ll need to do from a bird’s eye view:
1. Create a folder on your computer to hold the downloaded files
1. Generate a list of archive.org item identifiers for the files you want to get (you can find the “identifier” at the end of the url for an archive.org item page)
1. Tell your wget command to retrieve the desired files
1. Run the command and wait for it to finish (which can take a long time depending on how many files you’re getting!)
    1. Step A: Create a folder for your downloaded files and identifiers file
Create a folder named “InternetArchive” on your computer Desktop. This is where the downloaded where files will go.

    1. Step B: Create a file with the list of identifiers

## Create a text file with items from archive.org

We need to create a text file with the list of archive.org item identifiers from which we want to download files. This file will be used by the wget to download the files. To do this, follow the steps below:

1. Use the advanced search on Archive.org to create the list and then download the list in the file. So, for example, if you want to search for “Native American Literature,” type that into the advanced search. If you’d like to narrow your search by including a date range or other available options, include those requirements in your original search.

1. Once you’ve figured out your search, go the “Advanced Search returning JSON, XML, and more” section to create your query. Select “identifier” from the “Fields to return” list. Optionally sort the results by “identifier asc”

1. Enter the number of results from step 1 into the “Number of results” box. If you want to pull every file returned by your search, enter a number higher than the number of results. If you just want to test the process, enter a low number. Beware, though, that some of the files in your query are actually folders and may contain yet more files within them. 

1. Choose the “CSV format” button.

1. Click search. An alert box will ask you if you want to see your results, and you can click “Ok.” You’ll see a prompt to download the “search.csv” file to your computer.
1. Rename the file to “itemlist.txt” without quotes.
1. Drag this “itemlist.txt” files into your “Internet_Archive” folder that you created.
1. Open the file in a text editor like TextEdit or Atom. Delete the first line which reads “identifier.” Now, remove all quotes by searching and replacing “ with nothing.
Your itemlist.txt file should look like this:

![A properly cleaned itemlist file](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Images/Itemlist%20Example.png?raw=true)

## Use wget to return the full text results from your itemlist.txt file
Open your terminal window and navigate to your “Internet_Archive” folder. This can be done in a few steps.
1. Open your command line
1. If your “Internet_Archive” folder is on your desktop, type “cd desktop”
1. Then type “cd Internet_Archive.”

## Below are a few commonly used wget commands for downloading the identifiers list in your itemlist.txt file.

* To get all files (including all different file formats like .pdf, .txt., gifs and more, use the below code:
wget -r -H -nc -np -nH --cut-dirs=1 -e robots=off -l1 -i ./itemlist.txt -B 'http://archive.org/download/'

* To get only certain file formats (in this case txt) you should include the -A option (which means “accept”). In this example, we would download the txt files relevant to our query.  
wget -r -H -nc -np -nH --cut-dirs=1 -A .txt -e robots=off -l1 -i ./itemlist.txt -B 'http://archive.org/download/'

* To download all files except specific formats (this example txt), you should include the -R option (or “reject”):
wget -r -H -nc -np -nH --cut-dirs=1 -R .txt -e robots=off -l1 -i ./itemlist.txt -B 'http://archive.org/download/'
Enter the command of your choice and hit “run.” It may take awhile for the program to run. In this example, it took me about two hours to complete it. Just leave your computer on and connected to your power cord, and it should be fine.

* If at any point you'd like to cancel a download process that is taking too long or was initiated in error,  Ctrl+C should quit the process. You can also force quit the Terminal itself, which will have the same effect. 
