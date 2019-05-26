# trying to extract text from website

import newspaper
import nltk
from newspaper import Article
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# nltk.download('punkt')
url = "https://www.dhakatribune.com/bangladesh/dhaka/2019/05/25/dncc-mayor-footpaths-must-be-kept-clear-to-reduce-tailbacks"
fyt = "https://www.instagram.com/p/Bx3Y54TJ03X/"

dhaka_article = Article(url, keep_article_html=True, language='en')
dhaka_article.download()
dhaka_article.parse()
dhaka_article.nlp()
print("Article's Title:")
# print(dhaka_article.title,'\n')
# print(dhaka_article.html)
# print(dhaka_article.article_html)

soup = BeautifulSoup(dhaka_article.html, features="lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get text
text = soup.get_text()

# splitting text into list of words
list_w = text.split()

# remove non-alphanumeric characters
word = ''
list_w = [re.sub(r'\W+', '', word) for word in list_w]

print(list_w)


