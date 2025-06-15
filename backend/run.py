from backend.bots.send_message_bot import SendMessageBot
from backend.config import SESSION
async def run():
        
    send_message_bot = SendMessageBot(SESSION)
    send_message_bot.run("send_first_message")