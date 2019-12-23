import giphy_client
from telegram.ext import Updater
from telegram.ext import CommandHandler
import keys

TOKEN = keys.TOKEN
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

GIPHY_API_KEY = keys.GIPHY_API_KEY

def get_nya(api_key):
    api_instance = giphy_client.DefaultApi()
    api_response = api_instance.gifs_random_get(api_key, tag='kitten')
    x = api_response.data.image_original_url
    return(x)

def answer(update, context):
    context.bot.send_animation(chat_id=update.effective_chat.id, animation=get_nya(GIPHY_API_KEY))

nya_handler = CommandHandler('nya', answer)
dispatcher.add_handler(nya_handler)

updater.start_polling()
