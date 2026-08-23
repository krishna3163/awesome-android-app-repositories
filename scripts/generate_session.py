"""Helper script to interactively generate a Telethon StringSession.

Run this script locally to log in to Telegram and output a TELEGRAM_SESSION_STRING
that can be safely stored as an environment variable or GitHub Secret.

Usage:
    python scripts/generate_session.py
"""

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession


async def generate_session() -> None:
    print("=" * 60)
    print(" Telegram StringSession Generator")
    print("=" * 60)
    print("You will need your API ID and API Hash from https://my.telegram.org\n")

    api_id_input = input("Enter TELEGRAM_API_ID: ").strip()
    if not api_id_input.isdigit():
        print("❌ Error: API ID must be a numeric integer.")
        return
    api_id = int(api_id_input)

    api_hash = input("Enter TELEGRAM_API_HASH: ").strip()
    if not api_hash:
        print("❌ Error: API Hash cannot be empty.")
        return

    print("\nConnecting to Telegram... (Follow the prompts for phone & login code)")
    client = TelegramClient(StringSession(), api_id, api_hash)
    await client.start()

    session_string = client.session.save()
    print("\n" + "=" * 60)
    print("✅ SUCCESS! Your session string has been generated:")
    print("=" * 60)
    print(session_string)
    print("=" * 60)
    print("\n⚠️ IMPORTANT:")
    print("1. Copy this string and add it to your .env as TELEGRAM_SESSION_STRING=...")
    print("2. Add it as a GitHub Secret under Settings > Secrets > Actions.")
    print("3. NEVER share this string publicly or commit it to Git repository!\n")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(generate_session())
