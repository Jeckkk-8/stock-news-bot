import requests
import time
import threading
import os
from flask import Flask

from config import TOKEN,CHAT_ID
from news_engine import fetch_news
from sentiment_engine import analyze
from alpha_brief import generate
from market_engine import premarket_scan

app=Flask(__name__)

@app.route("/")
def home():
    return "Investor Terminal v6 running"

def send(msg):

    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":msg
    })


def morning_report():

    brief=generate()

    send(brief)

    movers=premarket_scan()

    if movers:

        msg="🚨 Premarket Movers\n\n"

        for m in movers:

            msg+=f"{m}\n"

        send(msg)


def breaking_news():

    news=fetch_news()

    for item in news:

        sentiment=analyze(item["summary"])

        msg=f"""
⚡ ข่าวด่วนตลาดหุ้น

🏢 {item['ticker']}

📰 {item['title']}

📊 Sentiment
{sentiment}

📄 สรุปข่าว
{item['summary']}

🔗 แหล่งข่าว
{item['link']}
"""

        send(msg)


def bot_loop():

    print("Investor Terminal v6 started")

    morning_report()

    while True:

        breaking_news()

        time.sleep(300)


if __name__=="__main__":

    threading.Thread(target=bot_loop).start()

    port=int(os.environ.get("PORT",10000))

    app.run(host="0.0.0.0",port=port)
