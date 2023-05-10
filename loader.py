import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import load_config, Config

logging.basicConfig(
    format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
    level=logging.INFO,
)


async def try_connection():
    """
    Function check connection to redis database
    wia setting "some_state" state to first chat (random datas)
    """
    await storage.set_state(chat=1, state='some_state')
    state = await storage.get_state(chat=1)

config: Config = load_config()


# if config.redis.host and config.redis.port:
try:
    
    storage = RedisStorage2(config.redis.host, config.redis.port, db=config.redis.db)
    asyncio.get_event_loop().run_until_complete(try_connection())
    logging.info("Redis database start")
# else:
except Exception as e:
    storage = MemoryStorage()
    logging.info(f"Redis database isn't start because {e}!\nUse built-in database instead")


bot = Bot(token=config.bot.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)
