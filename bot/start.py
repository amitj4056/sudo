from googletrans import Translator

class MyBotHandler(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''Your description of the bot'''

    def handle_message(self, message, bot_handler):
    	print(message['full_content'])
    	translator = Translator()
    	reply = translator.translate(message['full_content'], dest='en')
    	#bot_handler.send_reply(message, reply.text)

    	bot_handler.send_message(dict(
	    type='private', # can be 'stream' or 'private'
	    to='sunilkv20164012@gmail.com', # either the stream name or user's email
	    subject='private message by bot', # message subject
	    content=reply.text, # content of the sent message
	))

handler_class = MyBotHandler
