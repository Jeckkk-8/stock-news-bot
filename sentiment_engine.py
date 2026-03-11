from textblob import TextBlob

def analyze(text):

    score=TextBlob(text).sentiment.polarity

    if score>0.15:
        return "🟢 Bullish"

    elif score<-0.15:
        return "🔴 Bearish"

    return "🟡 Neutral"
