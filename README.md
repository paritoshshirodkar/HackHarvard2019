# HackHarvard2019


## Motivation
Nowadays, people are constantlty busy behind one form of screen or other and forget to take a break.
My teammates and I thought a great idea for the hackathon would be to make peoples' lives easier by forcing them to take a break from their work in a fun way.

## Presenting Amuse Me a Chrome extension designed to show you memes based on your current webpage!

We do this by computing the most frequent words from your current webpage, eliminating the stop words. 
Based on the top 5 words we scrape funny memes and display it in a browser pop-up.


Want to work? Challenge accepted! If you have this extension enabled, you'll be bombarded with memes every few minutes to keep you from getting your work done.


You will be forced to quit the browser to stop the memes.

Follow the steps mentioned here to enable developer mode in Google Chrome and see the extension in action
All files pertaining to extension are in Amuze Me/ 
```
https://developer.chrome.com/extensions/getstarted
```

## Tech Stack

We have leveraged Google Cloud Platform to host our API (developed using Flask) which computes the term frequency and scrapes memes from giphy.com and reddit

HTMLTextAPI.py corresponds to our Flask based API.

The extension itself is build using Javascript but other components of the project are developed using python.
