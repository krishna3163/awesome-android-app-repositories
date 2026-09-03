import asyncio
from unittest.mock import AsyncMock, patch
import pytest
from src.telegram.client import TelegramAuthError, TelegramClient


def test_telegram_client_unauthorized_raises_auth_error():
    """Verify that an unauthorized session raises TelegramAuthError."""
    async def _run():
        client = TelegramClient(api_id=12345, api_hash="fakehash", session_string="")

        with patch("src.telegram.client._TelegramClient") as mock_telethon:
            mock_instance = AsyncMock()
            mock_instance.connect = AsyncMock()
            mock_instance.is_user_authorized = AsyncMock(return_value=False)
            mock_instance.disconnect = AsyncMock()
            mock_telethon.return_value = mock_instance

            with pytest.raises(TelegramAuthError, match="not authorized or has expired"):
                await client.connect()

    asyncio.run(_run())


def test_telegram_client_invalid_session_string_raises_auth_error():
    """Verify that an invalid session string raises TelegramAuthError."""
    async def _run():
        client = TelegramClient(api_id=12345, api_hash="fakehash", session_string="not-a-valid-session")
        with pytest.raises(TelegramAuthError, match="invalid or connection failed"):
            await client.connect()

    asyncio.run(_run())
