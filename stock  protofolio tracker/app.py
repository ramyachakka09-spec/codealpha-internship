# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

@app.route("/", methods=["GET", "POST"])
def index():
    total_value = None
    portfolio = {}
    if request.method == "POST":
        stock = request.form.get("stock").upper()
        qty = int(request.form.get("quantity"))
        portfolio[stock] = qty
        if stock in stock_prices:
            total_value = stock_prices[stock] * qty
        else:
            total_value = "Stock not found!"
    return render_template("index.html", portfolio=portfolio, total_value=total_value, stock_prices=stock_prices)

if __name__ == "__main__":
    app.run(debug=True)