import logging

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    logging.basicConfig(level=logging.DEBUG)
    executor.start_polling(dp, skip_updates=True)



