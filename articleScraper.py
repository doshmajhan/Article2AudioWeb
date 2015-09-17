from newspaper import Article
from gtts import gTTS

def articleScraper(url):
    a = Article(url, language='en')
    a.download()
    a.parse()
    articleString = a.text
    tts = gTTS(text='Hello', lang='en')
    tts.save("hello.mp3")


def main():
    #url = raw_input("URL: ")
    url = "http://www.nytimes.com/2015/09/17/us/texas-student-is-under-police-investigation-for-building-a-clock.html?ref=us&_r=0"
    articleScraper(url)


main()
