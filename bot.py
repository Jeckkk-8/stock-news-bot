from news_engine import fetch_news
from sentiment_engine import analyze
from alpha_brief import generate
from config import TOKEN,CHAT_ID
import requests
import feedparser
import time
import threading
import os
from flask import Flask
from textblob import TextBlob

TOKEN="8692112101:AAHa6X-3bCXpzRRsrbNGFNAM9-W6nLGNaHo"
CHAT_ID="8386698996"

app = Flask(__name__)

@app.route("/")
def home():
    return "Investor Terminal running"

def send_telegram(msg):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url,data={"chat_id":CHAT_ID,"text":msg})

def bot_loop():

    print("Investor Terminal started")

    while True:

news = fetch_news()

        time.sleep(300)  # เช็คข่าวทุก 5 นาที
if __name__ == "__main__":

    threading.Thread(target=bot_loop).start()

    port=int(os.environ.get("PORT",10000))

    app.run(host="0.0.0.0",port=port)
