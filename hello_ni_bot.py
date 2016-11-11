"""This module does SlackClient Service to define who is Ni"""
import time
from slackclient import SlackClient


BOT_TOKEN = "<YOUR TOKEN>"
CHANNEL_NAME = "<YOUR CHANEL NAME>"
BOT_NAME = "hello_ni_bot"

def main():
    """Send the message to the channel of Slack which you define"""
    # Create the slackclient instance
    slack_client = SlackClient(BOT_TOKEN)
    # Connect to slack
    if slack_client.rtm_connect():
        # Send first message
        slack_client.rtm_send_message(CHANNEL_NAME, "NiBai is a kind of Ni.")
        while True:
            # Read latest messages
            for slack_message in slack_client.rtm_read():
                message = slack_message.get("message2")
                user = slack_message.get(BOT_NAME)
                if not message or not user:
                    continue
                slack_client.rtm_send_message(
                    CHANNEL_NAME, "<@{}> wrote something...".format(user)
                )
            # Sleep for half a second
            time.sleep(0.5)

if __name__ == '__main__':
    main()
