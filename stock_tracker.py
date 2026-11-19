# Stock Portfolio Tracker

# Stock names and prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190
}

# Starting total investment
total_investment = 0

# Ask number of stocks
number_of_stocks = int(input("How many different stocks do you have? "))

# Get stock details
for i in range(number_of_stocks):

    stock_name = input("Enter stock name: ").upper()

    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:

        price = stocks[stock_name]

        investment = price * quantity

        total_investment = total_investment + investment

        print("Investment:", investment)

    else:
        print("Stock not found!")

# Display total
print("----------------------")
print("Total Investment:", total_investment)

# Save result
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("Total Investment: " + str(total_investment))

print("Portfolio saved successfully!")