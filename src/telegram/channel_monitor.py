"""Monitor Telegram channels for new messages.

Reads the last processed message ID from processed-messages.json and
fetches only newer messages using Telethon's min_id parameter.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from telethon.tl.types import Message

from src.telegram.client import TelegramClient

logger = logging.getLogger("telegram-sync")


@dataclass
class ChannelMessages:
    """Messages fetched from a Telegram channel."""

    channel: str
    messages: list[Message] = field(default_factory=list)
    latest_message_id: int = 0


async def fetch_new_messages(
    client: TelegramClient,
    channel_username: str,
    last_processed_id: int = 0,
    limit: int | None = None,
) -> ChannelMessages:
    """Fetch new messages from a Telegram channel.

    Only retrieves messages with ID greater than last_processed_id.

    Args:
        client: Connected TelegramClient instance.
        channel_username: Channel username without '@' (e.g. 'popMODS').
        last_processed_id: The last processed message ID. Only messages
            newer than this will be fetched. 0 means fetch recent messages.
        limit: Maximum number of messages to fetch per call.

    Returns:
        ChannelMessages with the list of new Message objects and the
        latest message ID for updating the processed-messages tracker.
    """
    result = ChannelMessages(channel=channel_username)

    try:
        entity = await client.client.get_entity(channel_username)
    except Exception as exc:
        logger.error("[ERROR] Could not resolve channel @%s: %s", channel_username, exc)
        return result

    logger.info("[INFO] Checking @%s (last processed: %d)", channel_username, last_processed_id)

    messages: list[Message] = []
    try:
        async for message in client.client.iter_messages(
            entity,
            limit=limit,
            min_id=last_processed_id,
        ):
            if isinstance(message, Message) and message.text:
                messages.append(message)
    except Exception as exc:
        logger.error("[ERROR] Failed to fetch messages from @%s: %s", channel_username, exc)
        return result

    # Reverse to process in chronological order (oldest first)
    messages.reverse()

    result.messages = messages
    if messages:
        result.latest_message_id = max(m.id for m in messages)
    else:
        result.latest_message_id = last_processed_id

    logger.info("[INFO] Found %d new messages from @%s", len(messages), channel_username)
    return result
