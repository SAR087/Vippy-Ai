import random
from telegram.ext import CommandHandler

msg = ["Hi ! I'm Always Here !", "Hello ? Anyone Here ?", "I'm Online !", "Hello ? Anyone There ?", "Hello, My Friend !"]

def sendmsg(update, context):
    update.effective_message.reply_text(
        random.choice(msg)
    )


__handlers__ = [
    [
        CommandHandler(
            "vippy",
            sendmsg
        )
    ]
]
