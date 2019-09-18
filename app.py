from flask import Flask, request, abort

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

line_bot_api = LineBotApi('hQfjE9b1fjwLta+gWbXVcXuiAlC5UjXCZoyLeb0PsXw1EoTAlfgWs6WejJyMcTcbT63uMfAs9mC1dWBH0Rv3/kIVzmE5xjA/ATBySpXeHNbELZgXFEYwQx2c+IvkH229VwPMaaSXQrn1ckOIIRR2jwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a7494ab2c3e12ab6c390b72fd15550cd')


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
    r = '很抱歉,我只認識甲蟲王者'

    if msg in ['大頭', '渣男']:
        message = ImageSendMessage(
            original_content_url='https://example.com/original.jpg',
            preview_image_url='https://i.imgur.com/A8noZDB.jpg'
            )
        line_bot_api.reply_message(event.reply_token, message)
    
        return

    if msg == '你是誰':
        r = '傑出的閃亮亮'
    elif '愷' in msg:
        r = '天母劉德華？'
    elif msg in ['曾昱瑋', '小狗']:
        r = '約妹帝王'
    elif '讀' in msg:
        r = '怎麼又有人已讀～'
    elif '彥' in msg:
        r = '彥丞該戒煙了'
    elif ['股票', '石油', '退休'] in msg:
        r = '要起飛了嗎'
    elif '敦' in msg:
        r = '董事長好'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()

#test