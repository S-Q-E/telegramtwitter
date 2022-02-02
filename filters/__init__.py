from aiogram import Dispatcher
from .group_chat import IsGroup
from .admin_filter import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
