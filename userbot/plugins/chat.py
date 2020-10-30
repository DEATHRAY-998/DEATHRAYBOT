from telethon import utils

hat_from = event.chat if event.chat else (await event.get_chat()) # telegram MAY not send the chat enity
chat_title = utils.get_display_name(chat_from)