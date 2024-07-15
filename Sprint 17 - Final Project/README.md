# Final Project

## Introduction

The telecom operator Interconnect would like to be able to forecast their churn of clients. If it's discovered that a user is planning to leave, they will be offered promotional codes and special plan options. Interconnect's marketing team has collected some of their clientele's personal data, including information about their plans and contracts.


## Goal

Predict which customers are most likely to churn.

## Description of the Data

Obtained from multiple sources, the data consists of four files:

- `contract.csv`: contract information
  - `'customer_id'`: unique ID assigned to each customer
  - `'begin_date'`: sign-up date for each customer
  - `'end_date'`: our target feature, No == customer remains with the service
  - `'contract_type'`: plan type
  - `'paperless_billing'`: way of receiving billing statements
  - `'payment_method'`: method of payment
  - `'monthly_charges'`: monthly charges for the services provided
  - `'total_charges'`: total charges for the services provided

- `personal.csv`: the customer's personal data
  - `'customer_id'`: unique ID assigned to each customer
  - `'gender'`: gender of the customer
  - `'senior_citizen'`: age identifier for each customer
  - `'partner'`: customer husband/wife or partner
  - `'dependents'`: customer dependents

- `internet.csv`: information about internet services
  - `'customer_id'`: unique ID assigned to each customer
  - `'internet_service'`: type of internet service
  - `'online_security'`: additional internet service
  - `'online_backup'`: additional internet service
  - `'device_protection'`: additional internet service
  - `'tech_support'`: additional internet service

- `phone.csv`: information about telephone services
  - `'customer_id'`: unique ID assigned to each customer
  - `'multiple_lines'`: quantity of cell phone lines

## Tools

- Python
  - Pandas
  - Numpy
  - DateTime
  - TimeSeriesAnalyis
  - Plotly
  - MatPlotLib
  - Seaborn
  - SciKitLearn
  - LightGBM
  - XGBoost
  - LGBoost

## Examples of Charts

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%201.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%202.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%203.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%204.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%205.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%206.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%207.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%208.png)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2017%20-%20Final%20Project/Images/Image%209.png)
