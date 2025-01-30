from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')  # Stock market API key (Alpha Vantage / IEX Cloud)

# Portfolio to store user's stock choices (for demo purposes, using a simple list)
portfolio = []

# Fetch stock data from an API (e.g., Alpha Vantage)
def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Time Series (5min)' in data:
        time_series = data['Time Series (5min)']
        latest_time = list(time_series.keys())[0]
        latest_data = time_series[latest_time]
        return {
            'symbol': symbol,
            'price': latest_data['1. open'],
            'timestamp': latest_time
        }
    return None

# Home page - Search for stock
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        stock_data = get_stock_data(symbol)
        if stock_data:
            return render_template('index.html', stock_data=stock_data)
        return render_template('index.html', error="Stock not found")
    return render_template('index.html')

# Portfolio page - Display user's stocks
@app.route('/portfolio')
def show_portfolio():
    return render_template('portfolio.html', portfolio=portfolio)

# Add stock to portfolio
@app.route('/add_to_portfolio', methods=['POST'])
def add_to_portfolio():
    symbol = request.form['symbol']
    stock_data = get_stock_data(symbol)
    if stock_data:
        portfolio.append(stock_data)
    return redirect(url_for('show_portfolio'))

if __name__ == '__main__':
    app.run(debug=True)
