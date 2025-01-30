from flask import Flask, render_template, request
import yfinance as yf
import plotly.express as px
import plotly.io as pio

# Create the Flask app
app = Flask(__name__)

# Default route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch stock data and display the chart
@app.route('/get_stock', methods=['POST'])
def get_stock():
    stock_symbol = request.form.get('stock_symbol')
    
    if not stock_symbol:
        return "Stock symbol is required!", 400
    
    # Fetch stock data using yfinance
    stock_data = yf.download(stock_symbol, period="1d", interval="1m")
    
    if stock_data.empty:
        return f"No data found for {stock_symbol}", 404
    
    # Create the stock price plot
    fig = px.line(stock_data, x=stock_data.index, y='Close', title=f'{stock_symbol} Stock Price')
    fig.update_layout(xaxis_title="Date", yaxis_title="Stock Price (USD)", showlegend=False)
    
    # Return the plot as HTML
    graph_html = pio.to_html(fig, full_html=False)
    
    return render_template('stock_chart.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
