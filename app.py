from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_info = None
    error_message = None

    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']

        try:
            # Fetch stock data using yfinance
            stock = yf.Ticker(stock_symbol)
            stock_info = stock.history(period="1d")

            # Check if stock_info is empty
            if stock_info.empty:
                error_message = f"No data available for {stock_symbol}"
        except Exception as e:
            error_message = f"Error fetching data for {stock_symbol}: {str(e)}"

    return render_template('index.html', stock_info=stock_info, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
