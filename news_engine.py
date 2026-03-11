import feedparser
from newspaper import Article
from deep_translator import GoogleTranslator
from config import RSS_FEEDS, STOCKS

def get_article_text(url):

    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text

        if len(text) < 200:
            return None

        return text

    except:
        return None


def summarize(text):

    sentences = text.split(". ")

    summary = ". ".join(sentences[:5])

    return summary


def translate(text):

    try:
        thai = GoogleTranslator(source="auto", target="th").translate(text)

        return thai

    except:

        return text


def fetch_news():

    results = []

    for feed in RSS_FEEDS:

        data = feedparser.parse(feed)

        for entry in data.entries:

            title = entry.title
            link = entry.link

            for stock in STOCKS:

                if stock.lower() in title.lower():

                    article = get_article_text(link)

                    if article is None:
                        continue

                    summary = summarize(article)

                    thai_summary = translate(summary)

                    results.append({

                        "ticker": stock,
                        "title": title,
                        "summary": thai_summary,
                        "link": link

                    })

    return results
