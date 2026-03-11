from datetime import datetime
from news_engine import fetch_news

def generate():

    today=datetime.now().strftime("%d %B %Y")

    news=fetch_news()

    ai=0
    chip=0
    cloud=0
    energy=0

    for n in news:

        text=n["summary"].lower()

        if "ai" in text:
            ai+=1

        if "chip" in text or "semiconductor" in text:
            chip+=1

        if "cloud" in text:
            cloud+=1

        if "energy" in text or "power" in text:
            energy+=1

    themes=[]

    if ai>0:
        themes.append("• AI Infrastructure")

    if chip>0:
        themes.append("• Semiconductor Supply Chain")

    if cloud>0:
        themes.append("• Cloud Computing")

    if energy>0:
        themes.append("• Energy for Data Centers")

    theme_text="\n".join(themes)

    return f"""
🌅 สรุปข่าวตลาดก่อนเปิด

📅 {today}

🧠 ธีมตลาดวันนี้
{theme_text}

👀 หุ้นที่ควรจับตา
NVDA / AVGO / PLTR / MSFT / TSM
"""
