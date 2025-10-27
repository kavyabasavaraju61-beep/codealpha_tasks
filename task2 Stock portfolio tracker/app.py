from flask import Flask, render_template, request

app = Flask(__name__)

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
    "META": 320
}

@app.route("/", methods=["GET", "POST"])
def index():
    total_investment = None
    portfolio_details = []

    if request.method == "POST":
        # Step 2: Get input from form
        stocks = request.form.get("stocks").upper().split(",")
        quantities = request.form.get("quantities").split(",")

        # Step 3: Calculate total investment
        total_investment = 0
        for i in range(len(stocks)):
            stock = stocks[i].strip()
            qty = int(quantities[i].strip())
            if stock in stock_prices:
                value = stock_prices[stock] * qty
                total_investment += value
                portfolio_details.append({
                    "stock": stock,
                    "quantity": qty,
                    "price": stock_prices[stock],
                    "value": value
                })
            else:
                portfolio_details.append({
                    "stock": stock,
                    "quantity": qty,
                    "price": "N/A",
                    "value": "N/A"
                })

    return render_template("index.html", portfolio=portfolio_details, total=total_investment)

if __name__ == "__main__":
    app.run(debug=True)

