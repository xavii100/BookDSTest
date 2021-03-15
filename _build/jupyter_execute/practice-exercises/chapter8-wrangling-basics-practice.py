![](../docs/banner.png)

# Basic Wrangling With Pandas

**Tomas Beuzen, September 2020**

These exercises complement [Chapter 8](../chapters/chapter8-wrangling-basics.ipynb).

## Exercises

### 1.

In this set of practice exercises we'll be again looking at the dataset of consumption and carbon footprints of different foods that we looked at in the last set of practice exercises, which was compiled by [Kasia Kulma](https://r-tastic.co.uk/post/from-messy-to-tidy/) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday).

Let's start by importing pandas with the alias `pd`.

# Your answer here.

### 2.

As a reminder, the dataset has the following columns:

|column      |description |
|:-------------|:-----------|
|country       | Country Name |
|food_category | Food Category |
|consumption   | Consumption (kg/person/year) |
|co2_emmission | Co2 Emission (Kg CO2/person/year) |


Import the dataset as a dataframe named `df` from this url: <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-18/food_consumption.csv>

# Your answer here.

### 3.

What country consumes the most food per person per year (across all food categories)?

# Your answer here.

### 4.

Which food category is the biggest contributor to the above country's consumption total?

# Your answer here.

### 5.

What country produces the most kg C02 per person per year?

# Your answer here.

### 6.

Which food category is the biggest contributor to the above country's C02 emissions?

# Your answer here.

### 7.

What food category produces the most C02 per person per year across all countries?

# Your answer here.

### 8.

What food category is consumed the most across all countries per person per year? What food category is consumed the least across all countries?

# Your answer here.

### 9.

Make the dataset wide by pivoting on the `food_category` column. You'll end up with a "multi-index" dataframe, with multiple levels of columns.

# Your answer here.

### 10.

Now that the dataset is wide, I want you to answer the same question from Question 5 above: "What country produces the most kg C02 per person per year?". Specifically, I want you to notice that the way we answer the same data analysis question changes depending on the format of the data (wide vs long). You can form your own opinion on which option you prefer - I prefer long data (and remember that many visualization libraries work best with long data too - more on that in DSCI 531). *Hint*: you can index the outer layer of a multi-index column using the same syntax we've seen previously: `df['co2_emmission']`, if you wanted to access an inner index, you'd have to use a tuple: `df[("consumption", "Beef")]`. Read more on multi-indexes (also called "hierarchical indexes") in [Chapter 9](../chapters/chapter9-wrangling-advanced.ipynb).

# Your answer here.

<hr>
<hr>
<hr>

## Solutions

### 1.

In this set of practice exercises we'll be again looking at the dataset of consumption and carbon footprints of different foods that we looked at in the last set of practice exercises, which was compiled by [Kasia Kulma](https://r-tastic.co.uk/post/from-messy-to-tidy/) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday).

Let's start by importing pandas with the alias `pd`.

import pandas as pd

### 2.

As a reminder, the dataset has the following columns:

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

What country consumes the most food per person per year (across all food categories)?

df.groupby("country").sum().sort_values(by="consumption").tail(1)

### 4.

Which food category is the biggest contributor to the above country's consumption total?

df.query("country == 'Finland'").sort_values(by="consumption").tail(1)

### 5.

What country produces the most kg C02 per person per year?

df.groupby("country").sum().sort_values(by="co2_emmission").tail(1)

### 6.

Which food category is the biggest contributor to the above country's C02 emissions?

df.query("country == 'Argentina'").sort_values(by="co2_emmission").tail(1)

### 7.

What food category produces the most C02 per person per year across all countries?

df.groupby("food_category").sum().sort_values(by="co2_emmission", ascending=False)

### 8.

What food category is consumed the most across all countries per person per year? What food category is consumed the least across all countries?

print("Most consumption:")
print(df.groupby("food_category").sum().sort_values(by="consumption", ascending=False).head(1))
print("")
print("Least consumption:")
print(df.groupby("food_category").sum().sort_values(by="consumption", ascending=False).tail(1))

### 9.

Make the dataset wide by pivoting on the `food_category` column. You'll end up with a "multi-index" dataframe, with multiple levels of columns.

df = df.pivot(index='country', columns='food_category')
df

### 10.

Now that the dataset is wide, I want you to answer the same question from Question 5 above: "What country produces the most kg C02 per person per year?". Specifically, I want you to notice that the way we answer the same data analysis question changes depending on the format of the data (wide vs long). You can form your own opinion on which option you prefer - I prefer long data (and remember that many visualization libraries work best with long data too - more on that in DSCI 531). *Hint*: you can index the outer layer of a multi-index column using the same syntax we've seen previously: `df['co2_emmission']`, if you wanted to access an inner index, you'd have to use a tuple: `df[("consumption", "Beef")]`. Read more on multi-indexes (also called "hierarchical indexes") in [Chapter 9](../chapters/chapter9-wrangling-advanced.ipynb).

df["consumption"].sum(axis=1).sort_values().tail(1)