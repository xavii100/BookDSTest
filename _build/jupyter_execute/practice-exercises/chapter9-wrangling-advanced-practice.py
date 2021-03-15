![](../docs/banner.png)

# Advanced Wrangling With Pandas

**Tomas Beuzen, September 2020**

These exercises complement [Chapter 9](../chapters/chapter9-wrangling-advanced.ipynb).

## Exercises

### 1.

In this set of practice exercises we'll be looking at a cool dataset of real passwords (made available from actual data breaches) sourced and compiled from [Information is Beautiful](https://informationisbeautiful.net/visualizations/top-500-passwords-visualized/?utm_content=buffer994fa&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday). These passwords are common ("bad") passwords that you should avoid using! But we're going to use this dataset to practice some regex skills.

Let's start by importing pandas with the alias `pd`.

# Your answer here.

### 2.

The dataset has the following columns:

|variable          |class     |description |
|:-----------------|:---------|:-----------|
|rank              |int    | popularity in their database of released passwords |
|password          |str | Actual text of the password |
|category          |str | What category does the password fall in to?|
|value             |float    | Time to crack by online guessing |
|time_unit         |str | Time unit to match with value |
|offline_crack_sec |float    | Time to crack offline in seconds |
|rank_alt          |int    | Rank 2 |
|strength          |int    | Strength = quality of password where 10 is highest, 1 is lowest, please note that these are relative to these generally bad passwords |
|font_size         |int    | Used to create the graphic for KIB |


In these exercises, we're only interested in the `password`, `value` and `time_unit` columns so import only these two columns as a dataframe named `df` from this url: <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv>

# Your answer here.

### 3.

An online password attack is when someone tries to hack your account by simply trying a very large number of username/password combinations to access your account. For each `password` in our dataset, the `value` column shows the amount of time it is estimated to take an "online password attack" to hack your account. The column `time_unit` shows the units of that time value (e.g., hours, days, years, etc.)

It would be much nicer if our `value`s were of the same units so we can more easily compare the "online password guessing time" for each password. So your first task is to convert all of the values to units of hours (assume the conversion units I've provided below, e.g., 1 day is 24 hours, 1 week is 168 hours, etc).

units = {
    "seconds": 1 / 3600,
    "minutes": 1 / 60,
    "days": 24,
    "weeks": 168,
    "months": 720,
    "years": 8760,
}

# Your answer here.

### 4.

How many password begin with the sequence `123`?

# Your answer here.

### 5.

What is the average time in hours needed to crack these passwords that begin with `123`? How does this compare to the average of all passwords in the dataset?

# Your answer here.

### 6.

How many passwords do not contain a number?

# Your answer here.

### 7.

How many passwords contain at least one number?

# Your answer here.

### 8.

Is there an obvious difference in online cracking time between passwords that don't contain a number vs passwords that contain at least one number?

# Your answer here.

### 9.

How many passwords contain at least one of the following punctuations: `[.!?\\-]` (hint: remember this dataset contains *weak* passwords...)?

# Your answer here.

### 10.

Which password(s) in the datasets took the shortest time to crack by online guessing? Which took the longest?

# Your answer here.

<hr>
<hr>
<hr>

## Solutions

### 1.

In this set of practice exercises we'll be looking at a cool dataset of real passwords (made available from actual data breaches) sourced and compiled from [Information is Beautiful](https://informationisbeautiful.net/visualizations/top-500-passwords-visualized/?utm_content=buffer994fa&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer) and contributed to [R's Tidy Tuesday project](https://github.com/rfordatascience/tidytuesday). These passwords are common ("bad") passwords that you should avoid using! But we're going to use this dataset to practice some regex skills.

Let's start by importing pandas with the alias `pd`.

import pandas as pd

### 2.

The dataset has the following columns:

|variable          |class     |description |
|:-----------------|:---------|:-----------|
|rank              |int    | popularity in their database of released passwords |
|password          |str | Actual text of the password |
|category          |str | What category does the password fall in to?|
|value             |float    | Time to crack by online guessing |
|time_unit         |str | Time unit to match with value |
|offline_crack_sec |float    | Time to crack offline in seconds |
|rank_alt          |int    | Rank 2 |
|strength          |int    | Strength = quality of password where 10 is highest, 1 is lowest, please note that these are relative to these generally bad passwords |
|font_size         |int    | Used to create the graphic for KIB |


In these exercises, we're only interested in the `password`, `value` and `time_unit` columns so import only these two columns as a dataframe named `df` from this url: <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv>

df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv',
                 usecols=['password', 'value', 'time_unit'],
                 skipfooter = 7,
                 engine='python')
df.head()

### 3.

An online password attack is when someone tries to hack your account by simply trying a very large number of username/password combinations to access your account. For each `password` in our dataset, the `value` column shows the amount of time it is estimated to take an "online password attack" to hack your account. The column `time_unit` shows the units of that time value (e.g., hours, days, years, etc.)

It would be much nicer if our `value`s were of the same units so we can more easily compare the "online password guessing time" for each password. So your first task is to convert all of the values to units of hours (assume the conversion units I've provided below, e.g., 1 day is 24 hours, 1 week is 168 hours, etc).

units = {
    "seconds": 1 / 3600,
    "minutes": 1 / 60,
    "days": 24,
    "weeks": 168,
    "months": 720,
    "years": 8760,
}

for key, val in units.items():
    df.loc[df['time_unit'] == key, 'value'] *= val 

df['time_unit'] = 'hours'
df.head()

### 4.

How many password begin with the sequence `123`?

df['password'].str.contains(r"^123").sum()

### 5.

What is the average time in hours needed to crack these passwords that begin with `123`? How does this compare to the average of all passwords in the dataset?

print(f"Avg. time to crack passwords beginning with 123: {df[df['password'].str.contains(r'^123')]['value'].mean():.0f} hrs")
print(f"Avg. time to crack for all passwords in dataset: {df['value'].mean():.0f} hrs")

### 6.

How many passwords do not contain a number?

df[df['password'].str.contains(r"^[^0-9]*$")].head()

### 7.

How many passwords contain at least one number?

df[df['password'].str.contains(r".*[0-9].*")].head()

### 8.

Is there an obvious difference in online cracking time between passwords that don't contain a number vs passwords that contain at least one number?

print(f"        Avg. time to crack passwords without a number: {df[df['password'].str.contains(r'^[^0-9]*$')]['value'].mean():.0f} hrs")
print(f"Avg. time to crack passwords with at least one number: {df[df['password'].str.contains(r'.*[0-9].*')]['value'].mean():.0f} hrs")

### 9.

How many passwords contain at least one of the following punctuations: `[.!?\\-]` (hint: remember this dataset contains *weak* passwords...)?

df[df['password'].str.contains(r'[.!?\\-]')]

### 10.

Which password(s) in the datasets took the shortest time to crack by online guessing? Which took the longest?

df.query("value == value.min()")

df.query("value == value.max()")