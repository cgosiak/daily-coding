"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
from typing import List


def optimal_stock_profit(stock_list: List[int]) -> int:
    maximum_profit: int = 0
    minimum_purchase: int = stock_list[0]

    for i in range(1, len(stock_list)):
        current_stock_price: int = stock_list[i]
        if current_stock_price < minimum_purchase:
            minimum_purchase = current_stock_price
        else:
            profit: int = current_stock_price - minimum_purchase
            if profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit


print(optimal_stock_profit([9, 11, 8, 5, 7, 10]))
