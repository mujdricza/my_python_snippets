"""
https://www.youtube.com/watch?v=ph2HjBQuI8Y

https://github.com/ArjanCodes/2022-functions

"""
import statistics
from dataclasses import dataclass
from typing import Callable, Protocol

from exchange import Exchange


# Version 1
class TradingStrategy(Protocol):
    """Trading strategy that decides whether to buy or sell, given a list of prices."""

    def should_buy(self, prices: list[int]) -> bool:
        raise NotImplementedError()

    def should_sell(self, prices: list[int]) -> bool:
        raise NotImplementedError()


class AverageTradingStrategy:
    """Trading strategy based on price averages."""

    def should_buy(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)


class MinMaxTradingStrategy:
    """Trading strategy based on price minima and maxima."""
    def should_buy(self, prices: list[int]) -> bool:
        # buy if it's below $32,000
        return prices[-1] < 32_000_00

    def should_sell(self, prices: list[int]) -> bool:
        # sell if it's at least $32,000
        return prices[-1] >= 32_000_00


@dataclass
class TradingBot:
    """Trading bot that connects to a crypto exchange and performs trades."""

    exchange: Exchange
    trading_strategy: TradingStrategy

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)
        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")


def main_classic() -> None:
    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()

    # create the trading strategy
    trading_strategy = MinMaxTradingStrategy()

    # create the trading bot and run the bot once
    bot = TradingBot(exchange, trading_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":
    main_classic()
    """
    Connecting to Crypto exchange...
    Selling amount 10 in market BTC/USD.
    """
