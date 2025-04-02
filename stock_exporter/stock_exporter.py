
from prometheus_client import start_http_server, Gauge
import yfinance as yf
import time

# Define metrics
stock_price = Gauge('stock_price', 'Price of the stock', ['stock_symbol'])
stock_eps = Gauge('stock_eps', 'Earnings per Share', ['stock_symbol'])
stock_dividend = Gauge('stock_dividend', 'Dividend', ['stock_symbol'])
stock_market_cap = Gauge('stock_market_cap', 'Market Capitalization', ['stock_symbol'])
stock_volume = Gauge('stock_volume', 'Stock Volume', ['stock_symbol'])
stock_daily_change = Gauge('stock_daily_change', 'Price change from market open', ['stock_symbol'])
stock_percent_change = Gauge('stock_percent_change', 'Percent price change from market open', ['stock_symbol'])

stocks = {
    'MBG.DE': 'Mercedes-Benz',
    'GOOGL': 'Google',
    'AMZN': 'Amazon'
}

def update_metrics():
    while True:
        for ticker, label in stocks.items():
            try:
                ticker_obj = yf.Ticker(ticker)
                hist = ticker_obj.history(period="1d", interval="1m")
                if not hist.empty:
                    latest_price = hist['Close'].iloc[-1]
                    opening_price = hist['Open'].iloc[0]
                    stock_price.labels(stock_symbol=label).set(latest_price)
                    stock_daily_change.labels(stock_symbol=label).set(latest_price - opening_price)
                    if opening_price > 0:
                        percent_change = ((latest_price - opening_price) / opening_price) * 100
                        stock_percent_change.labels(stock_symbol=label).set(percent_change)

                data = ticker_obj.info
                stock_eps.labels(stock_symbol=label).set(data.get('trailingEps', 0))
                stock_dividend.labels(stock_symbol=label).set(data.get('dividendRate') or 0)
                stock_market_cap.labels(stock_symbol=label).set(data.get('marketCap', 0) / 1e9)
                stock_volume.labels(stock_symbol=label).set(data.get('volume', 0))

                print(f"Updated {label}: ${latest_price:.2f}")
            except Exception as e:
                print(f"Error fetching data for {label} ({ticker}): {e}")

        time.sleep(300)

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus stock exporter started on port 8000")
    update_metrics()
