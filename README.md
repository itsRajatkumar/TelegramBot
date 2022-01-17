# TelegramBot

## Requirements
***A Telegram Account:***
  If you don’t have the Telegram app installed just download it from the play store. After downloading create an account using your mobile number just like WhatsApp.

***python-telegram-bot module:***
  Here we will need a module called python-telegram-bot, This library provides a pure Python interface for the Telegram Bot API.
  
## Installation of the module

We can install this module via pip

```pip
pip install python-telegram-bot
```

for conda installation
```pip
conda install -c conda-forge python-telegram-bot
```

## Steps to get Telegram bot and Token

***Step 1:*** After opening Telegram, in the search bar search for **“BotFather”**
</br>
<img  src="https://github.com/itsRajatkumar/TelegramBot/blob/main/Images/bfsearch.JPG"/>


***Step 2:*** Click on the ‘BotFather’ and type **/newbot**
</br>
<img src="https://github.com/itsRajatkumar/TelegramBot/blob/main/Images/newbot.JPG"/>


***Step 3:*** Give a name to your bot. like 'mybot' 'telegram bot'
</br>
<img  src="https://github.com/itsRajatkumar/TelegramBot/blob/main/Images/name.JPG"/>

***Step 4:*** Botfather will ask for its username. Then give a unique name BUT remember the username of your bot must end with the bot, like my_bot, Rajatbot etc.
</br>
<img  src="https://github.com/itsRajatkumar/TelegramBot/blob/main/Images/uniquebot.JPG"/>


***Step 5:*** After giving a unique name and if it gets accepted if not then give other name and then you will get a message like this –
</br>
<img  src="https://github.com/itsRajatkumar/TelegramBot/blob/main/Images/api.JPG"/>
</br>
Here the token value will be different for you, we will use this token in our python code to make changes in our bot and make it just like we want.


## Stepwise implement
***Step 1:*** Importing required libraries
```python

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
```

***Step 2: Define functions for operation***
**Start function:** It will display the first conversation, the message inside it will be sent to the user whenever they press ‘start’ at the very beginning.
```python
updater = Updater("your_own_API_Token got from BotFather", use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Enter the text you want to show to the user whenever they start the bot")
```

**Help function:** It is basically in this function you should add any kind of help the user, All the commands your bot understands, The information related to the bot, etc
```python

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/instagram - To get the Instagram URL
	/linkedin - To get the LinkedIn profile URL
	/github - To get GitHub URL
	/Website - To get the WebSite URL
	/end - To End Conversation""")
```


**Adding some more functionalities to the Bot.**
```python

def github_url(update: Update, context: CallbackContext):
	update.message.reply_text("GitHub Profile =>\https://www.github.com/itsrajatkumar")


def instagram_url(update: Update, context: CallbackContext):
	update.message.reply_text("Instagram Profile =>\https://www.instagram.com/thisisrajatkumar")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("LinkedIn Profile =>\https://www.linkedin.com/in/thisisrajatkumar")


def website_url(update: Update, context: CallbackContext):
	update.message.reply_text("Website Profile =>\https://www.rajatkumar.tech")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
```

***Step 3:*** Adding the Handlers to handle our messages and commands
```python
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
```

***Step 4:*** Running the bot
```python
updater.start_polling()
```
Here whenever we start polling the bot will be active and it will look for any new message sent by any of the users and if it matches the command specified there it will reply accordingly.


## our Bot is ready.
