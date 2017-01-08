'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (ie, buy one and sell one share 
of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
Difficulty: Easy-Medium
'''

def max_profit(stock_prices):
	if len(stock_prices) < 2:
		return 0
	profit = 0
	for i in xrange (1, len(stock_prices)):
		current_price = stock_prices[i-1]
		next_price = stock_prices[i]
		if current_price < next_price:
			profit += (next_price - current_price)
	return profit


if __name__ == '__main__':
  print max_profit([200,300, 400, 300, -100, -200, -100, 0, 100, 200, 300, -200, 500])
  # print max_profit([200,300])