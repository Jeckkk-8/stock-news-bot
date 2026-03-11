import feedparser
from config import RSS_FEEDS,STOCKS

def fetch_news():

    results=[]

    for feed in RSS_FEEDS:

        data=feedparser.parse(feed)

        for entry in data.entries:

            title=entry.title
            text=title.lower()

            for stock in STOCKS:

                if stock.lower() in text:

                    results.append({
                        "ticker":stock,
                        "title":title,
                        "source":feed
                    })

    return results
