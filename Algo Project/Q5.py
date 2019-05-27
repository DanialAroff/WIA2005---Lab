# trying to extract text from website

from newspaper import Article
from bs4 import BeautifulSoup
import re

stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and',
             'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being',
             'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did',
             "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few',
             'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having',
             'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
             'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
             'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't",
             'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other',
             'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd",
             "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's",
             'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they',
             "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under',
             'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
             'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why',
             "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've",
             'your', 'yours', 'yourself', 'yourselves']


url = "https://www.dhakatribune.com/bangladesh/dhaka/2019/05/25/dncc-mayor-footpaths-must-be-kept-clear-to-" \
      "reduce-tailbacks"
# untuk download artikel daripada internet
article = Article(url, keep_article_html=True, language='en')
article.download()
article.parse()
article.nlp()

page = open('news/Dhaka.html', 'w', encoding='utf-8')
page.write(article.html)
page.close()


# to extract text from the html. BeautifulSoup untuk dapatkan text drp HTML
soup = BeautifulSoup(article.html, features="lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get text
text = soup.get_text()

# splitting text into list of words
list_of_words = text.split()

# remove non-alphanumeric characters like ! and &
word = ''
list_of_words = [re.sub(r'\W+', '', word) for word in list_of_words]

print(list_of_words)


