![](../docs/banner.png)

# Chapter 9: Advanced Data Wrangling With Pandas

<h2>Chapter Outline<span class="tocSkip"></span></h2>
<hr>
<div class="toc"><ul class="toc-item"><li><span><a href="#1.-Working-With-Strings" data-toc-modified-id="1.-Working-With-Strings-2">1. Working With Strings</a></span></li><li><span><a href="#2.-Working-With-Datetimes" data-toc-modified-id="2.-Working-With-Datetimes-3">2. Working With Datetimes</a></span></li><li><span><a href="#3.-Hierachical-Indexing" data-toc-modified-id="3.-Hierachical-Indexing-4">3. Hierachical Indexing</a></span></li><li><span><a href="#4.-Visualizing-DataFrames" data-toc-modified-id="4.-Visualizing-DataFrames-5">4. Visualizing DataFrames</a></span></li><li><span><a href="#5.-Pandas-Profiling" data-toc-modified-id="5.-Pandas-Profiling-6">5. Pandas Profiling</a></span></li></ul></div>

## Chapter Learning Objectives
<hr>

- Manipulate strings in Pandas by accessing methods from the `Series.str` attribute.
- Understand how to use regular expressions in Pandas for wrangling strings.
- Differentiate between datetime object in Pandas such as `Timestamp`, `Timedelta`, `Period`, `DateOffset`.
- Create these datetime objects with functions like `pd.Timestamp()`, `pd.Period()`, `pd.date_range()`, `pd.period_range()`.
- Index a datetime index with partial string indexing.
- Perform basic datetime operations like splitting a datetime into constituent parts (e.g., `year`, `weekday`, `second`, etc), apply offsets, change timezones, and resample with `.resample()`.
- Make basic plots in Pandas by accessing the `.plot` attribute or importing functions from `pandas.plotting`.

## 1. Working With Strings
<hr>

import pandas as pd
import numpy as np
pd.set_option("display.max_rows", 20)

Working with text data is common in data science. Luckily, Pandas Series and Index objects are equipped with a set of string processing methods which we'll explore here.

### String dtype

String data is represented in pandas using the `object` dtype, which is a generic dtype for representing mixed data or data of unknown size. It would be better to have a dedicated dtype and Pandas has just introduced this: the `StringDtype`. `object` remains the default dtype for strings however, as Pandas looks to continue testing and improving the `string` dtype. You can read more about the `StringDtype` in the [Pandas documentation here](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html#text-data-types).

### String Methods

We've seen how libraries like NumPy and Pandas can vectorise operations for increased speed and useability:

x = np.array([1, 2, 3, 4, 5])
x * 2

This is not the case for arrays of strings however:

x = np.array(['Tom', 'Mike', 'Tiffany', 'Joel', 'Varada'])
x.upper()

Instead, you would have to operate on each string object one at a time, using a loop for example:

[name.upper() for name in x]

But even this will fail if your array contains a missing value:

x = np.array(['Tom', 'Mike', None, 'Tiffany', 'Joel', 'Varada'])
[name.upper() for name in x]

Pandas addresses both of these issues (vectorization and missing values) with its string methods. String methods can be accessed by the `.str` attribute of Pandas Series and Index objects. Pretty much all built-in string operations (`.upper()`, `.lower()`, `.split()`, etc) and more are available.

s = pd.Series(x)
s

s.str.upper()

s.str.split("ff", expand=True)

s.str.len()

We can also operate on Index objects (i.e., index or column labels):

df = pd.DataFrame(np.random.rand(5, 3),
                  columns = ['Measured Feature', 'recorded feature', 'PredictedFeature'],
                  index = [f"ROW{_}" for _ in range(5)])
df

type(df.columns)

Let's clean up those labels by:
1. Removing the word "feature" and "Feature"
2. Lowercase the "ROW" and add an underscore between the digit and letters

df.columns = df.columns.str.capitalize().str.replace("feature", "").str.strip()

df.index = df.index.str.lower().str.replace("w", "w_")

df

Great that worked! There are so many string operations you can use in Pandas. Here's a full list of all the string methods available in Pandas that I pulled from the documentation:

| Method                     | Description                                                                                                                       |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `Series.str.cat`           | Concatenate strings                                                                                                               |
| `Series.str.split`         | Split strings on delimiter                                                                                                        |
| `Series.str.rsplit`        | Split strings on delimiter working from the end of the string                                                                     |
| `Series.str.get`           | Index into each element (retrieve i-th element)                                                                                   |
| `Series.str.join`          | Join strings in each element of the Series with passed separator                                                                  |
| `Series.str.get_dummies`   | Split strings on the delimiter returning DataFrame of dummy variables                                                             |
| `Series.str.contains`      | Return boolean array if each string contains pattern/regex                                                                        |
| `Series.str.replace`       | Replace occurrences of pattern/regex/string with some other string or the return value of a callable given the occurrence         |
| `Series.str.repeat`        | Duplicate values (`s.str.repeat(3)` equivalent to `x * 3`)                                                                        |
| `Series.str.pad`           | "Add whitespace to left, right, or both sides of strings"                                                                         |
| `Series.str.center`        | Equivalent to `str.center`                                                                                                        |
| `Series.str.ljust`         | Equivalent to `str.ljust`                                                                                                         |
| `Series.str.rjust`         | Equivalent to `str.rjust`                                                                                                         |
| `Series.str.zfill`         | Equivalent to `str.zfill`                                                                                                         |
| `Series.str.wrap`          | Split long strings into lines with length less than a given width                                                                 |
| `Series.str.slice`         | Slice each string in the Series                                                                                                   |
| `Series.str.slice_replace` | Replace slice in each string with passed value                                                                                    |
| `Series.str.count`         | Count occurrences of pattern                                                                                                      |
| `Series.str.startswith`    | Equivalent to `str.startswith(pat)` for each element                                                                              |
| `Series.str.endswith`      | Equivalent to `str.endswith(pat)` for each element                                                                                |
| `Series.str.findall`       | Compute list of all occurrences of pattern/regex for each string                                                                  |
| `Series.str.match`         | "Call `re.match` on each element, returning matched groups as list"                                                               |
| `Series.str.extract`       | "Call `re.search` on each element, returning DataFrame with one row for each element and one column for each regex capture group" |
| `Series.str.extractall`    | "Call `re.findall` on each element, returning DataFrame with one row for each match and one column for each regex capture group"  |
| `Series.str.len`           | Compute string lengths                                                                                                            |
| `Series.str.strip`         | Equivalent to `str.strip`                                                                                                         |
| `Series.str.rstrip`        | Equivalent to `str.rstrip`                                                                                                        |
| `Series.str.lstrip`        | Equivalent to `str.lstrip`                                                                                                        |
| `Series.str.partition`     | Equivalent to `str.partition`                                                                                                     |
| `Series.str.rpartition`    | Equivalent to `str.rpartition`                                                                                                    |
| `Series.str.lower`         | Equivalent to `str.lower`                                                                                                         |
| `Series.str.casefold`      | Equivalent to `str.casefold`                                                                                                      |
| `Series.str.upper`         | Equivalent to `str.upper`                                                                                                         |
| `Series.str.find`          | Equivalent to `str.find`                                                                                                          |
| `Series.str.rfind`         | Equivalent to `str.rfind`                                                                                                         |
| `Series.str.index`         | Equivalent to `str.index`                                                                                                         |
| `Series.str.rindex`        | Equivalent to `str.rindex`                                                                                                        |
| `Series.str.capitalize`    | Equivalent to `str.capitalize`                                                                                                    |
| `Series.str.swapcase`      | Equivalent to `str.swapcase`                                                                                                      |
| `Series.str.normalize`     | Return Unicode normal form. Equivalent to `unicodedata.normalize`                                                                 |
| `Series.str.translate`     | Equivalent to `str.translate`                                                                                                     |
| `Series.str.isalnum`       | Equivalent to `str.isalnum`                                                                                                       |
| `Series.str.isalpha`       | Equivalent to `str.isalpha`                                                                                                       |
| `Series.str.isdigit`       | Equivalent to `str.isdigit`                                                                                                       |
| `Series.str.isspace`       | Equivalent to `str.isspace`                                                                                                       |
| `Series.str.islower`       | Equivalent to `str.islower`                                                                                                       |
| `Series.str.isupper`       | Equivalent to `str.isupper`                                                                                                       |
| `Series.str.istitle`       | Equivalent to `str.istitle`                                                                                                       |
| `Series.str.isnumeric`     | Equivalent to `str.isnumeric`                                                                                                     |
| `Series.str.isdecimal`     | Equivalent to `str.isdecimal`                                                                                                     |

I will also mention that I often use the dataframe method `df.replace()` to do string replacements:

df = pd.DataFrame({'col1': ['replace me', 'b', 'c'],
                   'col2': [1, 99999, 3]})
df

df.replace({'replace me': 'a',
            99999: 2})

### Regular Expressions

A regular expression (regex) is a sequence of characters that defines a search pattern. For more complex string operations, you'll definitely want to use regex. [Here's a great cheatsheet](https://www.rexegg.com/regex-quickstart.html) of regular expression syntax. I am self-admittedly not a regex expert, I usually jump over to [RegExr.com](https://regexr.com/) and play around until I find the expression I want. Many Pandas string functions accept regular expressions as input, these are the ones I use most often:

|Method|Description|
|---|---|
|`match()`|Call re.match() on each element, returning a boolean.
|`extract()`|Call re.match() on each element, returning matched groups as strings.
|`findall()`|Call re.findall() on each element
|`replace()`|Replace occurrences of pattern with some other string
|`contains()`|Call re.search() on each element, returning a boolean
|`count()`|Count occurrences of pattern
|`split()`|Equivalent to str.split(), but accepts regexps
|`rsplit()`|Equivalent to str.rsplit(), but accepts regexps

For example, we can easily find all names in our Series that start and end with a consonant:

s = pd.Series(['Tom', 'Mike', None, 'Tiffany', 'Joel', 'Varada'])
s

s.str.findall(r'^[^AEIOU].*[^aeiou]$')

Let's break down that regex:

|Part|Description|
|---|---|
|`^`|Specifies the start of a string|
|`[^AEIOU]`|Square brackets match a single character. When `^` is used inside square brackets it means "not", so we are are saying, "the first character of the string should not be A, E, I, O, or U (i.e., a vowel)"|
|`.*`|`.` matches any character and `*` means "0 or more time", this is basically saying that we can have any number of characters in the middle of our string|
|`[^aeiou]$`| `$` matches the end of the string, so we are saying, we don't want the last character to be a lowercase vowel|

Regex can do some truly magical things so keep it in mind when you're doing complicated text wrangling. Let's see one more example on the cycling dataset:

df = pd.read_csv('data/cycling_data.csv', index_col=0)
df

We could find all the comments that contains the string "Rain" or "rain":

df.loc[df['Comments'].str.contains(r"[Rr]ain")]

If we didn't want to include "Raining" or "raining", we could do:

df.loc[df['Comments'].str.contains(r"^[Rr]ain$")]

We can even split strings and separate them into new columns, for example, based on punctuation:

df['Comments'].str.split(r"[.,!]", expand=True)

My point being here that you can pretty much do anything your heart desires!

## 2. Working With Datetimes
<hr>

Just like with strings, Pandas has extensive functionality for working with time series data.

### Datetime dtype and Motivation for Using Pandas

Python has built-in support for datetime format, that is, an object that contains time and date information, in the `datetime` module.

from datetime import datetime, timedelta

date = datetime(year=2005, month=7, day=9, hour=13, minute=54)
date

We can also parse directly from a string, see [format codes here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes):

date = datetime.strptime("July 9 2005, 13:54", "%B %d %Y, %H:%M")
date

We can then extract specific information from our data:

print(f"Year: {date.strftime('%Y')}")
print(f"Month: {date.strftime('%B')}")
print(f"Day: {date.strftime('%d')}")
print(f"Day name: {date.strftime('%A')}")
print(f"Day of year: {date.strftime('%j')}")
print(f"Time of day: {date.strftime('%p')}")

And perform basic operations, like adding a week:

date + timedelta(days=7)

But as with strings, working with arrays of datetimes in Python can be difficult and inefficient. NumPy, therefore included a new datetime object to work more effectively with dates:

dates = np.array(["2020-07-09", "2020-08-10"], dtype="datetime64")
dates

We can create arrays using other built-in functions like `np.arange()` too:

dates = np.arange("2020-07", "2020-12", dtype='datetime64[M]')
dates

Now we can easily do operations on arrays of time. You can check out all the datetime units and their format in the documentation [here](https://numpy.org/doc/stable/reference/arrays.datetime.html#datetime-units).

dates +  np.timedelta64(2, 'M')

But while numpy helps bring datetimes into the array world, it's missing a lot of functionality that we would commonly want/need for wrangling tasks. This is where Pandas comes in. Pandas consolidates and extends functionality from the `datetime` module, `numpy`, and other libraries like `scikits.timeseries` into a single place. Pandas provides 4 key datetime objects which we'll explore in the following sections:
1. Timestamp (like np.datetime64)
2. Timedelta (like np.timedelta64)
3. Period (custom object for regular ranges of datetimes)
4. DateOffset (custom object like timedelta but factoring in calendar rules)

### Creating Datetimes

#### From scratch

Most commonly you'll want to:
1. Create a single point in time with `pd.Timestamp()`, e.g., `2005-07-09 00:00:00`
2. Create a span of time with `pd.Period()`, e.g., `2020 Jan`
3. Create an array of datetimes with `pd.date_range()` or `pd.period_range()`

print(pd.Timestamp('2005-07-09'))  # parsed from string
print(pd.Timestamp(year=2005, month=7, day=9))  # pass data directly
print(pd.Timestamp(datetime(year=2005, month=7, day=9)))  # from datetime object

The above is a specific point in time. Below, we can use `pd.Period()` to specify a span of time (like a day):

span = pd.Period('2005-07-09')
print(span)
print(span.start_time)
print(span.end_time)

point = pd.Timestamp('2005-07-09 12:00')
span = pd.Period('2005-07-09')
print(f"Point: {point}")
print(f" Span: {span}")
print(f"Point in span? {span.start_time < point < span.end_time}")

Often, you'll want to create arrays of datetimes, not just single values. Arrays of datetimes are of the class `DatetimeIndex`/`PeriodIndex`/`TimedeltaIndex`:

pd.date_range('2020-09-01 12:00',
              '2020-09-11 12:00',
              freq='D')

pd.period_range('2020-09-01',
                '2020-09-11',
                freq='D')

We can use `Timedelta` objects to perform temporal operations like adding or subtracting time:

pd.date_range('2020-09-01 12:00', '2020-09-11 12:00', freq='D') + pd.Timedelta('1.5 hour')

Finally, Pandas represents missing datetimes with `NaT`, which is just like `np.nan`:

pd.Timestamp(pd.NaT)

#### By converting existing data

It's fairly common to have an array of dates as strings. We can use `pd.to_datetime()` to convert these to datetime:

string_dates = ['July 9, 2020', 'August 1, 2020', 'August 28, 2020']
string_dates

pd.to_datetime(string_dates)

For more complex datetime format, use the `format` argument (see [Python Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for help):

string_dates = ['2020 9 July', '2020 1 August', '2020 28 August']
pd.to_datetime(string_dates, format="%Y %d %B")

Or use a dictionary:

dict_dates = pd.to_datetime({"year": [2020, 2020, 2020],
                             "month": [7, 8, 8],
                             "day": [9, 1, 28]})  # note this is a series, not an index!
dict_dates

pd.Index(dict_dates)

#### By reading directly from an external source

Let's practice by reading in our favourite cycling dataset:

df = pd.read_csv('data/cycling_data.csv', index_col=0)
df

Our index is just a plain old index at the moment, with dtype `object`, full of `string` dates:

print(df.index.dtype)
type(df.index)

We could manually convert our index to a datetime using `pd.to_datetime()`. But even better, `pd.read_csv()` has an argument `parse_dates` which can do this automatically when reading the file:

df = pd.read_csv('data/cycling_data.csv', index_col=0, parse_dates=True)
df

type(df.index)

print(df.index.dtype)
type(df.index)

The `parse_dates` argument is very flexible and you can specify the datetime format for harder to read dates. There are other related arguments like `date_parser`, `dayfirst`, etc that are also helpful, check out the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) for more.

### Indexing Datetimes

Datetime index objects are just like regular Index objects and can be selected, sliced, filtered, etc.

df

We can do partial string indexing:

df.loc['2019-09']

Exact matching:

df.loc['2019-10-10']

df.loc['2019-10-10 13:47:14']

And slicing:

df.loc['2019-10-01':'2019-10-13']

`df.query()` will also work here:

df.query("'2019-10-10'")

And for getting all results between two times of a day, use `df.between_time()`:

df.between_time('00:00', '01:00')

For more complicated filtering, we may have to decompose our timeseries, as we'll shown in the next section.

### Manipulating Datetimes

#### Decomposition

We can easily decompose our timeseries into its constituent components. There are [many attributes](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components) that define these constituents.

df.index.year

df.index.second

df.index.weekday

As well as methods we can use:

df.index.day_name()

df.index.month_name()

Note that if you're operating on a Series rather than a DatetimeIndex object, you can access this functionality through the `.dt` attribute:

s = pd.Series(pd.date_range('2011-12-29', '2011-12-31'))
s.year  # raises error

s.dt.year  # works

#### Offsets and Timezones

We saw before how we can use `Timedelta` to add/subtract time to our datetimes. `Timedelta` respects absolute time, which can be problematic in some cases, where time is not regular. For example, on March 8, Canada daylight savings started and clocks **moved forward 1 hour**. This extra "calendar hour" is not accounted for in absolute time:

t1 = pd.Timestamp('2020-03-07 12:00:00', tz='Canada/Pacific')
t2 = t1 + pd.Timedelta("1 day")
print(f"Original time: {t1}")
print(f" Plus one day: {t2}")  # note that time has moved from 12:00 -> 13:00

Instead, we'd need to use a `Dateoffset`:

t3 = t1 + pd.DateOffset(days=1)
print(f"Original time: {t1}")
print(f" Plus one day: {t3}")  # note that time has stayed at 12:00

You can see that we started including timezone information above. By default, datetime objects are "timezone unaware". To associate times with a timezone, we can use the `tz` argument in construction, or we can use the `tz_localize()` method:

print(f"        No timezone: {pd.Timestamp('2020-03-07 12:00:00').tz}")
print(f"             tz arg: {pd.Timestamp('2020-03-07 12:00:00', tz='Canada/Pacific').tz}")
print(f".tz_localize method: {pd.Timestamp('2020-03-07 12:00:00').tz_localize('Canada/Pacific').tz}")

You can convert between timezones using the `.tz_convert()` method. You might have noticed something funny about the times I've been riding to University:

df = pd.read_csv('data/cycling_data.csv', index_col=0, parse_dates=True)
df

I know for a fact that I haven't been cycling around midnight... There's something wrong with the timezone in this dataset. I was using the `Strava` app to document my rides, it was recording in Canadian time but converting to Australia time. Let's go ahead and fix that up:

df.index = df.index.tz_localize("Canada/Pacific")  # first specify the current timezone
df.index = df.index.tz_convert("Australia/Sydney")  # then convert to the proper timezone
df

We could have also used a `DateOffset` if we knew the offset we wanted to apply, in this case, 7 hours:

df = pd.read_csv('data/cycling_data.csv', index_col=0, parse_dates=True)
df.index = df.index + pd.DateOffset(hours=-7)
df

#### Resampling and Aggregating

One of the most common operations you will want do when working with time series is resampling the time series to a coarser/finer/regular resolution. For example, you may want to resample daily data to weekly data. We can do that with the `.resample()` method. For example, let's resample my irregular cycling timeseries to a regular 12-hourly series:

df.index

df.resample("1D")

`Resampler` objects are very similar to the `groupby` objects we saw in the previous chapter. We need to apply an aggregating function on our grouped timeseries, just like we did with `groupby` objects:

dfr = df.resample("1D").mean()
dfr

There's quite a few `NaN`s in there? Some days I didn't ride, but some might by weekends too...

dfr['Weekday'] = dfr.index.day_name()
dfr.head(10)

Pandas support "business time" operations and format codes in all the timeseries functions we've seen so far. You can check out [the documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html) for more info, but let's specify business days here to get rid of those weekends:

dfr = df.resample("1B").mean()  # "B" is business day
dfr['Weekday'] = dfr.index.day_name()
dfr.head(10)

## 3. Hierachical Indexing
<hr>

**Hierachical indexing**, sometimes called "multi-indexing" or "stacked indexing", is how Pandas "nests" data. The idea is to facilitate the storage of high dimensional data in a 2D dataframe.

![](img/chapter9/pandas_stacking.gif)

Source: [Giphy](https://giphy.com/gifs/panda-playing-QoCoLo2opwUW4)

### Creating a Hierachical Index

Let's start with a motivating example. Say you want to track how many courses each Master of Data Science instructor taught over the years in a Pandas Series.

```{note}
Recall that the content of this site is adapted from material I used to teach the 2020/2021 offering of the course "DSCI 511 Python Programming for Data Science" for the University of British Columbia's Master of Data Science Program.
```

We could use a tuple to make an appropriate index:

index = [('Tom', 2019), ('Tom', 2020),
         ('Mike', 2019), ('Mike', 2020),
         ('Tiffany', 2019), ('Tiffany', 2020)]
courses = [4, 6, 5, 5, 6, 3]
s = pd.Series(courses, index)
s

We can still kind of index this series:

s.loc[("Tom", 2019):("Tom", 2019)]

But if we wanted to get all of the values for 2019, we'd need to do some messy looping:

s[[i for i in s.index if i[1] == 2019]]

The better way to set up this problem is with a multi-index ("hierachical index"). We can create a multi-index with `pd.MultiIndex.from_tuple()`. There are [other variations](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.html) of `.from_X` but tuple is most common.

mi = pd.MultiIndex.from_tuples(index)
mi

s = pd.Series(courses, mi)
s

Now we can do more efficient and logical indexing:

s.loc['Tom']

s.loc[:, 2019]

s.loc["Tom", 2019]

We could also create the index by passing iterables like a list of lists directly to the `index` argument, but I feel it's not as explicit or intutitive as using `pd.MultIndex`:

index = [['Tom', 'Tom', 'Mike', 'Mike', 'Tiffany', 'Tiffany'],
         [2019, 2020, 2019, 2020, 2019, 2020]]
courses = [4, 6, 5, 5, 6, 3]
s = pd.Series(courses, index)
s

### Stacking / Unstacking

You might have noticed that we could also represent our multi-index series as a dataframe. Pandas noticed this too and provides the `.stack()` and `.unstack()` methods for switching between dataframes and multi-index series:

s = s.unstack()
s

s.stack()

### Using a Hierachical Index

Observing the multi-index <-> dataframe equivalence above, you might wonder why we would even want multi-indices. Above, we were only dealing with 2D data, but a multi-index allows us to store any arbitrary number of dimensions:

index = [['Tom', 'Tom', 'Mike', 'Mike', 'Tiffany', 'Tiffany'],
         [2019, 2020, 2019, 2020, 2019, 2020]]
courses = [4, 6, 5, 5, 6, 3]
s = pd.Series(courses, index)
s

pd.DataFrame(s).stack()

s.loc['Tom']

tom = pd.DataFrame({"Courses": [4, 6],
                    "Students": [273, 342]},
                    index = [2019, 2020])
mike = pd.DataFrame({"Courses": [5, 5],
                     "Students": [293, 420]},
                     index = [2019, 2020])
tiff = pd.DataFrame({"Courses": [6, 3],
                     "Students": [363, 190]},
                     index = [2019, 2020])

Here I have three 2D dataframes that I'd like to join together. There are so many ways you can do this, but I'm going to use `pd.concat()` and then specify the `keys` argument:

s3 = pd.concat((tom, mike, tiff),
               keys= ['Tom', 'Mike', 'Tiff'],
               axis=0)
s3

Now we have 3 dimensions of information in a single structure!

s3.stack()

s3.loc['Tom']

s3.loc['Tom', 2019]

We can access deeper levels in various ways:

s3.loc['Tom', 2019]['Courses']

s3.loc[('Tom', 2019), 'Courses']

s3.loc[('Tom', 2019), 'Courses']

If we name our index columns, we can also use `.query()`:

s3 = s3.rename_axis(index=["Name", "Year"])
s3

s3.query("Year == 2019")

Or you might prefer the "stacked" version of our hierachical index:

s3.stack()

s3.stack().loc[('Tom', 2019, 'Courses')]

By the way, we can also use all the previous methods we've learned about on hierachical dataframes:

s3.sort_index(ascending=False)

s3.sort_values(by='Students')

There's one important exception! We can now specify a `level` argument to chose which level of our multi-index to apply the function to:

s3.mean()

s3.mean(level='Year')

## 4. Visualizing DataFrames
<hr>

Pandas provides a `.plot()` method on Series and DataFrames which I wanted to show briefly here.

### Simple Plots

df = pd.read_csv('data/cycling_data.csv', index_col=0, parse_dates=True).dropna()

Let's go ahead and make a plot of the distances I've ridden:

df['Distance'].plot.line();

Cumulative distance might be more informative:

df['Distance'].cumsum().plot.line();

There are many configuration options for these plots which build of the `matplotlib` library:

df['Distance'].cumsum().plot.line(fontsize=14, linewidth = 2, color = 'r', ylabel="km");

I actually usually use built-in themes for my plots which do a lot of the colour and text formatting for you:

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16,
                     'axes.labelweight': 'bold',
                     'figure.figsize': (8,6)})

df['Distance'].dropna().cumsum().plot.line(ylabel="km");

Some people have also made custom themes, like this fun [cyberpunk theme](https://github.com/dhaitz/mplcyberpunk):

import mplcyberpunk
plt.style.use("cyberpunk")

df['Distance'].plot.line(ylabel="km")
mplcyberpunk.add_glow_effects()

There are many other kinds of plots you can make too:

|Method|Plot Type|
|---|---|
|`bar` or `barh` | bar plots|
|`hist` | histogram|
|`box` | boxplot|
|`kde` or `density` | density plots|
|`area` | area plots|
|`scatter` | scatter plots|
|`hexbin` | hexagonal bin plots|
|`pie` | pie plots|

plt.style.use('ggplot')
plt.rcParams.update({'font.size': 16,
                     'axes.labelweight': 'bold',
                     'figure.figsize': (8,6)})
df['Distance'].plot.hist();

df['Distance'].plot.density();

### Pandas Plotting

Pandas also supports a few more advanced plotting functions in the `pandas.plotting` module. You can view them in the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#plotting-tools).

from pandas.plotting import scatter_matrix

scatter_matrix(df);

We have an outlier time in the data above, a time value of ~48,000. Let's remove it and re-plot.

scatter_matrix(df.query('Time < 4000'), alpha=1);

## 5. Pandas Profiling

Pandas profiling is a nifty tool for generating summary reports and doing exploratory data analysis on dataframes. [Pandas profiling](https://github.com/pandas-profiling/pandas-profiling) is not part of base Pandas but you can install with: 

```
$ conda install -c conda-forge pandas-profiling
```

import pandas_profiling
df = pd.read_csv('data/cycling_data.csv')
df.profile_report(progress_bar=False)