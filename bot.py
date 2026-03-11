import requests
import time
import threading
import os
from datetime import datetime
from flask import Flask

from config import TOKEN, CHAT_ID
from news_engine import fetch_news
from sentiment_engine import analyze
from alpha_brief import generate
from market_engine import premarket_scan

if link in SEEN_NEWS:
    continue

SEEN_NEWS.add(link)

save_seen(link)
app = Flask(__name__)

@app.route("/")
def home():
    return "Investor Terminal v6 running"

def load_seen():

    try:
        with open("sent_news.txt","r") as f:
            return set(f.read().splitlines())

    except:
        return set()


def save_seen(link):

    with open("sent_news.txt","a") as f:
        f.write(link+"\n")

def send(msg):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })


def morning_report():

    brief = generate()

    send(brief)

    movers = premarket_scan()

    if movers:

        msg = "🚨 Premarket Movers\n\n"

        for m in movers:
            msg += f"{m}\n"

        send(msg)

if len(SEEN_NEWS)>500:
    SEEN_NEWS.clear()

def breaking_news():

    news = fetch_news()

    for item in news:

        link = item["link"]

        if link in SEEN_NEWS:
            continue

        SEEN_NEWS.add(link)

        sentiment = analyze(item["summary"])

        now = datetime.now().strftime("%H:%M")

        msg=f"""
⚡ ข่าวด่วนตลาดหุ้น

🕒 {now}

🏢 {item['ticker']}

📰 {item['title']}

📊 Sentiment
{sentiment}

📄 สรุปข่าว
{item['summary']}

📰 Source
{item['source']}

🔗 {item['link']}
"""

        send(msg)


def bot_loop():

    print("Investor Terminal v6 started")

    morning_report()

    while True:

        try:
            breaking_news()
        except Exception as e:
            print("ERROR:", e)

        time.sleep(300)


if __name__ == "__main__":

    threading.Thread(target=bot_loop).start()

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
