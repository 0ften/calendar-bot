import time
from slackclient import SlackClient

BOT_TOKEN = <YOUR TOKEN>
CHANNEL_NAME = <YOUR CHANEL NAME>
BOT_NAME = "hello_ni_bot"
def main():
    # Create the slackclient instance
    sc = SlackClient(BOT_TOKEN)

    # Connect to slack
    if sc.rtm_connect():
        # Send first message
        sc.rtm_send_message(CHANNEL_NAME, "NiBai is a kind of Ni.")
        while True:
            # Read latest messages
            for slack_message in sc.rtm_read():
                message = slack_message.get("message2")
                user = slack_message.get(BOT_NAME)
                if not message or not user:
                    continue
                sc.rtm_send_message(CHANNEL_NAME, "<@{}> wrote something...".format(user))
            # Sleep for half a second
            time.sleep(0.5)

if __name__ == '__main__':
    main()
