from flask import Flask, request
import telegram

app = Flask(__name__)

BOT_TOKEN = "8134320942:AAEQYzvNWzC5UfInBcNKYnmMjD7o8vFbLi4"
CHANNEL_ID = "@ZeroConfusion"
bot = telegram.Bot(token=BOT_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    bericht = data.get("text", "Trade alert ontvangen.")
    bot.send_message(chat_id=CHANNEL_ID, text=bericht)
    return "OK", 200
