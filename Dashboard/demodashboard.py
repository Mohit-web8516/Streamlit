import streamlit as st
import pandas as pd
import numpy as np

# ------------------ Page Configuration ------------------
st.set_page_config(page_title="Simple Sales Dashboard", layout="wide")

# ------------------ Custom CSS ------------------
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

h1 {
    color: #1f77b4;
    text-align: center;
    font-weight: bold;
}

h2, h3 {
    color: #2c3e50;
}

div[data-testid="metric-container"] {
    background-color: white;
    border: 2px solid #dce6f1;
    padding: 18px;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.08);
}

section[data-testid="stSidebar"] {
    background-color: #eef5ff;
}

div[data-testid="stDataFrame"] {
    border-radius: 10px;
    border: 1px solid #dcdcdc;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Dummy Data ------------------
@st.cache_data
def load_data():
    np.random.seed(42)

    data = {
        "Date": pd.date_range("2024-01-01", periods=60),
        "Region": ["North", "South", "East", "West"] * 15,
        "Product": ["Chai", "Coffee", "Green Tea"] * 20,
        "Revenue": np.random.randint(500, 3000, 60),
        "Units_Sold": np.random.randint(20, 100, 60)
    }

    return pd.DataFrame(data)

df = load_data()

# ------------------ Sidebar ------------------
st.sidebar.header("🔍 Filters")

region_filter = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    df["Product"].unique(),
    default=df["Product"].unique()
)

# ------------------ Filter Data ------------------
filtered_df = df[
    df["Region"].isin(region_filter) &
    df["Product"].isin(product_filter)
]

# ------------------ Dashboard Title ------------------
st.markdown(
    "<h1>📈 Simple Sales Dashboard</h1>",
    unsafe_allow_html=True
)

# ------------------ KPI Section ------------------
total_revenue = filtered_df["Revenue"].sum()
total_units = filtered_df["Units_Sold"].sum()
avg_units = filtered_df["Units_Sold"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,}")
col2.metric("📦 Total Units Sold", total_units)
col3.metric("📊 Avg Units per Day", f"{avg_units:.2f}")

st.markdown("---")

# ------------------ Revenue Chart ------------------
with st.container():
    st.subheader("💰 Revenue by Product")

    revenue_chart = filtered_df.groupby("Product")["Revenue"].sum()

    st.bar_chart(revenue_chart)

# ------------------ Line Chart ------------------
with st.container():
    st.subheader("📅 Units Sold Over Time")

    units_time = filtered_df.groupby("Date")["Units_Sold"].sum()

    st.line_chart(units_time)

st.markdown("---")

# ------------------ Data Table ------------------
st.subheader("📋 Sales Data")

st.dataframe(
    filtered_df.sort_values(by="Date", ascending=False),
    use_container_width=True
)