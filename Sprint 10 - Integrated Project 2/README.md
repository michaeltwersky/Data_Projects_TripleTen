# Integrated Project 2

## Introduction

Prepare a prototype of a machine learning model for Zyfra. The company develops efficiency solutions for heavy industry.

You have the data on extraction and purification.

The model will help to optimize the production and eliminate unprofitable parameters.

You need to:

1. Prepare the data
2. Perform data analysis
3. Develop and train a model

## Goal

Predict the amount of gold recovered from gold ore.

## Technological Process

Mined ore undergoes primary processing to get the ore mixture or rougher feed, which is the raw material for flotation (also known as the rougher process). After flotation, the material is sent to two-stage purification.

**1. Flotation**

Gold ore mixture is fed into the float banks to obtain rougher Au concentrate and rougher tails (product residues with a low concentration of valuable metals).

The stability of this process is affected by the volatile and non-optimal physicochemical state of the flotation pulp (a mixture of solid particles and liquid).

**2. Purification**

The rougher concentrate undergoes two stages of purification. After purification, we have the final concentrate and new tails.

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%204.jpeg)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%205.jpg)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%206.jpeg)

## Description of the Data

Spread across three tables, the data is as a follows:

**Technological process**

- `Rougher feed` — raw material
- `Rougher additions` (or reagent additions) — flotation reagents: Xanthate, Sulphate, Depressant
   - `Xanthate` — promoter or flotation activator;
   - `Sulphate` — sodium sulphide for this particular process;
   - `Depressant` — sodium silicate.
- `Rougher process` — flotation
- `Rougher tails` — product residues
- `Float banks` — flotation unit
- `Cleaner process` — purification
- `Rougher Au` — rougher gold concentrate
- `Final Au` — final gold concentrate

**Parameters of stages**

- `air amount` — volume of air
- `fluid levels`
- `feed size` — feed particle size
- `feed rate`

## Tools

- Python
  - Pandas
  - Matplotlib
  - SciKitLearn
  - Seaborn
  - Numpy
  - Plotly

## Examples of Charts

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%201.jpeg)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%202.jpeg)

![alt text](https://github.com/michaeltwersky/Data_Projects_TripleTen/blob/main/Sprint%2010%20-%20Integrated%20Project%202/Images/Image%203.jpeg)
