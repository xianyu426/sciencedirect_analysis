
import pandas as pd
from pyquery import PyQuery
key_words = 'cytoskeleton microtubular'
url_ = 'https://www.sciencedirect.com/search?qs=%s' %(key_words)
jpy1 = PyQuery(url_)
num = jpy1('#facets > div:nth-child(1) > h1:nth-child(1) > span:nth-child(1)').text().split()[0]

article_name = []
article_type = []
journal = []
time = []
author = []
if num >= 2500:
    for i in range(0, 2500, 25):
        url = 'https://www.sciencedirect.com/search?qs=cytoskeleton&offset=%d'%(i)
        jpy = PyQuery(url)
        for j in range(1, 26):
            article_name_ = jpy('li.ResultItem:nth-child(%d) > div:nth-child(1) > '
                      'div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)'%(j)).text()
            article_type_ = jpy('li.ResultItem:nth-child(%d) > div:nth-child(1) > '
                                'div:nth-child(2) > ol:nth-child(2) > li:nth-child(1) > span:nth-child(1)'%(j)).text()
            journal_ = jpy('li.ResultItem:nth-child(%d) > div:nth-child(1) > div:nth-child(2) > '
                      'ol:nth-child(3) > li:nth-child(1) > span:nth-child(1)'%(j)).text()
            time_ = jpy('li.ResultItem:nth-child(%d) > div:nth-child(1) > div:nth-child(2) > '
                   'ol:nth-child(3) > li:nth-child(3) > span:nth-child(1)'%(j)).text()
            author_ = jpy('li.ResultItem:nth-child(%d) > div:nth-child(1) > div:nth-child(2) > '
                     'ol:nth-child(4)'%(j)).text().split(',')[-2]
            article_name.append(article_name_)
            article_type.append(article_type_)
            journal.append(journal_)
            time.append(time_)
            author.append(author_)
else:
    print 'please go to the sciencedirect_spider.py to change the value of num'


data = {'author':author,
        'time':time,
        'article_name':article_name,
        'article_type':article_type,
        'journal':journal}
df = pd.DataFrame(data)
df.to_csv('sciencedirect_test.csv', encoding = 'utf-8')
#print df






