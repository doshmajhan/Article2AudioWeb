from flask import Flask
from flask import render_template
from flask import request
import articleScraper

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request == 'POST':
        url = request.form['searchbar']
        articleScraper.articleScraper(url)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
