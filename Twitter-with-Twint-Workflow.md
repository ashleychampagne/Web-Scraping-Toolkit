# Mining Twitter Data with Twint Workflow
_This workflow will guide you through the process of using the [Twint library](https://github.com/twintproject/twint) to mine data from Twitter. Last updated April 2020._
***
### Is Twint the Right Tool for my Project?
Twint is fundimentally more technical and less user friendly than [the Twitter API](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Twitter-API-Workflow.md). Therefore, you should use the Twitter API when possible to save yourself work. That said, Twint offers fewer restrictions than the API. Use Twint if:
* You need to mine tweets that are more than a week old. The Twitter API only allows you to access tweets from the last week or to set criteria to record future tweets as they are published. 
* You need to collect more than 3,200 tweets. The Twitter API will return a maximum of 3,200 tweets.
* You want to be anonymous. The Twitter API requires you to sign in with a Twitter account.
* You don't want rate limitations. If you want to use a tool programatically (in code), the Twitter API will impose rate limitations.

If your project can be completed by gathering no more than 3,200 tweets from the past week and/or the future and you're not worried about anonymity or rate limitations then you should use [the Twitter API](https://github.com/ashleychampagne/Web-Scraping-Toolkit/blob/master/Twitter-API-Workflow.md). Otherwise, continue onward to learn how to use Twint.
If you're interested, [here](https://www.youtube.com/watch?v=jzLJjbZVQ9s) is a video that expains most of the information covered in this workflow.
### Set Up:
* Installing Python 3.6
    * You can check which virsion of Python your computer is running by typing "python" into a new terminal and pressing enter. For example, in the screenshot below I check my Python version and discover that I am running Python 2.7:
    ![Python](/Images/Twint/python.png)
    * If you don't already have Python 3.6 you can download it [here](https://www.python.org/downloads/).
* If you have not already, [install git](https://git-scm.com/downloads).
* Open a new terminal. Enter the following commands one at a time.
    ~~~
    git clone https://github.com/twintproject/twint.git
    cd twint
    pip3 install . -r requirements.txt
    ~~~
    This last command may take a number of minutes to execute. Your computer is accessing all of the Python libraries that Twint uses to mine Twitter data.
### Using Twint:
