import streamlit as st
import numpy as np
import pandas as pd

st.title("Superstore KPI Dashboard")
st.write("My First Streamlit Dashboard")

# Load Dataset
df = pd.read_csv("Superstore.csv", encoding="latin-1")
st.write(df.head())

# Conver Date Column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Add Sidebar Filters
st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Order Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Order Date"].max()
)

region = st.sidebar.selectbox(
    "Select Region",
    df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

# Apply Filters to Dataset
filtered_df = df[
    (df["Order Date"] >= pd.to_datetime(start_date))&
    (df["Order Date"] <= pd.to_datetime(end_date))&
    (df["Region"] == region)&
    (df["Category"].isin(category))
]

# KPI Metrics
revenue = filtered_df['Sales'].sum()
orders = filtered_df['Order ID'].nunique()
profit = filtered_df['Profit'].sum()
aov = revenue / orders
profit_margin = (profit / revenue) * 100

col1 , col2 , col3 , col4 = st.columns(4)

col1.metric('Revenue' , f"${revenue:,.0f}")
col2.metric('Orders',orders)
col3.metric('Avg Order Value' , f"${aov:,.2f}")
col4.metric('Profit Margin' , f"${profit_margin:.2f}%")

# Line Chart(Revenue Trend)
import plotly.express as px

monthly_sales = filtered_df.resample(
    "M", on="Order Date"
)["Sales"].sum().reset_index()

line_chart = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Revenue Trend"
)

st.plotly_chart(line_chart, use_container_width=True)

# Bar chart

bar_chart = px.bar(
    filtered_df,
    x = 'Category',
    y = 'Sales',
    color = 'Category',
    title = 'Sales by Category'
)

st.plotly_chart(bar_chart , use_container_width = True)

# SCATTER PLOT

scatter = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category",
    title="Profit vs Discount"
)

st.plotly_chart(scatter, use_container_width=True)

# HEATMAP

filtered_df["Month"] = filtered_df["Order Date"].dt.month
filtered_df["Year"] = filtered_df["Order Date"].dt.year

pivot = filtered_df.pivot_table(
    values="Sales",
    index="Month",
    columns="Year",
    aggfunc="sum"
)

heatmap = px.imshow(pivot, title="Monthly Performance")

st.plotly_chart(heatmap)

# DONUT CHART

pie = px.pie(
    filtered_df,
    names="Segment",
    values="Sales",
    hole=0.4,
    title="Customer Segment Split"
)

st.plotly_chart(pie)

# MoM Growth %

monthly_sales["MoM"] = monthly_sales["Sales"].pct_change()*100

st.line_chart(
    monthly_sales.set_index("Order Date")["MoM"]
)

# Running Average (Forecast Trend)

monthly_sales["Running Avg"] = monthly_sales["Sales"].rolling(3).mean()

forecast = px.line(
    monthly_sales,
    x="Order Date",
    y=["Sales","Running Avg"],
    title="Forecast Trend"
)

st.plotly_chart(forecast, use_container_width=True)

