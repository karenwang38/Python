from flask import Flask, request, abort
from py_translator import Translator

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('3R6rWttchztIO20fTxeS5BNrVMFmcgs3USaRiw4RH4hX3o2oGurVBYk57TdXU3rH5d9b4xjfISEqHOXgyQKaHKDIPJkK0goAQlXjctJljFBsjDssWTBuWFiLX336IDT9SyRWywofka81TUuaGtDkpgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fcfaa2da0689e66776f2b6b68ea2b7b7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    #
    translator = Translator()
    print("before translate :", event.message.text)
    translations = translator.translate(text = event.message.text, dest='zh-tw').text
    #Translator().translate(text='Hello my friend', dest='es').text
    #translations = translator.translate(event.message.text, dest='zh-tw')
    print("translation =", translations)

    event.message.text = translations
    print("after translate :", event.message.text)

    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

    '''
    music_link = "https://www.youtube.com/watch?v=IRwFrOKpRbc"

    print("event.message.text =", event.message.text)
    if event.message.text == 'music':
        message = TextSendMessage(text = music_link)
    else:
        message = TextSendMessage(text=event.message.text)
        #message = TextSendMessage(text='hello world')
    line_bot_api.reply_message(event.reply_token, message)
    '''

    '''
    # parrot
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)
    '''




import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
