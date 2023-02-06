# What is this script for

This script reads, processes and saves some csv data.

**Functionalities:**

- reads the input csv data
- from products with particular matching_id takes those with the highest total
  price, limits data set by top_priced_count and aggregate prices
- saves the results as top_products.csv in five columns: matching_id, total_price,
  avg_price, currency, ignored_products_count

# Requirements

- Python minimum version 3.7
- to install use in terminal: pip install -r requirements.txt

# How to run

- type 'python valuation_service.py' in the terminal to execute the script
- type 'pytest' in the terminal to run unit tests
