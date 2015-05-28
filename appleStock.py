def bestProfit(array):

	current_maximum = 0
	temp_maximum = 0

	for i in range(len(array)):
		for number in array[i:]:
			temp_maximum = number - array[i]
			if( temp_maximum > current_maximum):
				current_maximum = temp_maximum
	print current_maximum

bestProfit([1,2,5,8,3,8,0])

# The above solution runs in O(n2) time, this is obviously inefficient
# We can improve upon this by keeping track of our current best minimum price to buy and maximum profit

def get_best_profit(stock_prices_yesterday):

	minimum_price = stock_prices_yesterday[0]
	max_profit = 0

	for current_price in stock_prices_yesterday:
		minimum_price = min(minimum_price, current_price)
		max_profit = max(max_profit, current_price - minimum_price)
	print max_profit

get_best_profit([1,2,5,8,3,8,0])

# The above solution runs in O(n) time. The difficulty I faced in coming up with this solution revlolved around over complicating the problem.
# I failed to break down the problem into its sub problems
# There was the minimum price and maximum profit, and these two need be considered while iterating through the array