FROM python:3.10
WORKDIR /app
COPY stock_exporter.py .
RUN pip install prometheus_client yfinance
CMD ["python", "stock_exporter.py"]
