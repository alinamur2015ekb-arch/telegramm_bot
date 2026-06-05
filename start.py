import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from main.hendlers import router
from basadata.basadate import init_db, init_db2
import sys
from aiohttp import web
   

load_dotenv()

bot_token = os.getenv("TOKEN") 


dp = Dispatcher()
dp.include_router(router)


async def handle(request):
    return web.Response(text="Bot is running!")
   
async def main():
    await init_db()
    await init_db2()

    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()
   
    bot = Bot(token=bot_token)

    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
