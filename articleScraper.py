from newspaper import Article
from gtts import gTTS

def articleScraper(url):
    print "Scraping article...."
    a = Article(url, language='en')
    a.download()
    a.parse()
    articleString = a.text
    print "Converting to mp3...."
    tts = gTTS(text=articleString, lang='en')
    tts.save("static/article.mp3")
    print "Finished"


if __name__ == '__main__':
    url = raw_input("URL: ")
    articleScraper(url)

