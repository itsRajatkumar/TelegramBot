from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater("Your Telegram Bot API key", use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Rajat Personal Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/instagram - To get the Instagram URL
	/linkedin - To get the LinkedIn profile URL
	/github - To get GitHub URL
	/Website - To get the WebSite URL
	/end - To End Conversation""")


def github_url(update: Update, context: CallbackContext):
	update.message.reply_text("GitHub Profile =>\
	https://www.github.com/itsrajatkumar")


def instagram_url(update: Update, context: CallbackContext):
	update.message.reply_text("Instagram Profile =>\
	https://www.instagram.com/thisisrajatkumar")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("LinkedIn Profile =>\
	https://www.linkedin.com/in/thisisrajatkumar")


def website_url(update: Update, context: CallbackContext):
	update.message.reply_text("Website Profile =>\
	https://www.rajatkumar.tech")

def end(update: Update, context: CallbackContext):
	update.message.reply_text("Thankyou for using Rajat Kumar Personal bot.")

def thankyou(update: Update, context: CallbackContext):
	update.message.reply_text("Your most welcome")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('Thankyou', thankyou))
updater.dispatcher.add_handler(CommandHandler('EndChat', end))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))



updater.start_polling()
