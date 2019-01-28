from googletrans import Translator

class MyBotHandler(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''Your description of the bot'''

    def handle_message(self, message, bot_handler):
        translator = Translator()

        print(message['full_content'])

        sender_addr = message['display_recipient'][1]['email']
        print(sender_addr)
        if(sender_addr == 'sunilkv20164012@gmail.com'):
            reply = translator.translate(message['full_content'], dest='en')
            #bot_handler.send_reply(message, reply.text)

            bot_handler.send_message(dict(
            type='private', # can be 'stream' or 'private'
            to='saurabh4104@gmail.com', # either the stream name or user's email
            subject='private message to saurabh', # message subject
            content=reply.text,))

        else:
            reply = translator.translate(message['full_content'], dest='hi')
            #bot_handler.send_reply(message, reply.text)

            bot_handler.send_message(dict(
            type='private', # can be 'stream' or 'private'
            to='sunilkv20164012@gmail.com', # either the stream name or user's email
            subject='private message to sunil', # message subject
            content=reply.text,)) # content of the sent message


handler_class = MyBotHandler
