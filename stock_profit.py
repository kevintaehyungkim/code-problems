'''
Suppose we could access yesterday's Apple stock prices as a list, where:
The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
Write an efficient function that takes stock_prices_yesterday and returns the best profit 
I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

Difficulty: Medium

Solution notes:
O(n) time
O(1) space

dynamic programming

# if allowed to mutate input array
def max_profit(stock_prices):
	if len(stock_prices) < 2:
		return 0
	min_price = stock_prices[0]
	for i in xrange(0, len(stock_prices)):
		price = stock_prices[i]
		if price < min_price:
			min_price = price
			stock_prices[i] = 0
		else:
			stock_prices[i] = price - min_price
	return max(stock_prices)

'''


# without mutating input array
def max_profit(stock_prices):
	if len (stock_prices) < 2:
		return 0
	max_profit = 0
	min_price = stock_prices[0]
	for price in stock_prices:
		profit = price - min_price
		min_price = min(min_price, price)
		max_profit = max(max_profit, profit)
	return max_profit



if __name__ == '__main__':
  print max_profit([200,300, 400, 300, -100, -200, -100, 0, 100, 200, 300, -200, 500])
