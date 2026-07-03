import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------

try:
    df = pd.read_csv("sales_data.csv")
    print("Dataset Loaded Successfully!")
except FileNotFoundError:
    print("Dataset not found!")
    exit()

# -------------------------------
# Data Cleaning
# -------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# Basic Analysis
# -------------------------------

print("\nDataset Information")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nTotal Sales:", df["Total_Sales"].sum())

print("\nAverage Sales:", df["Total_Sales"].mean())

# -------------------------------
# Sales by Product
# -------------------------------

product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# -------------------------------
# Sales Trend
# -------------------------------

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10,5))
daily_sales.plot(kind="line")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -------------------------------
# Region-wise Sales
# -------------------------------

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(6,6))
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.ylabel("")
plt.title("Region-wise Sales Distribution")
plt.tight_layout()
plt.show()

# -------------------------------
# Insights
# -------------------------------

print("\n===== Insights =====")

print("Best Selling Product:")
print(product_sales.idxmax())

print("\nHighest Sales Region:")
print(region_sales.idxmax())

print("\nTotal Revenue:")
print(df["Total_Sales"].sum())