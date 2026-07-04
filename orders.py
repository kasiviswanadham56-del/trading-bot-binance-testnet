from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    client = get_client()

    logger.info(f"MARKET | {symbol} | {side} | {quantity}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
    )

    return order


def place_limit_order(symbol, side, quantity, price):

    client = get_client()

    logger.info(
        f"LIMIT | {symbol} | {side} | {quantity} | {price}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC",
    )

    return order