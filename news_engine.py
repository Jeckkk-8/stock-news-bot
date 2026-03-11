import feedparser
from newspaper import Article
from deep_translator import GoogleTranslator
from config import RSS_FEEDS,STOCKS

SOURCE_MAP={
"reuters":"Reuters",
"cnbc":"CNBC",
"yahoo":"Yahoo Finance",
"seekingalpha":"Seeking Alpha",
"investing":"Investing.com"
}

COMPANY_NAMES={
"NVDA":"nvidia",
"AMZN":"amazon",
"MSFT":"microsoft",
"GOOGL":"google",
"META":"meta",
"TSM":"tsmc",
"PLTR":"palantir",
"CRWD":"crowdstrike",
"LLY":"eli lilly",
"RKLB":"rocket lab",
"AVGO":"broadcom",
"VRT":"vertiv",
"CEG":"constellation",
"OKLO":"oklo",
"RBRK":"rubrik"
}

translator=GoogleTranslator(source="auto",target="th")

def summarize(text):

    sentences=text.split(". ")

    return ". ".join(sentences[:5])


def fetch_news():

    results=[]

    for feed in RSS_FEEDS:

        data=feedparser.parse(feed)

        for entry in data.entries:

            title=entry.title
            link=entry.link

            for stock in STOCKS:

                company=COMPANY_NAMES[stock]

                if stock.lower() in title.lower() or company in title.lower():

                    try:

                        article=Article(link)
                        article.download()
                        article.parse()

                        text=article.text

                        summary=summarize(text)

                        source="News"

                     for key in SOURCE_MAP:

                         if key in link.lower():

                            source=SOURCE_MAP[key]

                            results.append({

                            "ticker":stock,
                            "title":title_th,
                            "summary":summary_th,
                            "link":link,
                            "source":source

})
                    except:
                        pass

    return results
