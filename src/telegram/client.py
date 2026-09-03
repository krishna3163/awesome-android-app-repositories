"""Telethon client wrapper with session string support.

The client connects using a session string (no .session file needed),
which is ideal for headless environments like GitHub Actions.
"""

from __future__ import annotations

import logging
from types import TracebackType

from telethon import TelegramClient as _TelegramClient
from telethon.sessions import StringSession

logger = logging.getLogger("telegram-sync")


class TelegramAuthError(Exception):
    """Raised when Telegram session credentials or authorization fail."""
    pass


class TelegramClient:
    """Managed Telegram client that connects via session string.

    Usage::

        async with TelegramClient(api_id, api_hash, session_string) as client:
            # client is connected and ready
            ...
    """

    def __init__(
        self,
        api_id: int,
        api_hash: str,
        session_string: str = "",
    ) -> None:
        self._api_id = int(str(api_id).strip()) if api_id else 0
        self._api_hash = str(api_hash).strip().strip("'\"")
        # Sanitize session string: remove whitespace, newlines, quotes that might come from CI secrets
        cleaned = str(session_string).strip().strip("'\"").replace("\r", "").replace("\n", "").replace(" ", "")
        self._session_string = cleaned
        self._client: _TelegramClient | None = None

    @property
    def client(self) -> _TelegramClient:
        """Return the underlying Telethon client.

        Raises:
            RuntimeError: If the client is not connected.
        """
        if self._client is None:
            raise RuntimeError("Telegram client is not connected. Use 'async with' context manager.")
        return self._client

    async def connect(self) -> None:
        """Connect to Telegram."""
        try:
            session = StringSession(self._session_string)
            self._client = _TelegramClient(session, self._api_id, self._api_hash)
            await self._client.connect()
        except TelegramAuthError:
            raise
        except Exception as err:
            logger.error("Failed to initialize Telegram client: %s", err)
            raise TelegramAuthError(f"Telegram session string is invalid or connection failed: {err}") from err

        if not await self._client.is_user_authorized():
            logger.error("Telegram session is not authorized. Please regenerate the session string.")
            raise TelegramAuthError("Telegram session is not authorized or has expired.")
        logger.info("[INFO] Connected to Telegram")

    async def disconnect(self) -> None:
        """Disconnect from Telegram."""
        if self._client:
            await self._client.disconnect()
            self._client = None
            logger.info("[INFO] Disconnected from Telegram")

    async def __aenter__(self) -> TelegramClient:
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.disconnect()
