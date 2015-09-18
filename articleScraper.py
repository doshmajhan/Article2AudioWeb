from newspaper import Article
from gtts import gTTS

def articleScraper(url):
    a = Article(url, language='en')
    a.download()
    a.parse()
    articleString = a.text
    tts = gTTS(text=articleString, lang='en')
    tts.save("article.mp3")


if __name__ == '__main__':
    url = raw_input("URL: ")
    articleScraper(url)

