from bottle import route, run
from scraper import articles

#articles = getResult()

@route('/')
def index():
    return("<h1> On the Home page! Go to /articles to see our scraped data! </h1>")

@route('/articles')
def getArticles():
    return {'articles':articles}

run(reloader=True, debug=True)