import pandas as pd

# Create sample sales data.
sales = pd.DataFrame({
    "Region": ["North", "South", "West"],
    "Units": [12, 9, 15],
    "Price": [100, 100, 100]
})

# Calculate total sales for each region.
sales["Sales"] = sales["Units"] * sales["Price"]

# Prepare the table that Power BI will import.
report = sales[["Region", "Sales"]]

# Display the results when running in Python.
print(report.to_string(index=False))