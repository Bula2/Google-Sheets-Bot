# Библиотеки
import logging
import bot_config.data as data
from aiogram import Bot, Dispatcher, types, executor
import bot_config.keyboard
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Объект бота
bot = Bot(data.token, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())
#dp.middleware.setup(LoggingMiddleware())
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot_config.keyboard.Buttoms(dp, bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)