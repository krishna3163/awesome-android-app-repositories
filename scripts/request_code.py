"""Step 1 of Telegram login: Request login code."""

import asyncio
import json
from pathlib import Path
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 32027913
API_HASH = "d6e47ac7c7589e239818ac352a738281"
PHONE = "+918210763241"
AUTH_FILE = Path(__file__).resolve().parent / ".auth_state.json"


async def main():
    session = StringSession()
    client = TelegramClient(session, API_ID, API_HASH)
    await client.connect()

    print(f"Sending login code request to {PHONE}...")
    res = await client.send_code_request(PHONE)
    temp_session_str = session.save()

    AUTH_FILE.write_text(
        json.dumps({
            "phone": PHONE,
            "phone_code_hash": res.phone_code_hash,
            "session_str": temp_session_str,
        }),
        encoding="utf-8",
    )
    print("SUCCESS: Code requested. Check your Telegram app or SMS for the verification code.")
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
