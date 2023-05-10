from aiogram import types
from loader import dp
import aiohttp


@dp.message_handler(commands=["dog"], state="*")
async def send_dog_picture(message: types.Message):
    """
    Handle messages when user sends the "/dog" command.
    Sends a random dog picture to the user.

    :param message: aiogram.types.Message - The message object containing the command.
    :return: None
    """
    async with aiohttp.ClientSession() as session:
        async with session.get("https://random.dog/woof.json") as response:
            picture = await response.json()
    await message.answer_photo(photo=picture["url"])
