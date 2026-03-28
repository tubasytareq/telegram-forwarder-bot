from telethon import TelegramClient, events
import asyncio

api_id = 37384127
api_hash = '9f9f0a19aeee055c06bdc6ed5e5a5b09'

source = 'Nablusgheer'       # القناة التي تريد نسخ منها
target = 'shamaleldafa'      # القناة التي تريد النشر فيها

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source))
async def handler(event):
    await client.send_message(target, event.message)

async def main():
    await client.start()
    print("البوت يعمل الآن 🔥")
    await client.run_until_disconnected()

asyncio.run(main())