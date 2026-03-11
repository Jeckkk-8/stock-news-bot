import feedparser
from newspaper import Article
from deep_translator import GoogleTranslator
from config import RSS_FEEDS,STOCKS

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

                if stock.lower() in title.lower():

                    try:

                        article=Article(link)
                        article.download()
                        article.parse()

                        text=article.text

                        summary=summarize(text)

                        results.append({

                        "ticker":stock,
                        "title":translator.translate(title),
                        "summary":translator.translate(summary),
                        "link":link

                        })

                    except:
                        pass

    return results
