import requests
import os
from datetime import datetime

SLACK_BOT_TOKEN = os.getenv("xoxb-7808228366695-9304782153152-YQtvYKamZxkZ9ohOQJvqhqTK")
CHANNEL_ID = os.getenv("C098QCKTMH7")  # Ex: C012ABC345

def send_daily_standup():
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
