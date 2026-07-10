# Stock Portfolio Tracker

## Overview

The **Stock Portfolio Tracker** is a simple web application built with **Flask** that allows users to calculate the value of a stock investment. Users can select a stock symbol, enter the number of shares they own, and view the total portfolio value based on predefined stock prices.

This project is ideal for beginners learning Flask, HTML forms, and basic web development with Python.

---

## Features

- Simple web interface using Flask
- Calculate portfolio value based on stock quantity
- Predefined stock prices for selected companies
- Displays stock prices on the homepage
- Handles invalid stock symbols
- Lightweight and easy to customize

---

## Technologies Used

- Python 3
- Flask
- HTML
- Jinja2 Templates

---

## Project Structure

```
Stock-Portfolio-Tracker/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (Optional CSS files)
├── requirements.txt
└── README.md
```

---

## Stock Prices

The application currently supports the following stocks:

| Stock Symbol | Price (USD) |
|--------------|------------:|
| AAPL | $180 |
| TSLA | $250 |
| MSFT | $320 |
| GOOGL | $140 |

These prices are hardcoded in the application and can be modified in `app.py`.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
```

### 2. Navigate to the project directory

```bash
cd stock-portfolio-tracker
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will run at:

```
http://127.0.0.1:5000/
```

Open the URL in your web browser.

---

## How It Works

1. Open the web application.
2. Enter a stock symbol (e.g., `AAPL`).
3. Enter the number of shares.
4. Submit the form.
5. The application calculates and displays the total portfolio value.

If the stock symbol is not available, the application displays:

```
Stock not found!
```

---

## Example

### Input

```
Stock Symbol: AAPL
Quantity: 5
```

### Output

```
Portfolio Value = $900
```

---

## Code Explanation

### `stock_prices`

A Python dictionary stores predefined stock prices.

```python
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}
```

### Flask Route

The `/` route accepts both **GET** and **POST** requests.

- **GET:** Displays the homepage.
- **POST:** Reads user input and calculates the portfolio value.

### Portfolio Calculation

```python
total_value = stock_prices[stock] * qty
```

The total value is calculated by multiplying the stock price by the quantity entered.

---

## Future Improvements

- Fetch live stock prices using a financial API.
- Support multiple stocks in one portfolio.
- Store portfolio data in a database.
- Add user authentication.
- Display charts showing portfolio performance.
- Improve the user interface with Bootstrap.
- Export portfolio reports as PDF or Excel files.

---

## Requirements

- Python 3.x
- Flask

Install Flask using:

```bash
pip install flask
```

---

## Author

Developed as a beginner-friendly Flask project to practice web development, form handling, routing, and template rendering with Python.