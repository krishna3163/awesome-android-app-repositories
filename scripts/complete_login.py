"""Step 2 of Telegram login: Complete login with OTP code."""

import asyncio
import json
import sys
from pathlib import Path
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession

API_ID = 32027913
API_HASH = "d6e47ac7c7589e239818ac352a738281"
TWO_FACTOR_PIN = "3163019"
AUTH_FILE = Path(__file__).resolve().parent / ".auth_state.json"
ENV_FILE = Path(__file__).resolve().parents[1] / ".env"


async def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/complete_login.py <OTP_CODE>")
        return

    code = sys.argv[1].strip()

    if not AUTH_FILE.exists():
        print("Error: .auth_state.json not found. Run request_code.py first.")
        return

    auth_data = json.loads(AUTH_FILE.read_text(encoding="utf-8"))
    phone = auth_data["phone"]
    phone_code_hash = auth_data["phone_code_hash"]
    session_str = auth_data["session_str"]

    session = StringSession(session_str)
    client = TelegramClient(session, API_ID, API_HASH)
    await client.connect()

    try:
        await client.sign_in(phone=phone, code=code, phone_code_hash=phone_code_hash)
    except SessionPasswordNeededError:
        print("2FA required, submitting password/PIN...")
        await client.sign_in(password=TWO_FACTOR_PIN)

    final_session_string = session.save()
    print("=" * 60)
    print("SUCCESSFULLY LOGGED IN!")
    print("=" * 60)
    print(f"SESSION_STRING: {final_session_string}")
    print("=" * 60)

    # Update .env
    if ENV_FILE.exists():
        content = ENV_FILE.read_text(encoding="utf-8")
        if "TELEGRAM_SESSION_STRING=" in content:
            lines = []
            for line in content.splitlines():
                if line.startswith("TELEGRAM_SESSION_STRING="):
                    lines.append(f"TELEGRAM_SESSION_STRING={final_session_string}")
                else:
                    lines.append(line)
            ENV_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print("Updated .env with TELEGRAM_SESSION_STRING.")

    # Clean up auth file
    AUTH_FILE.unlink(missing_ok=True)
    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
