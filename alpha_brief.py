from datetime import datetime

def generate():

    today=datetime.now().strftime("%d %B %Y")

    return f"""
🌅 สรุปข่าวตลาดก่อนเปิด (Morning Alpha Brief)

📅 วันที่ {today}

🧠 ธีมตลาดวันนี้
• การลงทุนด้าน AI และ Data Center ยังคงเป็นธีมหลักของตลาด
• ความต้องการชิป AI ส่งผลบวกต่อกลุ่ม Semiconductor
• บริษัท Cloud ยังคงเพิ่มงบลงทุนโครงสร้างพื้นฐาน AI

🔬 กลุ่มเทคโนโลยี / AI
• NVDA – ความต้องการ GPU สำหรับ AI ยังแข็งแกร่ง
• MSFT – การผสาน AI เข้ากับผลิตภัณฑ์ Cloud
• AVGO – ชิปสำหรับ Data Center และ Networking เติบโต

🛡 Cybersecurity
• CRWD และ PLTR ได้ประโยชน์จากการใช้ AI ในระบบความปลอดภัย

💊 Healthcare
• LLY ได้แรงหนุนจากยอดขายยากลุ่ม GLP-1

⚡ พลังงาน / Data Center
• CEG และ VRT ได้ประโยชน์จากการเติบโตของ Data Center

👀 หุ้นที่ควรจับตา
NVDA / AVGO / PLTR / MSFT / TSM

📊 ธีมการลงทุน
AI Infrastructure
Semiconductor Supply Chain
Energy for Data Centers
"""
