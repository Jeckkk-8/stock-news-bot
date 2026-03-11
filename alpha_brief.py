from datetime import datetime

def generate():

    today=datetime.now().strftime("%d %B %Y")

    return f"""
🌅 สรุปข่าวตลาดก่อนเปิด

📅 {today}

🧠 ธีมตลาดวันนี้
• การลงทุนด้าน AI และ Data Center ยังคงเป็นแรงขับเคลื่อนหลัก
• ความต้องการชิป AI เพิ่มขึ้นในกลุ่ม Semiconductor
• Cloud และ Cybersecurity เติบโตต่อเนื่อง

👀 หุ้นที่ควรจับตา
NVDA / AVGO / PLTR / MSFT / TSM

📊 ธีมการลงทุน
AI Infrastructure
Semiconductor Supply Chain
Energy for Data Centers
"""
