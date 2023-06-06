from uuid import uuid4

from aiogram import types

from loader import dp, db


@dp.inline_handler()
async def inline_mode(query: types.InlineQuery):
    data = db.q.get(query.from_user.id)
    print(1)
    if data:
        articles = [
            types.InlineQueryResultArticle(
                id=uuid4().hex,
                title=i,
                input_message_content=types.InputMessageContent(
                    message_text=i
                ),
            ) for i in data
        ]
    else:
        articles = [
            types.InlineQueryResultArticle(
                id=uuid4().hex,
                title='Нет сохраннных заметок',
                input_message_content=types.InputMessageContent(
                    message_text='Нет сохраннных заметок'
                ),
            )
        ]
    await query.answer(articles, cache_time=1, is_personal=True)