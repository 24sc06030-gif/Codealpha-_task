# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"Added {stock}: ₹{investment}")

print("\n💰 Total Investment Value: ₹", total_investment)

# Optional: Save result to a file
save = input("Do you want to save result to file? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write(f"Total Investment Value: ₹{total_investment}")
    file.close()
    print("📄 Saved to portfolio.txt")
