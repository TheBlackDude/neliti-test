from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """

    html = open(url, 'r', encoding='utf-8')
    code = html.read()

    soup = BeautifulSoup(code, features="html.parser")

    # We get the words in paragrphs
    text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
    c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

    # We get the words in divs
    text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
    c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

    # We sum the two countesr and get a list with words count from most to less common
    total = c_div + c_p
    returnDict = {}

    for k, v in total.most_common():
        returnDict[k] = v
    return returnDict

