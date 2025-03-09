from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import isCountingCorrect

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message.isdigit():
        return  
    
    user_input = int(user_message)
    username = message.author.display_name

    correct = isCountingCorrect(user_input, username)

    if correct:
        await message.add_reaction("✅")
    else:
        await message.channel.send(f"**{username}** has got it wrong! Starting from 1.")
        await message.add_reaction("❌")


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_read() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()