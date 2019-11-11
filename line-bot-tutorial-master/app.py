from flask import Flask, request, abort
from googletrans import Translator
#from py_translator import Translator
import random

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

#database
location_list = {'台北市':{'台北101':['Taipei 101 will hold a fireworks show during the New Year\'s Eve','跨年的時候台北101會舉辦煙火秀'],
                          '國立故宮博物院':['National plalce museum is one of the eight scenic spots in Taiwan','國家宮殿博物館是台灣八大景區之一'],
                          '陽明山國家公園':['It is most comfortable to have a hot spring here in winter!','冬天這裡有溫泉最舒服'],
                          '西門町':['Here is where young people like to come.','這裡是年輕人喜歡來的地方。'],
                          '中正紀念堂':['In addition to people’s leisure, it is often a venue for large-scale arts and cultural events, often holding exhibitions.','除了人們的休閒活動外，它還經常舉辦大型藝術和文化活動，經常舉辦展覽。']},
                '新北市':{'九份':['Jiufen taro ball  is very delicious!','九份芋圓非常好吃'],
                        '野柳風景特定區':['One of the premier destinations in northern Taiwan, Yehliu Geopark is home to a number of unique geological formations including the iconic "Queen\'s Head"','野柳風景特定區是台灣北部的首要目的地之一，擁有眾多獨特的地質構造，包括標誌性的“女王頭”'],
                        '艋舺龍山寺':['It is most comfortable to have a hot spring here in winter!','冬天這裡有溫泉最舒服'],
                        '十分瀑布':['Shihfen Waterfall falls about 20 meters high, very spectacular','十分瀑布高約20米，非常壯觀'],
                        '金瓜石':['JinGuaShih shrine, here is a must for photography enthusiasts','金瓜石神社啦，這裡可是攝影愛好者的必來之處']}}
City_list = list(location_list.keys())

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

    
    #location english sentence
    City_idx = random.choice(range(len(location_list)))

    Position_idx = random.choice(range(len(location_list[City_list[City_idx]])))
    position_list = list(location_list[City_list[City_idx]].keys())


    Text = ["你要去"+City_list[City_idx]+"的"+position_list[Position_idx]+"\n""你要學的英文是： "
            +location_list[City_list[City_idx]][position_list[Position_idx]][0]
            +"("+location_list[City_list[City_idx]][position_list[Position_idx]][1]+")"]
    print(Text[0])
    message = TextSendMessage(text=Text[0])
    line_bot_api.reply_message(event.reply_token, message)




    '''
    # 2 Translator
    translator = Translator()
    print("before translate :", event.message.text)
    lanDetection = translator.detect(event.message.text)
    print("lanDetection =", lanDetection)
    if lanDetection.lang == 'zh-CN':
        translations = translator.translate(text = event.message.text, dest='en').text
    else:
        translations = translator.translate(text = event.message.text, dest='zh-tw').text


    #Translator().translate(text='Hello my friend', dest='es').text
    #translations = translator.translate(event.message.text, dest='zh-tw')
    print("translation =", translations)

    event.message.text = translations
    print("after translate :", event.message.text)

    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)
    '''




    '''
    # music replay
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

