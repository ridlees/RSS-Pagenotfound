from feedgen.feed import FeedGenerator
import get_articles
import datetime
fg = FeedGenerator()
fg.id('test.com')
fg.title('Unoficial PageNotFound RSS')
fg.link(href='http://example.com', rel='alternate' )
fg.description("Unoficial PageNotFound RSS created by Martin K.")
articles = get_articles.get_articles()

for article in articles:
    fe = fg.add_entry()
    fe.id(article.ahref)
    fe.title(article.title)
    fe.link(href=article.ahref)
    fe.description(article.perex)

atomfeed = fg.atom_str(pretty=True)
rssfeed  = fg.rss_str(pretty=True)
fg.atom_file('atom.xml')
fg.rss_file('rss.xml')


now = datetime.datetime.now()
print(f"{now} - fetched")
    
