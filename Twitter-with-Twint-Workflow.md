# Mining Twitter Data with Twint Workflow
_This workflow will guide you through the process of using the [Twint library](https://github.com/twintproject/twint) to mine data from Twitter. Last updated April 2020._
***
### Is Twint the Right Tool for my Project?
Twint is fundamentally more technical and less user friendly than [the Twitter API](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Twitter-API-Workflow.md). Therefore, you should use the Twitter API when possible to save yourself work. That said, Twint offers fewer restrictions than the API. Use Twint if:
* You need to mine tweets that are more than a week old. The Twitter API only allows you to access tweets from the last week or to set criteria to record future tweets as they are published. (IMPORTANT DISCLAIMER: as of July of 2022, Twint is not working to collect large numbers of historical tweets. Although it is able to go beyond the standard search window, some changes to the Twitter API have limited it to collecting only a few tweets from that window. It is still therefore a viable option for collecting a small dataset/performing historical searches, but if you want to pull large numbers of historical tweets it would be best to look elsewhere for now. Check out our Melanie Walsh's writeup of one alternative, twarc, [here.](https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/12-Twitter-Data.html))
* You need to collect more than 3,200 tweets. The Twitter API will return a maximum of 3,200 tweets.
* You want to be anonymous. The Twitter API requires you to sign in with a Twitter account.
* You don't want rate limitations. If you want to use a tool programatically (in code), the Twitter API will impose rate limitations.

If your project can be completed by gathering no more than 3,200 tweets from the past week and/or the future and you're not worried about anonymity or rate limitations then you should use [the Twitter API](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Twitter-API-Workflow.md). Otherwise, continue onward to learn how to use Twint.
If you're interested, [here](https://www.youtube.com/watch?v=jzLJjbZVQ9s) is a video that expains most of the information covered in this workflow.
### Set Up:
* Install Python 3.6 if you don't already have it. You can find it [here](https://www.python.org/downloads/).
* If you have not already, [install git](https://git-scm.com/downloads).
* Open a new terminal. Enter the following commands one at a time.
    ~~~
    git clone https://github.com/twintproject/twint.git
    cd twint
    pip3 install . -r requirements.txt
    ~~~
    This last command may take a number of minutes to execute. Your computer is accessing all of the Python libraries that Twint uses to mine Twitter data.
### Using Twint:
Now you're ready to begin searching Twitter and scraping Twitter data. Twint offers a variety if search parameters. For example, you can search for tweets from a specific user, time frame, geolocation, and/or for tweets containing specific words or phrases. You can combine multiple parameters to make your search more specific and useful. A full list of Twint's parameters and options can be found [here](https://github.com/twintproject/twint/wiki/Basic-usage). This workflow will proceed to explain how make a Twint search, explain some of the most useful parameters, and give a few examples.
##### Making a Twint Search
To use Twint, type "twint" into terminal followed by your search parameter. Type each search parameter in a space separated list.
##### Useful parameters
* Search for tweets from specific users:
    Include "-u " followed by the username the of twitter user you want to search for tweets from.
    For example, the following command accesses all of the tweets from Elon Musk. Note that Elon Musk has **many** tweets so this may take a couple minutes to run. You can interupt any search using control-z. 
    ~~~
    twint -u elonmusk
    ~~~
* Search for tweets including specific words or phrases:
    Include "-s " followed by a word or phrase in quotes. For example, the following command accesses all of the tweets from Elon Musk that mention the word spacex.
    ~~~
    twint -u elonmusk -s "spacex"
    ~~~
    You can also use -s to search for tweets with a certian hashtag by including the # in the searchterm. To search for only those tweets that include the hashtag #spacex simply modify the above command to the following.
    ~~~
    twint -u elonmusk -s "#spacex"
    ~~~
* Search for geotagged tweets from a specific geolocation:
    Include -g followed by lattitude, longitude, and a radius with commas between them and a single pair of quotes around all three. The coordinates of a location can be easily found by right clicking on a location on [Google Maps](https://www.google.com/maps) and selecting "what's here?" For example, the following command accesses all of the tweets that mention the word spacex and are geotagged within two kilometers of the SpaceX launch complex in Cape Canaveral, Florida:
     ~~~
    twint -s "spacex" -g "28.562115,-80.577587,2km"
    ~~~
* Search for tweets until or since a particular moment in time:
    Include --since or --until followed by a moment in time in quotes in the format "YYYY-MM-DD HH:MM:SS". You can use both --since and --until for a specific window of time. For example the following command accesses all of the tweets that mention the word spacex and are geotagged within two kilometers of the SpaceX launch complex in Cape Canaveral, Florida since January first, 2020 at 1:13PM and 59 seconds:
    ~~~
    twint -s "spacex" -g "28.562115,-80.577587,2km" --since "2020-01-13 13:13:59"
    ~~~
##### Saving the results
So far we have only seen results printed in Terminal. You can have them automatically saved to a file using "-o". Add "-o" and a file name to your command and your results will be saved to that file. For example, the following command accesses all of the tweets from Elon Musk that mention the word spacex and saves them into a file called tweets.txt:
~~~
twint -u elonmusk -s "spacex" -o "tweets.txt"
~~~
You can also save your results as a csv file (easily opened as a spreadsheet). To do so, include "-o" and a file name ending in .csv and "--csv" in your command. For example, the following command accesses all of the tweets from Elon Musk that mention the word spacex and saves them into a file called tweets.csv:
~~~
twint -u elonmusk -s "spacex" -o "tweets.csv" --csv
~~~
### Separating each tweet into a text file:
If you want to split each tweet into its own text file, follow the instructions above to save the tweets into a .txt file. Then, begin on step 3 of [this workflow](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Spreadsheet-Splitting-Workflow.md).
    

