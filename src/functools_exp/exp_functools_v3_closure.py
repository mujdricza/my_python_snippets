"""
https://www.youtube.com/watch?v=ph2HjBQuI8Y

https://github.com/ArjanCodes/2022-functions

"""
import statistics
from dataclasses import dataclass
from typing import Callable, Protocol

from exchange import Exchange


# Version 3, parametrized
TradingStrategyFunction = Callable[[list[int]], bool]

# closure mechanism
def should_buy_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_buy_avg(prices: list[int]) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] < statistics.mean(list_window)
    return should_buy_avg


def should_sell_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_sell_avg(prices: list[int]) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] > statistics.mean(list_window)
    return should_sell_avg


def should_buy_minmax_closure(max_price: int) -> TradingStrategyFunction:
    def should_buy_minmax(prices: list[int]) -> bool:
        return prices[-1] < max_price
    return should_buy_minmax


def should_sell_minmax_closure(max_price: int) -> TradingStrategyFunction:
    def should_sell_minmax(prices: list[int]) -> bool:
        return prices[-1] >= max_price
    return should_sell_minmax


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
    # advantage: any combination of buy and sell strategies possible
    bot = TradingBot_V2(exchange, should_buy_avg_closure(4), should_sell_minmax_closure(35_000_00))
    bot.run("BTC/USD")


if __name__ == "__main__":

    main_funcional_v2()
    """
    Connecting to Crypto exchange...
    Buying amount 10 in market BTC/USD. 
    """
