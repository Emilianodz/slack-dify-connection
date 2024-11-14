# slack_integration/slack_client.py
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

slack_token = os.getenv('SLACK_BOT_TOKEN')
client = WebClient(token=slack_token)

def send_message(channel, text):
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return response
    except SlackApiError as e:
        print(f"Error al enviar mensaje: {e.response['error']}")
        return None
