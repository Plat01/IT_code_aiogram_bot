from aiogram import types
from loader import dp
from utils import ceaser_cipher, decipher
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=["cipher"], state="*")
async def set_cipher_state_command_handler(message: types.Message, state: FSMContext):
    """
    Sets the user's state to 'ciphering' using the given FSMContext object.

    :param message: The message object representing the user's message.
    :param state: The FSMContext object for storing the user's state.
    """
    await state.set_state(state="ciphering")
    current_state = await state.get_state()
    await message.answer(f"Your current mode is {current_state}")


@dp.message_handler(commands=["decipher"], state="*")
async def set_cipher_state_command_handler(message: types.Message, state: FSMContext):
    """
    Sets the user's state to 'deciphering' using the given FSMContext object.

    :param message: The message object representing the user's message.
    :param state: The FSMContext object for storing the user's state.
    """
    await state.set_state(state="deciphering")
    current_state = await state.get_state()
    await message.answer(f"You in {current_state} mode now")


@dp.message_handler(state="ciphering")
async def handle_ciphering_messages(message: types.Message):
    """
    Handle messages when user is in "ciphering" state.
    Encrypts the message using a Caesar cipher with the user's ID as the key.

    :param message: aiogram.types.Message - The message to be encrypted.
    :return: None
    """
    text = ceaser_cipher(message.text, key=message.from_id)
    await message.answer(message.text)
    await message.answer(text)


@dp.message_handler(state="deciphering")
async def handle_deciphering_messages(message: types.Message, state: FSMContext):
    """
    Handle messages when user is in "deciphering" state.
    Decrypts the message using a Caesar cipher with the forwarded message's sender ID as the key.
    And set None state after all.

    :param message: aiogram.types.Message - The message to be decrypted.
    :param state: aiogram.dispatcher.storage.FSMContext - The FSM context object.
    :return: None
    """
    text = decipher(message.text, key=message.forward_from.id)
    await message.answer(text)
    await state.set_state(state=None)

