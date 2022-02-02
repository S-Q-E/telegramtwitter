from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Get information about commands"),
        types.BotCommand("add", "Set keywords"),
        types.BotCommand("del", "Delete keywords"),
        types.BotCommand("list", "Show list of keywords"),
        types.BotCommand("bladd", "Add keywords to block list"),
        types.BotCommand("bllist", "Show block list of keywords"),
        types.BotCommand("bldel", "Delete keywords from block list"),
    ])


