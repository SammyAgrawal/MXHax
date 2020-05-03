my_api_key = "87a9307974f4442ea0c08daf27e46918"
from newsapi import NewsApiClient
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key=my_api_key)
#nltk.download('vader_lexicon')

def getArticles(num):
    return(newsapi.get_everything(q="up",
            from_param='2020-05-01',
                to='2017-05-03',
                language='en',
                sort_by='relevancy',
                page=num))
def getResult():
    all_res = []
    for i in range(1,6):
        articles = getArticles(i)['articles']
        for article in articles:
            all_res.append(article)
    return all_res

def goodNewsArray():
    news_array = []
    midnight = 'T00:00:00'
    noon = 'T12:00:00'
    b4mdn = 'T23:59:59'
    for i in range(0,16):
        j = i
        k = 26
        if i<10:
            st = '2020-04-' 
            et = '2020-04-'
        else:
            st = '2020-05-0' 
            et = '2020-05-0'
            j = i-10
            k = 1
        if (i%2 == 0):
            st = st + str(int(j/2) + k) + midnight
            et = et + str(int(j/2) + k) + noon
        else:
            st = st + str(int(j/2) + k) + noon
            et = et + str(int(j/2) + k) + b4mdn
        newsapi = NewsApiClient(api_key='2fe96f1bcd91473ebbfa6975cf5d1fe1')
        news = newsapi.get_everything(q='happy AND help NOT fail NOT despair NOT sad NOT earnings NOT tech',
                            from_param= st,
                            to = et,
                            sort_by = 'popularity',
                            page_size = 100,
                            language = 'en'
                            )['articles']
        for item in news:
            store_details = {}
            store_details['time'] = item['publishedAt']
            store_details['title'] = item['title']
            store_details['description'] = item['description']
            store_details['link'] = item['url']
            store_details['imgurl'] = item['urlToImage']
            news_array.append(store_details)
    sia = SIA()
    results = []
    for line in news_array: #sample has to be a list like Alan's news_array
        analyze = str(line['title'])+str(line['description'])
        pol_score = sia.polarity_scores(analyze)
        pol_score['headline'] = line['title']
        if pol_score['pos']>0.35:
            results.append({'time': line['time'], 'title': line['title'], 'description': line['description'], 
                            'link': line['link'], 'pos': pol_score['pos'], 'compound':pol_score['pos'], 'imgurl':line['imgurl']})
    return results

articles = goodNewsArray()