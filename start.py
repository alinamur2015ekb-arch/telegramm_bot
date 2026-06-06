import asyncio
import os
import sys
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiohttp import web
from hendlers import router as hendlers_router
from rouetr_anket import router as anket_router
from router_anket_join import router as join_router
from router import router as media_router
from basadata import init_db, init_db2
import asyncio
import aiohttp


async def pinger():
    """Функция, которая сама пингует сайт бота, чтобы он не спал"""
    await asyncio.sleep(10) # Даем боту сначала запуститься
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get('https://telegramm-bot-rpin.onrender.com') as response:
                    print(f"Пинг выполнен! Статус: {response.status}")
            except Exception as e:
                print(f"Ошибка пинга: {e}")
            await asyncio.sleep(600)

load_dotenv()
bot_token = os.getenv("TOKEN")

dp = Dispatcher()
dp.include_routers(
    hendlers_router,
    anket_router,
    join_router,
    media_router
)

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    await init_db()
    await init_db2()

    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 10000)
    await site.start()

    bot = Bot(token=bot_token)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
