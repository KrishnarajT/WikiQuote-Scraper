![](https://github.com/KrishnarajT/WikiQuote-Scraper/blob/master/Wikiquote%20Scrapper_.png)

# Wikiquotes Scraper

This is a convenient hacky little python script that I wrote to get some quotes from wikiquotes to fortune. 

This was done because the official method in the fortune archwiki did not seem to work. 

I then saw the [blog of Lucas Z ](https://www.lukaszielinski.de/blog/posts/2019/01/20/how-to-scrape-wikiquote/#:~:text=Open%20it%20on%20your%20browser,lines%20that%20only%20contain%20quotes.) who explained that you could go the edit page of wikiquotes, and scrap the text from there. He did it using ruby and published his repo [here](https://github.com/lukas2/wikiquote_to_fortune). However, this did not work for me, and is written in ruby, that I dont really understand and couldn't debug, and so I decided to write it in python for a few wiki pages that I liked for the shows that I had seen. The basic idea of the code has been copied from his repo.

_I do not guarantee that It will work on any page of wikiquote, but may work on some. It is made largely just for personal convenience, and I decided to make it public in case someone wanted to give it a go._

## Requirements

1. resources
2. beautiful-soup4

`pip install resources beautifulsoup4` 

## Installation

Just clone using git, and run `python source.py "NAME_OF_WIKIPAGE"` after installing the requirements for python. 

## Usage

1. Run `python source.py "NAME_OF_WIKIPAGE"` after installing and navigating to the direcotory of install. 
2. It will generate a fortune file
3. While in the same directory as the previously mentioned fortune file, run `strfile FILENAME` to generate a binary `.dat` file. 
4. Copy both the files to your fortune folder, Generally located in `/usr/bin/Fortune`
5. Run fortune, and you should now see quotes from the files that you added (which will be taken on random, so if you just want to see for your files, refer to fortune wiki)

## Improvements and TO-DO

1. Make it download every wikiquote page as its a cool site.
2. Make a gui for downloading several pages.
3. Add the ability to create binary files within the program so the user doesn't have to do it manually
4. Make it an executable that can run in both places.
5. Add it to the AUR, add the Packages to the AUR, Add it to PyPi as well for installation using pip

## Contribution.

Any File that you create using this program or a fork of this or any project concerning creation of fortune style files from wikiquotes is welcome to be added and contiributed to ./Fortune Files directory of this repo.

## Credits

[Lucas Z ](https://www.lukaszielinski.de/blog/posts/2019/01/20/how-to-scrape-wikiquote/#:~:text=Open%20it%20on%20your%20browser,lines%20that%20only%20contain%20quotes.) for his idea of scraping the editing page. Thanks!
