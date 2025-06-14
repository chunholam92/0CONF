from flask import Flask, request
import requests

app = Flask(__name__)

# Vervang dit met je eigen waarden
TELEGRAM_BOT_TOKEN = "8134320942:AAEQYzvNWzC5UfInBcNKYnmMjD7o8vFbLi4"
TELEGRAM_CHANNEL_ID = "@ZeroConfusion"

def send_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_data(as_text=True)
    send_message(data)
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
