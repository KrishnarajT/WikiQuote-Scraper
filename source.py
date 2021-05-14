# This is a scraper that will get the html text from the editing page of wikiquote, and then convert it to a file that fortune can read
# The idea belongs to Lucas Z and was read from his Blog and his repo https://github.com/lukas2/wikiquote_to_fortune in which the same thing is done with ruby
# but when I installed it, it did not work, and i could not get it working as i dont know a lot of ruby, and even with a lot of failed attempts, i
# could not make it work with ruby installed on my linux machine, and so i decided to make a python alternative as i really wanted the fortune quotes to work, and thought this was a cool idea. 


import requests
import re, sys, time
from bs4 import BeautifulSoup


def main():

    try:
        word = sys.argv[1].replace('\"', '')
        print(word)
        url = 'https://en.wikiquote.org/w/index.php?action=edit&title=' + word
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        quotes = soup.text
        quotes = re.sub("===([a-z]|[A-Z]|\s|[0-9]|[\\'-_@!#$\\|%&\\(\\)\\[\\]])*===", "<hr width=\"50%\"/>\n", quotes)
        quotes = re.sub("\\[\\[w:([a-z]|[A-Z]|\s|[0-9]|[\\'-_@!#$%&\\(\\)\\[\\]])*\\|", "", quotes)
        quotes = re.sub("\\]\\]", "", quotes)
        quotes = re.sub("\\:\'\'\'", "<b>", quotes)
        quotes = re.sub("=\s", "=", quotes)
        quotes = re.sub("\s=", "=", quotes)
        quotes = re.sub("\n\n", "\n", quotes)
        quotes = re.sub("\n\n", "\n", quotes)
        quotes = re.sub("<\s", "<", quotes)
        quotes = re.sub("\s>", ">", quotes)
        quotes = re.sub("\'\'\'", "<b>", quotes)
        quotes = re.sub("\\:\'\'", "<i>", quotes)
        quotes = re.sub("\'\'", "<i>", quotes)
        extracted = re.sub("\<hr width=[\"\s][0-9][0-9]\%[\"\s]\/>\\n", "%%%%\n\n", quotes)
        extracted = re.sub("\\<hr width=[0-9][0-9]%\\/>\\n", "%%%%\n\n", extracted)
        extracted = re.split("%%%%\n", extracted)
        extracted.remove(extracted[-1])
        extracted.remove(extracted[0])

        # Making the text file
        with open('extract.txt', 'w') as f:
            f.writelines(extracted)

        print('Made raw extract file')

        quotes = re.sub("\<hr width=[\"\s][0-9][0-9]\%[\"\s]\/>\\n", f"\n - {word.replace('_', ' ')}\n%%%%\n%\n", quotes)
        quotes = re.sub("\\<hr width=[0-9][0-9]%\\/>\\n", f"\n - {word.replace('_', ' ')}\n%%%%\n%\n", quotes)
        quotes = re.sub("<b>", "", quotes)
        quotes = re.sub("<i>", "", quotes)
        quotes = re.split("%%%%\n", quotes)
        quotes.remove(quotes[-1])
        quotes.remove(quotes[0])
        quotes[0] = quotes[0].replace('%\n', '')

        # Making the fortune file
        with open(word, 'w') as f:
            f.writelines(quotes)

        print('Made Fortune File.')
        print('Everything Done Successfully!')

    except Exception as err:
        print('Not Done Successfully')
        print(err)
        time.sleep(2)
        exit()


main()