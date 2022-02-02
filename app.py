import logging

from aiogram import executor
from loader import dp, db
import filters, handlers
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.info("Starting bot")
    filters.setup(dp)
    await set_default_commands(dp)
    await on_startup_notify(dispatcher)
    logging.info('Creating keywords table')
    if len(db.is_keywords_table_created()) == 0:
        db.create_table_keywords()
    else:
        logging.info('Table already exists')
    logging.info('Creating block list table')
    if len(db.is_block_keywords_table_created()) == 0:
        db.create_table_block_keywords()
    else:
        logging.info('Block list table alredy exists')
    logging.info("Everythis is ok! You can start working")

if __name__ == '__main__':
    logging.info('Starting bot')
    executor.start_polling(dp, on_startup=on_startup)
