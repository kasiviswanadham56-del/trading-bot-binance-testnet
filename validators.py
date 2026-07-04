"""
validators.py

This file validates all user inputs before
sending the order to Binance.
"""


def validate_symbol(symbol):
    """
    Checks whether the trading symbol is valid.
    Example: BTCUSDT
    """
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    return symbol.upper()


def validate_side(side):
    """
    Checks whether order side is BUY or SELL.
    """

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError(
            "Side must be BUY or SELL."
        )

    return side


def validate_order_type(order_type):
    """
    Checks order type.
    """

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity):
    """
    Quantity must be greater than zero.
    """

    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price, order_type):
    """
    LIMIT order requires price.
    MARKET order does not.
    """

    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError(
                "Price is required for LIMIT orders."
            )

        price = float(price)

        if price <= 0:
            raise ValueError(
                "Price must be greater than zero."
            )

        return price

    return None