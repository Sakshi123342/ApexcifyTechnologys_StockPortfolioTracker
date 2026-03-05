#Basic Stock Portfolio Tracker
import csv
from datetime import datetime

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 300
}

def display_available_stocks():
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

def get_user_input():
    while True:
        try:
            num=int(input("\nHow many different stocks do you want to invest in? "))
            if num > 0:
                return num
            else:
                print("please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_portfolio(num_stocks):
    portfolio = []
    total_investment = 0
    
    for i in range(num_stocks):
        print(f"\nStock Entry {i+1}")
        stock_name = input("Enter stock name:").upper()
        
        if stock_name not in stock_prices:
            print("stock not available. skipping...")
            continue

        try:
            quantity=int(input("Enter quantity:"))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Invalid quantity. skipping...")
            continue

        price = stock_prices[stock_name]
        investment= price* quantity
        total_investment += investment

        portfolio.append([stock_name,price,quantity,investment])

    return portfolio, total_investment

def display_summary(portfolio, total):
    print("\n-----Portfolio Summary-----")
    print(f"{'Stock':<10}{'Price':<10}{'Qty':<10}{'Investment':<15}")
    print("-" * 45)

    for entry in portfolio:
        print(f"{entry[0]:<10}{entry[1]:<10}{entry[2]:<10}{entry[3]:<15}")

        print("-" * 45)
        print(f"Total Investment value:${total}")
    
def save_to_csv(portfolio, total):
        filename ="portfolio_summary.csv"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, mode='w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Portfolio Summary"])
            writer.writerow(["Generated on:", timestamp])
            writer.writerow([])
            writer.writerow(["stock","price","Quantity","Investment"])

            for entry in portfolio:
                writer.writerow(entry)
            
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])

        print("\nPortfolio data saved successfully to portfolio_summary.csv")

def main():
    print("=== Welcome to Stock Portfolio Tracker ===")
    display_available_stocks()
    num_stocks = get_user_input()
    portfolio, total = calculate_portfolio(num_stocks)
    display_summary(portfolio, total)
    save_to_csv(portfolio, total)

if __name__ == "__main__":
     main()


# Advance Stock Portfolio Tracker            
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