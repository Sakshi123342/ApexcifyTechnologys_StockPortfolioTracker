import csv
from datetime import datetime

# Hardcoded buying prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

def display_stocks():
    print("\nAvailable Stocks (Buying Price):")
    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

def get_number():
    while True:
        try:
            num = int(input("\nHow many stocks do you want to enter? "))
            if num > 0:
                return num
            else:
                print("Enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Enter a valid number.")

def calculate_portfolio(n):
    portfolio = []
    total_investment = 0
    total_current_value = 0

    for i in range(n):
        print(f"\nStock Entry {i+1}")
        stock = input("Enter stock name: ").upper()

        if stock not in stock_prices:
            print("Stock not available. Skipping...")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            current_price = float(input("Enter current market price: "))
        except ValueError:
            print("Invalid input. Skipping...")
            continue

        buying_price = stock_prices[stock]
        investment = buying_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        portfolio.append([stock, buying_price, current_price, quantity, investment, current_value, profit_loss])

    return portfolio, total_investment, total_current_value

def display_summary(portfolio, total_inv, total_curr):
    print("\n------ Portfolio Summary ------")
    print(f"{'Stock':<8}{'Buy':<8}{'Curr':<8}{'Qty':<6}{'Invest':<12}{'CurrVal':<12}{'P/L':<10}")
    print("-" * 70)

    for row in portfolio:
        print(f"{row[0]:<8}{row[1]:<8}{row[2]:<8}{row[3]:<6}{row[4]:<12}{row[5]:<12}{row[6]:<10}")

    total_profit = total_curr - total_inv
    growth = (total_profit / total_inv * 100) if total_inv != 0 else 0

    print("-" * 70)
    print(f"Total Investment: ${total_inv}")
    print(f"Current Value: ${total_curr}")
    print(f"Total Profit/Loss: ${total_profit}")
    print(f"Growth Percentage: {round(growth,2)}%")

    return total_profit, growth

def save_to_csv(portfolio, total_inv, total_curr, total_profit, growth):
    filename = "advanced_portfolio_summary.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Portfolio Summary"])
        writer.writerow(["Generated On:", timestamp])
        writer.writerow([])
        writer.writerow(["Stock", "Buying Price", "Current Price", "Quantity", "Investment", "Current Value", "Profit/Loss"])

        for row in portfolio:
            writer.writerow(row)

        writer.writerow([])
        writer.writerow(["Total Investment", total_inv])
        writer.writerow(["Current Value", total_curr])
        writer.writerow(["Total Profit/Loss", total_profit])
        writer.writerow(["Growth Percentage", f"{round(growth,2)}%"])

    print("\nData saved successfully to advanced_portfolio_summary.csv")

def main():
    print("==== Advanced Stock Portfolio Tracker ====")
    display_stocks()
    num = get_number()
    portfolio, total_inv, total_curr = calculate_portfolio(num)
    total_profit, growth = display_summary(portfolio, total_inv, total_curr)
    save_to_csv(portfolio, total_inv, total_curr, total_profit, growth)

if __name__ == "__main__":
    main()
