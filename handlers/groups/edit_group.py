
from twint.tweet import Tweet
from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import AdminFilter, IsGroup
from loader import dp, bot, db
from utils.twetter_scraper import get_tweet


@dp.message_handler(Command('help', prefixes='!/'))
async def help_command(message: types.Message):
    await message.answer(f"Commands:\n"
                         f" /add\n"
                         f" For example /add defi, farmSupports any number of the keywords\n\n"
                         f"/del\n"
                         f" Deletes filters from the watchlist associated with the number\n\n"
                         f"/list\n"
                         f"Shows current filters with their number\n\n"
                         f"/bladd\n"
                         f" Adds the word to blacklis\n\n"
                         f"/bldel "
                         f"removes word from blacklist\n\n"
                         f"/bllist\n"
                         f" Show words in blacklist")


@dp.message_handler(IsGroup(), Command('add', prefixes='!/'), AdminFilter())
async def set_keywords(message: types.Message):
    keyword = message.get_args()
    chat_id = message.chat.id
    if keyword is not None:
        db.add_keyword(keyword, chat_id)
        await message.answer(f'Keyword {keyword} added to keyword list')
    else:
        await message.answer("You didn't enter anything")


@dp.message_handler(IsGroup(), Command('list', prefixes='!/'))
async def list_of_keywords(message: types.Message):
    keyword_list = db.select_all_keywords()
    for row in keyword_list:
        await message.answer(f"#{row[0]}\n{row[1]}\n")


@dp.message_handler(IsGroup(), Command('del', prefixes='!/'))
async def delete_keywords(message: types.Message):
    keyword_id = message.get_args()
    db.delete_keyword(keyword_id)
    await message.answer(f"Keyword with id {keyword_id} deleted")


@dp.message_handler(IsGroup(), Command('bladd', prefixes='!/'), AdminFilter())
async def set_block_keywords(message: types.Message):
    chat_id = message.chat.id
    block_keyword = message.get_args()
    if block_keyword is not None:
        db.add_block_keyword(block_keyword, chat_id)
        await message.answer(f"{block_keyword} was add to block list")
    else:
        await message.answer("You didn't enter any word")


@dp.message_handler(IsGroup(), Command('bllist', prefixes='!/'))
async def block_list_of_keywords(message: types.Message):
    block_keyword_list = db.select_all_block_keywords()
    chat_id = message.chat.id
    for row in block_keyword_list:
        await message.answer(f"#{row[0]} \n{row[1]} \n")


@dp.message_handler(Command('bldel', prefixes='!/'))
async def delete_block_keyword(message: types.Message):
    keyword_id = message.get_args()
    db.delete_from_block_list(keyword_id)
    await message.answer(f"Keyword with {keyword_id} removed from block list")


@dp.message_handler(Command('get_tweet'))
async def sending_tweets(message:types.Message):
    keywords_list = db.select_all_keywords()
    await message.answer(keywords_list)
    tweets = get_tweet(keywords_list, 100)
    for new_tweet in reversed(tweets):
        await message.answer(f"Working combinations:\n{[word[1] for word in keywords_list]}\n"
                             f"Name: {new_tweet['name']}\n\n"
                             f"User_name: {new_tweet['username']}\n\n"
                             f"URL of post: {new_tweet['link']}\n"
                             f"Tweet:  {new_tweet['tweet']}\n\n"
                             f"Links in tweet: {new_tweet['urls']}")
