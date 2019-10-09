#!/usr/bin/python

import argparse

def find_max_profit(prices):
  stock_max = max(prices)
  stock_max_index = prices.index(stock_max)
  if stock_max_index == 0:
    stock_max = max(prices[1:])
    stock_max_index = prices.index(stock_max)
  stock_max_index = prices.index(stock_max)  
  other_stocks = prices[0:stock_max_index]  
  stock_min = min(other_stocks)
  max_profit = stock_max - stock_min
  return max_profit

print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))