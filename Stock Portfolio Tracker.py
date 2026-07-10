stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}
portfolio = {}
total_value = 0
print("=== STOCK PORTFOLIO TRACKER ===")
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue
    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(stock, "- Quantity:", quantity, "- Price:", price, "- Value:", value)
print("\nTotal Portfolio Value: $", total_value)
