# E-commerce Sales Analysis

## Project Overview

The **E-commerce Sales Analysis** project demonstrates a complete data analysis workflow using Python. The project loads a sales dataset, cleans and validates the data, performs statistical analysis, and visualizes the results using different chart types.

The primary goal is to identify sales trends, compare product performance, and understand regional sales distribution through meaningful visualizations and insights.

---

## Project Objectives

* Load and process a real-world sales dataset.
* Clean and validate the dataset by handling duplicates and checking for missing values.
* Perform exploratory data analysis (EDA).
* Generate professional visualizations using Matplotlib.
* Extract meaningful business insights from the analysis.
* Demonstrate a complete data analysis pipeline suitable for beginners.

---

## Technologies Used

* Python 3.x
* Pandas
* Matplotlib

---

## Project Structure

```
e-commerce_sales_analysis/
│
├── data/
│   └── sales_data.csv
│
├── visualizations/
│   ├── sales_by_product.png
│   ├── sales_trend.png
│   └── region_sales.png
│
├── report/
│   └── Project_Report.md
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Setup and Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/tushar-737/e-commerce_sales_analysis.git
```

### 2. Navigate to the Project Folder

```bash
cd e-commerce_sales_analysis
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Project

```bash
python main.py
```

---

## Code Structure Explanation

### Data Loading

* Loads the CSV dataset using Pandas.
* Uses `try-except` for error handling if the dataset is missing.

### Data Cleaning

* Checks for missing values.
* Removes duplicate records.
* Converts the Date column into datetime format.

### Data Analysis

The project calculates:

* Total Sales
* Average Sales
* Product-wise Sales
* Daily Sales Trend
* Region-wise Sales

### Data Visualization

Three charts are created:

1. **Bar Chart**

   * Compares total sales for each product.

2. **Line Chart**

   * Displays sales trends over time.

3. **Pie Chart**

   * Shows the percentage contribution of each region to total sales.

### Business Insights

The project identifies:

* Best-selling product
* Highest revenue-generating region
* Overall revenue
* Average sales


### 1. Console Output

Screenshot showing:

* Dataset loaded successfully
* Summary statistics
* Business insights

### 2. Bar Chart

`sales_by_product.png`

### 3. Line Chart

`sales_trend.png`

### 4. Pie Chart

`region_sales.png`

---

## Technical Requirements Achieved

### Complete Data Analysis Pipeline

✔ Dataset loading

✔ Data validation

✔ Data cleaning

✔ Data analysis

✔ Data visualization

✔ Business insights

---

### Multiple Chart Types

✔ Bar Chart

✔ Line Chart

✔ Pie Chart

---

### Professional Formatting

✔ Titles added to charts

✔ Axis labels included

✔ Proper figure sizes

✔ Charts saved as image files

---

### Error Handling

✔ `try-except` block for file loading

✔ Dataset validation before analysis

---

## Key Insights

* Identified the product generating the highest sales.
* Determined the region contributing the most revenue.
* Observed daily sales trends using a line chart.
* Calculated total and average sales for the business.

---

## Future Improvements

* Interactive dashboards using Plotly or Streamlit.
* Monthly and yearly sales reports.
* Customer segmentation analysis.
* Predictive sales forecasting using machine learning.
* Export analysis results to Excel or PDF.


## Author

**Tushar Gupta**

