import os
import time
import re

from api.wiapi import WiApi
from config.config_manager import *
from slackclient import SlackClient

config = config_man('bot.ini')
# get bot id from environment
BOT_ID = config.BOT_ID
token = config.SLACK_BOT_TOKEN
AT_BOT = "<@" + BOT_ID + ">"

ASK_COMMAND = "vsts"

slack_client = SlackClient(token)
vsts_api = WiApi()


def handle_command(command, channel):
    """
    Receives commands directed at the bot and determines if they are valid commands.
    If so, then acts on the commands.
    If not, returns back what it needs for clarification.
    """
    response = "For start, ask me about *" + ASK_COMMAND + "*"
    if command.startswith(ASK_COMMAND):
        response = "Good news, it's new vsts command, which can provide you information about work items"
    elif "wi#" in command:
        wi_id = re.search("wi#(\d+)", command).group(1)
        try:
            wi = vsts_api.get_by_id(wi_id)
            response = wi.url
        except ValueError as val_err:
            response = str(val_err)
        except:
            pass
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
    return


def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API is an events firehouse.
    THis parsing function returns None unless a message is directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                output_text = output['text']
                if AT_BOT in output_text:
                    return output_text.split(AT_BOT)[1].strip().lower(), output['channel']
    return None, None


def wait_message():
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("vsts bot started up")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack params")


if __name__ == "__main__":
    wait_message()
