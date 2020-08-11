def get_max_profit(stock_prices):
    cur_max = stock_prices[1] - stock_prices[0]
    cur_min = stock_prices[0]
    for i in range(1, len(stock_prices)):
        if stock_prices[i] - cur_min > cur_max:
            cur_max = stock_prices[i] - cur_min
        if stock_prices[i] < cur_min:
            cur_min = stock_prices[i]
    return cur_max

