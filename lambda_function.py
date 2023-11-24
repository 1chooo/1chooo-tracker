# -*- coding: utf-8 -*-
"""
Date: 2023/11/20
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Version: v0.1.0
"""

import os
import json
import datetime as dt
# import boto3
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import ImageCarouselTemplate
from linebot.models import ImageCarouselColumn
from linebot.models import MessageAction
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def handle_todo_goal(event):

    ready_to_add_todo = False
    todos = []

    event_text = event.message.text

    if event_text == "Got things to do, busy! 🥴":

        reply_messages = [
            TextSendMessage(
                text="Please choose the type of your goal"
            ),
            TemplateSendMessage(
                alt_text='ImageCarousel template',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://hackmd.io/_uploads/BkwF_MI23.jpg',
                            action=MessageAction(
                                label='Add a goal',
                                text='I want to add sth...'
                            )
                        ),
                    ]
                )
            ),
        ]
        
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )
    else:
        return
    
def lambda_handler(event, context):
    # boto3.resource("dynamodb")
    @handler.add(MessageEvent, message=ImageMessage)
    def handle_image_message(event):
        reply_messages = [
            TextSendMessage(
                text=f'We have received your image; however, we won\'t do anything with it now.'
            ),
        ]
            
        line_bot_api.reply_message(
            event.reply_token,
            reply_messages
        )

    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):

        event_text = event.message.text

        handle_todo_goal(event)
        if event_text == "I want to see how busy you really are 👨🏻‍💻":
            reply_messages = [
                TextSendMessage(
                    text=f'Hi, I want to see how busy you really are 👨🏻‍💻'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "I want you to know how extravagant I can be 🤑":
            reply_messages = [
                TextSendMessage(
                    text=f'Hi, I want you to know how extravagant I can be 🤑'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "How rich am I, Huh? 💳":
            reply_messages = [
                TextSendMessage(
                    text=f'Hi, How rich am I, Huh? 💳'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "You know how much weight I pushed today? 😮‍💨":
            reply_messages = [
                TextSendMessage(
                    text=f'You know how much weight I pushed today? 😮‍💨'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "I just want to say something... ✍🏼":
            reply_messages = [
                TextSendMessage(
                    text=f'I just want to say something... ✍🏼'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想看帥哥":
            reply_messages = [
                TextSendMessage(
                    text=f'Test get image from s3 public bucket'
                ),
                TextSendMessage(
                    text=f'This is Hugo!'
                ),
                ImageSendMessage(
                    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "Image":
            reply_messages = [
                TextSendMessage(
                    text=f'Test get image from s3 public bucket'
                ),
                TextSendMessage(
                    text=f'This is Hugo!'
                ),
                ImageSendMessage(
                    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'{event_text}'
                ),
            ]
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )

    try:
        # get X-Line-Signature header value
        signature = event['headers']['x-line-signature']

        # get request body as text
        body = event['body']
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
        }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }