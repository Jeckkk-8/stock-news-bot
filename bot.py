import requests
import time
import threading
import os
from flask import Flask

from news_engine import fetch_news
from sentiment_engine import analyze
from alpha_brief import generate
from config import TOKEN,CHAT_ID

app = Flask(__name__)

@app.route("/")
def home():
    return "Investor Terminal Running"

def send(msg):

    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":msg
    })


def bot_loop():

    print("Investor Terminal started")

    brief = generate()
    send(brief)

    while True:

        news = fetch_news()

        for item in news:

            sentiment = analyze(item["title"])

            msg=f"""
⚡ ข่าวด่วนตลาดหุ้น

🏢 {item['ticker']}

📰 {item['title']}

📄 สรุปข่าว
{item['summary']}

🔗 แหล่งข่าว
{item['link']}
"""

            send(msg)

        time.sleep(300)


if __name__=="__main__":

    threading.Thread(target=bot_loop).start()

    port=int(os.environ.get("PORT",8080))

    app.run(host="0.0.0.0",port=port)
