# Stock Monitoring Dashboard with Grafana Cloud

A real-time stock monitoring system that collects, exports, and visualizes custom stock data using:

- Python-based Prometheus exporter
- Grafana Agent for remote metric delivery
- Grafana Cloud dashboard (live, shareable)

---

## 🚀 Features

- Custom exporter provides metrics like:
  - `stock_market_cap`
  - `stock_price`
  - `stock_volume`
  - `stock_daily_change`
- Grafana Agent pushes metrics to **Grafana Cloud**
- Dashboards are provisioned automatically using JSON
- Easily share live metrics with a public Grafana Cloud URL

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/stock-monitoring
cd stock-monitoring
```

### 2. Configure Grafana Cloud
1. [Sign in to Grafana Cloud](https://grafana.com)
2. Create a **Prometheus Cloud** instance
3. Generate a **MetricsPublisher** API key
4. Note your:
   - **Instance ID** (e.g., `2358171`)
   - **Remote write URL** (e.g., `https://prometheus-prod-24-prod-eu-west-2.grafana.net/api/prom/push`)

### 3. Fill in credentials
Edit `agent-config.yml`:
```yaml
remote_write:
  - url: <YOUR_REMOTE_WRITE_URL>
    basic_auth:
      username: <YOUR_INSTANCE_ID>
      password: <YOUR_API_TOKEN>
```

### 4. Build and start the stack
```bash
docker compose up --build -d
```
This runs:
- `stock_exporter`: serves metrics at port `8000`
- `grafana-agent`: scrapes exporter & pushes to Grafana Cloud

---

## 📊 Dashboard

The Grafana dashboard is provisioned automatically from `stock_dashboard.json`. You can also access it live via:

**🔗 Public dashboard:**
```
https://sinembilgeguler.grafana.net/d/ferebtebh31/stock-portfolio1
```

You must be signed in to Grafana Cloud to view it (or make it public from dashboard settings).

---

## 📂 Project Structure
```
.
├── docker-compose.yml
├── stock_exporter/
│   ├── Dockerfile
│   └── stock_exporter.py
├── agent-config.yml
├── grafana/
│   └── provisioning/
│       ├── dashboards/
│       │   └── stock_dashboard_fixed.json
│       └── datasources/
│           └── datasource.yml
```

---

## ✅ To Keep It Live
To keep your dashboard updated:
- Leave Docker running locally
- Or deploy it to a free-tier cloud host (Render, Railway, Fly.io)

---

## 📬 Contact
Made with ❤️ by Sinem Bilge Güler  
[LinkedIn](https://www.linkedin.com/in/sinembilge-güler-61a9261bb/)
