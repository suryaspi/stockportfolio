import csv

def run_stock_tracker():
    """
    A simple stock portfolio tracker that calculates total investment value
    based on hardcoded stock prices. It allows the user to input stocks
    and quantities, and can optionally save the portfolio to a file.
    """
    
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 150.20,
        "AMZN": 135.80,
        "MSFT": 320.10
    }

    
    portfolio = {}

    print("Welcome to the simple Stock Portfolio Tracker!")
    print("Available stocks and their prices:")
    for ticker, price in stock_prices.items():
        print(f" - {ticker}: ${price:.2f}")

    
    while True:
        
        ticker = input("\nEnter a stock ticker (e.g., AAPL) or 'done' to finish: ").upper()
        if ticker == 'DONE':
            break

        
        if ticker not in stock_prices:
            print("Error: That stock ticker is not in our database. Please try again.")
            continue

        
        try:
            quantity = int(input(f"Enter the quantity for {ticker}: "))
            if quantity <= 0:
                print("Error: Quantity must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for the quantity.")
            continue

        
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity
        print(f"Added {quantity} shares of {ticker} to your portfolio.")

    
    total_value = 0.0
    print("\n--- Your Portfolio ---")
    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for ticker, quantity in portfolio.items():
            price = stock_prices[ticker]
            stock_value = quantity * price
            total_value += stock_value
            print(f"{ticker}: {quantity} shares @ ${price:.2f} each = ${stock_value:.2f}")
    
    print(f"\n--- Total Portfolio Value: ${total_value:.2f} ---")

    
    save_option = input("\nWould you like to save your portfolio to a file? (yes/no): ").lower()
    if save_option == 'yes':
        try:
            
            with open("portfolio.txt", "w") as f:
                f.write("Stock Portfolio Report\n")
                f.write("----------------------\n")
                for ticker, quantity in portfolio.items():
                    price = stock_prices[ticker]
                    stock_value = quantity * price
                    f.write(f"{ticker}: {quantity} shares @ ${price:.2f} | Value: ${stock_value:.2f}\n")
                f.write(f"\nTotal Portfolio Value: ${total_value:.2f}\n")
            print("Portfolio successfully saved to 'portfolio.txt'.")

            
            with open("portfolio.csv", "w", newline='') as csvfile:
                fieldnames = ['Ticker', 'Quantity', 'Price', 'Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for ticker, quantity in portfolio.items():
                    price = stock_prices[ticker]
                    stock_value = quantity * price
                    writer.writerow({
                        'Ticker': ticker,
                        'Quantity': quantity,
                        'Price': f'{price:.2f}',
                        'Value': f'{stock_value:.2f}'
                    })
            print("Portfolio also saved to 'portfolio.csv'.")

        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

run_stock_tracker()
