from aiogram import types

from loader import dp, db


@dp.message_handler()
async def save(message: types.Message):

    db.add(message.from_user.id, message.text)
    await message.answer(f'Save note with text: <i>{message.text}</i>', parse_mode="HTML")


# @dp.message_handler()
# async def test(message: types.Message):
#     await message.answer('test')
