import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os

BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
APP_TOKEN = os.environ["SLACK_APP_TOKEN"]

app = App(token=BOT_TOKEN)

@app.command("/starbot-ping")
def ping(ack, respond):
    ack()

    respond("Pong! StarBot is online!")

@app.command("/starbot-joke")
def joke(ack, respond):
    ack()

    jokes = [
        "Why do programmers use dark mode? Because light attracts bugs. ",
        "I wrote a program without bugs... unfortunately, it doesn't compile. ",
        "A programmer walks into a bar and orders 1 beer, 0 beers, and -1 beers. ",
        "Python told me it was going to be easy. Spoiler: it wasn't. "
    ]

    respond(random.choice(jokes))

@app.command("/starbot-help")
def help_command(ack, respond):
    ack()

    respond(
        " *StarBot Commands*\n\n"
        " `/starbot-ping` - Check if the bot is online\n"
        " `/starbot-joke` - Get a random joke\n"
        " `/starbot-help` - Show all available commands"
    )

if __name__ == "__main__":
    print(" StarBot is starting...")

    handler = SocketModeHandler(app, APP_TOKEN)

    print(" StarBot is online!")

    handler.start()
