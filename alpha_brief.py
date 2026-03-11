from datetime import datetime

def generate():

    today=datetime.now().strftime("%Y-%m-%d")

    return f"""
🌅 MORNING ALPHA BRIEF

Date: {today}

AI / Semiconductor
• NVDA demand driven by hyperscaler AI spending
• TSM production capacity expansion

Cloud / Cybersecurity
• MSFT AI integration continues
• CRWD security demand strong

Healthcare
• LLY obesity drug growth

Key Watchlist
NVDA / AVGO / PLTR / MSFT

Market Themes
• AI Capex
• Semiconductor supply
• Defense tech
"""
