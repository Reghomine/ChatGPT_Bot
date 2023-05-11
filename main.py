import openai 
from aiogram import Bot, Dispatcher, executor, types


openai.api_key = 'your ChatGPT token'
openai.Model.list()


API_TOKEN = 'Your bot token'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'💡 Добро пожаловать, {message.from_user.first_name}!')


@dp.message_handler()
async def answer(message: types.Message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=1,
        max_tokens=2048,
        top_p=0.7,
        frequency_penalty=0,
    )
    await message.reply(response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp)