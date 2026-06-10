"""
https://www.youtube.com/watch?v=ph2HjBQuI8Y

https://github.com/ArjanCodes/2022-functions

partial functions -> more flexibility, simpler

"""
import statistics
from dataclasses import dataclass
from functools import partial
from typing import Callable, Protocol

from exchange import Exchange


# Version 3, parametrized
TradingStrategyFunction = Callable[[list[int]], bool]


def should_buy_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)


def should_buy_minmax(prices: list[int], max_price: int) -> bool:
    return prices[-1] < max_price


def should_sell_minmax(prices: list[int], max_price: int) -> bool:
    return prices[-1] >= max_price


@dataclass
class TradingBot_V2:
    exchange: Exchange
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.buy_strategy(prices)
        should_sell = self.sell_strategy(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")


def main_funcional_v2() -> None:
    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()

    # create the trading bot and run the bot once
    # partially applied functions
    buy_strategy = partial(should_buy_avg, window_size=4)
    sell_strategy = partial(should_sell_minmax, max_price=35_000_00)
    bot = TradingBot_V2(exchange, buy_strategy, sell_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":

    main_funcional_v2()
    """
    Connecting to Crypto exchange...
    Buying amount 10 in market BTC/USD. 
    """
