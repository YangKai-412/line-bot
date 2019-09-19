from flask import Flask, request, abort

import random

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('hQfjE9b1fjwLta+gWbXVcXuiAlC5UjXcbT63uMfAs9mC1dWBH0Rv3/kIVzLZgXFEYwQx2c+IvkH229VwPMaaSXQrn1ckOIIRR2jwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('46c390b72fd15550cd')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    i = random.randint(1,6)
    if msg in ['大頭', '暖男']:
        if i == 1:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/A8noZDB.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
        elif i == 2:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/Q808Q6d.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
        elif i == 3:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/zzxL0hw.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
        elif i == 4:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/4RT5VB3.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
        elif i == 5:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/OYkhR9c.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
        elif i == 6:
            message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://i.imgur.com/KpL9rsz.jpg'          
                )
            line_bot_api.reply_message(event.reply_token, message)
    
        return

    if '誰' in msg:
        r = '我是傑出的閃亮亮'
    elif '愷' in msg:
        r = '天母劉德華？'
    elif msg in ['曾昱瑋', '小狗']:
        r = '約妹帝王'
    elif '讀' in msg:
        r = '怎麼又有人已讀～'
    elif '彥' in msg:
        r = '彥丞該戒煙了'
    elif msg in ['股票', '石油', '退休']:
        r = '要起飛了嗎'
    elif '敦' in msg:
        r = '董事長好'
    elif msg in ['靠', '幹', '哀']:
        r = '我不許你這樣說'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()

#test
