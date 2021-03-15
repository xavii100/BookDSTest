![](../docs/banner.png)

# Pandas

**Tomas Beuzen, September 2020**

These exercises complement [Chapter 7](../chapters/chapter7-pandas.ipynb).

## Exercises

### 1.

In this set of practice exercises we'll be investigating the carbon footprint of different foods. We'll be leveraging a dataset compiled by [Kasia Kulma](https://r-tastic.co.uk/post/from-messy-to-tidy/) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday).

Start by importing pandas with the alias `pd`.

# Your answer here.

### 2.

The dataset we'll be working with has the following columns:

|column      |description |
|:-------------|:-----------|
|country       | Country Name |
|food_category | Food Category |
|consumption   | Consumption (kg/person/year) |
|co2_emmission | Co2 Emission (Kg CO2/person/year) |


Import the dataset as a dataframe named `df` from this url: <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv>

# Your answer here.

### 3.

How many rows and columns are there in the dataframe?

# Your answer here.

### 4.

What is the type of data in each column of `df`?

# Your answer here.

### 5.

What is the mean `co2_emission` of the whole dataset?

# Your answer here.

### 6.

How many different kinds of foods are there in the dataset? How many countries are in the dataset?

# Your answer here.

### 7.

What is the maximum `co2_emmission` in the dataset and which food type and country does it belong to?

# Your answer here.

### 8.

How many countries produce more than 1000 Kg CO2/person/year for at least one food type?

# Your answer here.

### 9.

Which country consumes the least amount of beef per person per year?

# Your answer here.

### 10.

Which country consumes the most amount of soybeans per person per year?

# Your answer here.

### 11.

What is the total emissions of all the meat products (Pork, Poultry, Fish, Lamb & Goat, Beef) in the dataset combined?

# Your answer here.

### 12.

What is the total emissions of all other (non-meat) products in the dataset combined?

# Your answer here.

<hr>
<hr>
<hr>

## Solutions

### 1.

In this set of practice exercises we'll be investigating the carbon footprint of different foods. We'll be leveraging a dataset compiled by [Kasia Kulma](https://r-tastic.co.uk/post/from-messy-to-tidy/) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday).

Start by importing pandas with the alias `pd`.

import pandas as pd

### 2.

The dataset we'll be working with has the following columns:

|column      |description |
|:-------------|:-----------|
|country       | Country Name |
|food_category | Food Category |
|consumption   | Consumption (kg/person/year) |
|co2_emmission | Co2 Emission (Kg CO2/person/year) |


Import the dataset as a dataframe named `df` from this url: <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv>

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv"
df = pd.read_csv(url)
df

### 3.

How many rows and columns are there in the dataframe?

df.shape

### 4.

What is the type of data in each column of `df`?

df.info()

### 5.

What is the mean `co2_emission` of the whole dataset?

df["co2_emmission"].mean()

### 6.

How many different kinds of foods are there in the dataset? How many countries are in the dataset?

print(f"There are {df['food_category'].nunique()} foods.")
print(f"There are {df['country'].nunique()} countries.")

### 7.

What is the maximum `co2_emmission` in the dataset and which food type and country does it belong to?

df.iloc[df['co2_emmission'].idxmax()]

### 8.

How many countries produce more than 1000 Kg CO2/person/year for at least one food type?

df.query("co2_emmission > 1000")

### 9.

Which country consumes the least amount of beef per person per year?

(df.query("food_category == 'Beef'")
   .sort_values(by="consumption")
   .head(1))

### 10.

Which country consumes the most amount of soybeans per person per year?

(df.query("food_category == 'Soybeans'")
   .sort_values(by="consumption", ascending=False)
   .head(1))

### 11.

What is the total emissions of all the meat products (Pork, Poultry, Fish, Lamb & Goat, Beef) in the dataset combined?

meat = ['Poultry', 'Pork', 'Fish', 'Lamb & Goat', 'Beef']
df["co2_emmission"][df['food_category'].isin(meat)].sum()

### 12.

What is the total emissions of all other (non-meat) products in the dataset combined?

meat = ['Poultry', 'Pork', 'Fish', 'Lamb & Goat', 'Beef']
df["co2_emmission"][~df['food_category'].isin(meat)].sum()