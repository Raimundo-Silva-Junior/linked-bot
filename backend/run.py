from backend.bots.send_message_bot import SendMessageBot
from backend.config import SESSION
from uuid import UUID
async def run():
        
    send_message_bot = SendMessageBot(SESSION)
    send_message_bot.run("send_first_message")