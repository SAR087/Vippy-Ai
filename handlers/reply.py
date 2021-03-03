from telegram.ext import MessageHandler, Filters
from helpers import reply as r


def reply(update, context):
    try:
        msg = r(

update.effective_message.text

            )
        context.bot.send_chat_action(update.effective_chat.id, "typing")
        update.effective_message.reply_text(
          msg
)
    except:
        pass


__handlers__ = [
    [
        MessageHandler(
            Filters.text & Filters.reply,
            reply
        )
    ]
]
