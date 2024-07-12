# Exploratory Data Analysis (EDA)

## Introduction

Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and Door Dash work. This particular dataset was publicly released by [Instacart](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2) in 2017 for a [Kaggle competition](https://www.kaggle.com/c/instacart-market-basket-analysis/overview).

## Goal

Clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers. Create plots to communicate the results.

## Description of the Data

The data is spread across five tables:


- `instacart_orders.csv`: each row corresponds to one order on the Instacart app
    - `order_id`: ID number that uniquely identifies each order
  - `user_id`: ID number that uniquely identifies each customer account
  - `order_number`: the number of times this customer has placed an order
  - `order_dow`: day of the week that the order placed (which day is 0 is uncertain)
  - `order_hour_of_day`: hour of the day that the order was placed
  - `days_since_prior_order`: number of days since this customer placed their previous order

- `products.csv`: each row corresponds to a unique product that customers can buy
  - `product_id`: ID number that uniquely identifies each product
  - `product_name`: name of the product
  - `aisle_id`: ID number that uniquely identifies each grocery aisle category
  - `department_id`: ID number that uniquely identifies each grocery department category
- `order_products.csv`: each row corresponds to one item placed in an order
  - `order_id`: ID number that uniquely identifies each order
  - `product_id`: ID number that uniquely identifies each product
  - `add_to_cart_order`: the sequential order in which each item was placed in the cart
  - `reordered`: 0 if the customer has never ordered this product before, 1 if they have
- `aisles.csv`
  - `aisle_id`: ID number that uniquely identifies each grocery aisle category
  - `aisle`: name of the aisle
- `departments.csv`
  - `department_id`: ID number that uniquely identifies each grocery department category
  - `department`: name of the department




## Tools

- Python
  - Pandas
  - Matplotlib
  - Numpy

## Examples of Charts

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Images/Image%201.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2002%20-%20Exploratory%20Data%20Analysis%20(EDA)/Images/Image%202.png)
