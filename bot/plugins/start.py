from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

import time

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("start")
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
                  [
                      InlineKeyboardButton("How To Use Me🙄", callback_data="/help")
                  ],
                  [
                      InlineKeyboardButton("Project Channel!", url="https://t.me/hxbots"),
                      InlineKeyboardButton("Support Group", url="https://t.me/HxSupport")
                  ],
                  [  
                      InlineKeyboardButton("Upgrade😀", url="https://t.me/+97tA4_TrzyowMjk1")
                  ]]
        ),
    ),
    # Set the time limit (in seconds)
    time_limit = 60

    # Start the timer
    start_time = time.time()

    # Loop until the time limit is reached
    while (time.time() - start_time) < time_limit:
    # Calculate the time remaining
    time_remaining = time_limit - (time.time() - start_time)
    # Print the time remaining
    print("Time remaining: {:.2f} seconds".format(time_remaining))
    # Wait for 1 second before checking the time again
    time.sleep(1)

    # Time limit has been reached
     print("Time's up!")
