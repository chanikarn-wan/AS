import os
import requests

# ดึง URL จากระบบความปลอดภัยของ GitHub
SPACE_URL = os.environ.get("HF_SPACE_URL")

def ping_space():
    if not SPACE_URL:
        print("ข้อผิดพลาด: ไม่พบตัวแปร HF_SPACE_URL กรุณาตั้งค่าใน GitHub Secrets")
        return

    try:
        response = requests.get(SPACE_URL)
        if response.status_code == 200:
            print("🚀 สะกิดสำเร็จ: ระบบ Hugging Face ตื่นอยู่แน่นอน!")
        else:
            print(f"⚠️ ส่งสัญญาณแล้ว แต่ระบบตอบกลับด้วย Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

if __name__ == "__main__":
    ping_space()
