from config import TOKEN_API
from aiogram import Bot, types, Dispatcher, executor

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def get_user_info(message: types.Message):
    await bot.send_message(message.from_user.id, message.from_user.full_name)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
