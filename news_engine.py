import feedparser
from newspaper import Article
from deep_translator import GoogleTranslator
from config import RSS_FEEDS, STOCKS

translator = GoogleTranslator(source="auto", target="th")

SOURCE_MAP = {
"reuters": "Reuters",
"cnbc": "CNBC",
"yahoo": "Yahoo Finance",
"seekingalpha": "Seeking Alpha",
"investing": "Investing.com"
}
IMPACT_KEYWORDS=[

"earnings",
"guidance",
"upgrade",
"downgrade",
"rating",
"contract",
"deal",
"partnership",
"acquisition",
"merger",
"ai",
"chip",
"semiconductor",
"data center",
"forecast",
"lawsuit",
"investigation",
"regulation",
"ban",
"sanction"

]
def has_market_impact(text):

    text=text.lower()

    for word in IMPACT_KEYWORDS:

        if word in text:

            return True

    return False
    
def summarize(text):

    sentences = text.split(". ")

    return ". ".join(sentences[:5])


def fetch_news():

    results = []

    for feed in RSS_FEEDS:

        data = feedparser.parse(feed)

        for entry in data.entries:

            title = entry.title
            link = entry.link

            for stock in STOCKS:

                if stock.lower() in title.lower():

                    try:

                        article = Article(link)
                        article.download()
                        article.parse()

                        text = article.text

                        summary = summarize(text)

                if not has_market_impact(summary):
                        continue

                        title_th = translator.translate(title)
                        summary_th = translator.translate(summary)

                        source = "News"

                        for key in SOURCE_MAP:

                            if key in link.lower():

                                source = SOURCE_MAP[key]

                        results.append({

                            "ticker": stock,
                            "title": title_th,
                            "summary": summary_th,
                            "link": link,
                            "source": source

                        })

                    except:

                        pass

    return results
