import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Đọc từ environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

def send_daily_standup():
    if not SLACK_BOT_TOKEN or not CHANNEL_ID:
        print("❌ Thiếu SLACK_BOT_TOKEN hoặc SLACK_CHANNEL_ID")
        return
    
    message = f"""
*🌞 Daily Standup - {datetime.now().strftime('%Y-%m-%d')}*
1. Hôm qua bạn đã làm gì?
2. Hôm nay bạn định làm gì?
3. Có cản trở nào không?

👉 Vui lòng reply trực tiếp vào thread này.
    """
    
    res = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "channel": CHANNEL_ID,
            "text": message
        }
    )
    print(res.json())

if __name__ == "__main__":
    send_daily_standup()