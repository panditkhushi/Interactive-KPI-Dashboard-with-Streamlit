## 👩‍💻 Author

Khushi Pandit

# 📊 Superstore KPI Dashboard (Streamlit)

## 📌 Project Overview
This project is an interactive **KPI Dashboard** built using **Streamlit** to analyze Superstore sales data.

The dashboard provides real-time insights into:
- Revenue
- Orders
- Profitability
- Customer segments
- Sales trends

Users can dynamically filter data and visualize business performance using interactive charts.


## 🎯 Objective
- Build an interactive business dashboard
- Track key performance indicators (KPIs)
- Enable data-driven decision-making
- Practice real-world data visualization


## 📂 Dataset
The project uses the **Superstore dataset**, which includes:
- Order Date
- Region
- Category
- Sales
- Profit
- Discount
- Segment
- Order ID


## ⚙️ Tech Stack

- **Python 🐍**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Plotly**


## 🚀 Features

### 🔍 Filters (Sidebar)
- Date range filter
- Region selection
- Category multi-select

### 📊 KPI Metrics
- Total Revenue
- Total Orders
- Average Order Value (AOV)
- Profit Margin %


## 📈 Visualizations

### 📉 Charts Included
- Line Chart → Revenue Trend (Monthly)
- Bar Chart → Sales by Category
- Scatter Plot → Profit vs Discount
- Heatmap → Monthly Sales Performance
- Donut Chart → Customer Segment Distribution
- MoM Growth Chart → Month-over-Month growth %
- Forecast Trend → Running Average (3-month rolling)


## 🧠 Key Calculations

- **Revenue** = Sum of Sales  
- **Orders** = Unique Order IDs  
- **AOV** = Revenue / Orders  
- **Profit Margin** = (Profit / Revenue) × 100  
- **MoM Growth** = Percentage change in monthly sales  
- **Running Average** = Rolling mean (window = 3)


## 📌 Important Notes

- Ensure Superstore.csv is in the same directory as the script
- Encoding used: latin-1
- Date column is converted to datetime format

## 🚀 Future Improvements

- Add advanced filters (City, Segment)
- Add download/export options
- Deploy on Streamlit Cloud
- Add predictive models (Sales Forecasting)
- Improve UI/UX design

## 📚 Learning Outcomes

- Building dashboards using Streamlit
- Data filtering and transformation
- KPI calculation and business metrics
- Interactive visualization with Plotly
