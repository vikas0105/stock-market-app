from flask import Flask, render_template, request
import yfinance as yf
import plotly.graph_objs as go

app = Flask(__name__)

# Simple route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    graph_html = ""
    ticker = ""

    if request.method == 'POST':
        # Get the ticker symbol entered by the user
        ticker = request.form.get('ticker_symbol').upper()  # Ensure uppercase for NSE symbols like RELIANCE.NS
        
        try:
            # Fetch stock data for the given ticker symbol from Yahoo Finance
            stock_data = yf.download(ticker, perio
