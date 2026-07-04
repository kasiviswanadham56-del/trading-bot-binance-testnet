"""
cli.py

Command Line Interface for Binance Futures Testnet Trading Bot.
"""

import argparse

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

from bot.orders import (
    place_market_order,
    place_limit_order,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading Symbol")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if price is not None:
            print(f"Price      : {price}")

        print("===================================\n")

        if order_type == "MARKET":
            order = place_market_order(
                symbol,
                side,
                quantity,
            )
        else:
            order = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        if not order:
            raise Exception("No response received from Binance.")

        print("\n✅ Order placed successfully!\n")

        print(f"Order ID       : {order.get('orderId')}")
        print(f"Status         : {order.get('status')}")
        print(f"Executed Qty   : {order.get('executedQty')}")
        print(f"Average Price  : {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n===================================")
        print("❌ ORDER FAILED")
        print("===================================")
        print(e)


if __name__ == "__main__":
    main()