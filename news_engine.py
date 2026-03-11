import feedparser
from newspaper import Article
from deep_translator import GoogleTranslator
from config import RSS_FEEDS, STOCKS

translator = GoogleTranslator(source="auto", target="th")


def get_article_text(url):

    try:
        article = Article(url)
        article.download()
        article.parse()

        return article.text

    except:
        return None


def summarize(text):

    sentences = text.split(". ")

    summary = ". ".join(sentences[:5])

    return summary


def translate(text):

    try:
        return translator.translate(text)

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

                    if not article:
                        continue

                    summary = summarize(article)

                    title_th = translate(title)
                    summary_th = translate(summary)

                    results.append({

                        "ticker": stock,
                        "title": title_th,
                        "summary": summary_th,
                        "link": link

                    })

    return results
