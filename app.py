import yfinance as yf
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stock_info = None
    error_message = None

    if request.method == "POST":
        stock_symbol = request.form.get("stock_symbol").upper()
        
        try:
            # Fetch stock data from Yahoo Finance
            stock = yf.Ticker(stock_symbol)
            stock_data = stock.history(period="1d")

            if stock_data.empty:
                error_message = f"No data available for {stock_symbol}."
            else:
                # Extract necessary data
                stock_info = {
                    "symbol": stock_symbol,
                    "close": stock_data["Close"][0],
                    "open": stock_data["Open"][0],
                    "high": stock_data["High"][0],
                    "low": stock_data["Low"][0],
                    "volume": stock_data["Volume"][0],
                }
        except Exception as e:
            error_message = f"Error fetching data for {stock_symbol}: {e}"

    return render_template("index.html", stock_info=stock_info, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
