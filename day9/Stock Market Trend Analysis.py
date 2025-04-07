def analyze_stock_trends():
    # Ask the user how many days of stock prices they want to enter
    days = int(input("Enter the number of days you want to analyze: "))
    
    # List to store the stock prices
    prices = []
    
    # Get stock prices for each day
    for day in range(1, days + 1):
        price = float(input(f"Enter the stock price for Day {day}: "))
        prices.append(price)
    
    print("\nAnalyzing Stock Trends...\n")
    
    # Ensure there are at least two prices to compare
    if len(prices) < 2:
        print("Not enough data to analyze trends.")
        return
    
    # Loop through the prices to analyze trends
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            print(f"Day {i+1}: Stock Price {prices[i]} - Buy Signal (price is rising)")
        elif prices[i] < prices[i - 1]:
            print(f"Day {i+1}: Stock Price {prices[i]} - Sell Signal (price is falling)")
        else:
            print(f"Day {i+1}: Stock Price {prices[i]} - Hold (price is stable)")

# Start the stock trend analysis
analyze_stock_trends()
