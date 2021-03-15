![](../docs/banner.png)

# Chapter 7: Introduction to Pandas

<h2>Chapter Outline<span class="tocSkip"></span></h2>
<hr>
<div class="toc"><ul class="toc-item"><li><span><a href="#1.-Introduction-to-Pandas" data-toc-modified-id="1.-Introduction-to-Pandas-1">1. Introduction to Pandas</a></span></li><li><span><a href="#2.-Pandas-Series" data-toc-modified-id="2.-Pandas-Series-2">2. Pandas Series</a></span></li><li><span><a href="#3.-Pandas-DataFrames" data-toc-modified-id="3.-Pandas-DataFrames-3">3. Pandas DataFrames</a></span></li><li><span><a href="#4.-Why-ndarrays-and-Series-and-DataFrames?" data-toc-modified-id="4.-Why-ndarrays-and-Series-and-DataFrames?-4">4. Why ndarrays and Series and DataFrames?</a></span></li></ul></div>

## Chapter Learning Objectives
<hr>

- Create Pandas series with `pd.Series()` and Pandas dataframe with `pd.DataFrame()`
- Be able to access values from a Series/DataFrame by indexing, slicing and boolean indexing using notation such as `df[]`, `df.loc[]`, `df.iloc[]`, `df.query[]`
- Perform basic arithmetic operations between two series and anticipate the result.
- Describe how Pandas assigns dtypes to Series and what the `object` dtype is
- Read a standard .csv file from a local path or url using Pandas `pd.read_csv()`.
- Explain the relationship and differences between `np.ndarray`, `pd.Series` and `pd.DataFrame` objects in Python.

## 1. Introduction to Pandas
<hr>

![](img/chapter7/pandas.png)

Pandas is most popular Python library for tabular data structures. You can think of Pandas as an extremely powerful version of Excel (but free and with a lot more features!) 

Pandas can be installed using `conda`:

```
conda install pandas
```

We usually import pandas with the alias `pd`. You'll see these two imports at the top of most data science workflows:

import pandas as pd
import numpy as np

## 2. Pandas Series
<hr>

### What are Series?

A Series is like a NumPy array but with labels. They are strictly 1-dimensional and can contain any data type (integers, strings, floats, objects, etc), including a mix of them. Series can be created from a scalar, a list, ndarray or dictionary using `pd.Series()` (**note the captial "S"**). Here are some example series:

![](img/chapter7/series.png)

### Creating Series

By default, series are labelled with indices starting from 0. For example:

pd.Series(data = [-5, 1.3, 21, 6, 3])

But you can add a custom index:

pd.Series(data = [-5, 1.3, 21, 6, 3],
          index = ['a', 'b', 'c', 'd', 'e'])

You can create a Series from a dictionary:

pd.Series(data = {'a': 10, 'b': 20, 'c': 30})

Or from an ndarray:

pd.Series(data = np.random.randn(3))

Or even a scalar:

pd.Series(3.141)

pd.Series(data=3.141, index=['a', 'b', 'c'])

### Series Characteristics

Series can be given a `name` attribute. I almost never use this but it might come up sometimes:

s = pd.Series(data = np.random.randn(5), name='random_series')
s

s.name

s.rename("another_name")

You can access the index labels of your series using the `.index` attribute:

s.index

You can access the underlying data array using `.to_numpy()`:

s.to_numpy()

pd.Series([[1, 2, 3], "b", 1]).to_numpy()

### Indexing and Slicing Series

Series are very much like ndarrays (in fact, series can be passed to most NumPy functions!). They can be indexed using square brackets `[ ]` and sliced using colon `:` notation:

s = pd.Series(data = range(5),
              index = ['A', 'B', 'C', 'D', 'E'])
s

s[0]

s[[1, 2, 3]]

s[0:3]

Note above how array-based indexing and slicing also returns the series index.

Series are also like dictionaries, in that we can access values using index labels:

s["A"]

s[["B", "D", "C"]]

s["A":"C"]

"A" in s

"Z" in s

Series do allow for non-unique indexing, but **be careful** because indexing operations won't return unique values:

x = pd.Series(data = range(5),
              index = ["A", "A", "A", "B", "C"])
x

x["A"]

Finally, we can also do boolean indexing with series:

s[s >= 1]

s[s > s.mean()]

(s != 1)

### Series Operations

Unlike ndarrays operations between Series (+, -, /, \*) align values based on their **LABELS** (not their position in the structure). The resulting index will be the __*sorted union*__ of the two indexes. This gives you the flexibility to run operations on series regardless of their labels.

s1 = pd.Series(data = range(4),
               index = ["A", "B", "C", "D"])
s1

s2 = pd.Series(data = range(10, 14),
               index = ["B", "C", "D", "E"])
s2

s1 + s2

As you can see above, indices that match will be operated on. Indices that don't match will appear in the product but with `NaN` values:

![](img/chapter7/series_addition.png)

We can also perform standard operations on a series, like multiplying or squaring. NumPy also accepts series as an argument to most functions because series are built off numpy arrays (more on that later):

s1 ** 2

np.exp(s1)

Finally, just like arrays, series have many built-in methods for various operations. You can find them all by running `help(pd.Series)`:

print([_ for _ in dir(pd.Series) if not _.startswith("_")])  # print all common methods

s1

s1.mean()

s1.sum()

s1.astype(float)

**"Chaining"** operations together is also common with pandas:

s1.add(3.141).pow(2).mean().astype(int)

### Data Types

Series can hold all the data types (`dtypes`) you're used to, e.g., `int`, `float`, `bool`, etc. There are a few other special data types too (`object`, `DateTime` and `Categorical`) which we'll talk about in this and later chapters. You can always read more about pandas dtypes [in the documentation too](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#dtypes). For example, here's a series of `dtype` int64:

x = pd.Series(range(5))
x.dtype

The dtype "`object`" is used for series of strings or mixed data. Pandas is [currently experimenting](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.StringDtype.html#pandas.StringDtype) with a dedicated string dtype `StringDtype`, but it is still in testing.

x = pd.Series(['A', 'B'])
x

x = pd.Series(['A', 1, ["I", "AM", "A", "LIST"]])
x

While flexible, it is recommended to avoid the use of `object` dtypes because of higher memory requirements. Essentially, in an `object` dtype series, every single element stores information about its individual dtype. We can inspect the dtypes of all the elements in a mixed series in several ways, below I'll use the `map` method:

x.map(type)

We can see that each object in our series has a different dtype. This comes at a cost. Compare the [memory usage](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.memory_usage.html) of the series below:

x1 = pd.Series([1, 2, 3])
print(f"x1 dtype: {x1.dtype}")
print(f"x1 memory usage: {x1.memory_usage(deep=True)} bytes")
print("")
x2 = pd.Series([1, 2, "3"])
print(f"x2 dtype: {x2.dtype}")
print(f"x2 memory usage: {x2.memory_usage(deep=True)} bytes")
print("")
x3 = pd.Series([1, 2, "3"]).astype('int8')  # coerce the object series to int8
print(f"x3 dtype: {x3.dtype}")
print(f"x3 memory usage: {x3.memory_usage(deep=True)} bytes")

In summary, try to use uniform dtypes where possible - they are more memory efficient!

One more gotcha, `NaN` (frequently used to represent missing values in data) is a float:

type(np.NaN)

This can be problematic if you have a series of integers and one missing value, because Pandas will cast the whole series to a float:

pd.Series([1, 2, 3, np.NaN])

Only recently, Pandas has implemented a "[nullable integer dtype](https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html)", which can handle `NaN` in an integer series without affecting the `dtype`. Note the captial "I" in the type below, differentiating it from numpy's `int64` dtype:

pd.Series([1, 2, 3, np.NaN]).astype('Int64')

This is not the default in Pandas yet and functionality of this new feature is still subject to change.

## 3. Pandas DataFrames
<hr>

### What are DataFrames?

Pandas DataFrames are you're new best friend. They are like the Excel spreadsheets you may be used to. DataFrames are really just Series stuck together! Think of a DataFrame as a dictionary of series, with the "keys" being the column labels and the "values" being the series data:

![](img/chapter7/dataframe.png)

### Creating DataFrames

Dataframes can be created using `pd.DataFrame()` (note the capital "D" and "F"). Like series, index and column labels of dataframes are labelled starting from 0 by default:

pd.DataFrame([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

We can use the `index` and `columns` arguments to give them labels:

pd.DataFrame([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             index = ["R1", "R2", "R3"],
             columns = ["C1", "C2", "C3"])

There are so many ways to create dataframes. I most often create them from dictionaries or ndarrays:

pd.DataFrame({"C1": [1, 2, 3],
              "C2": ['A', 'B', 'C']},
             index=["R1", "R2", "R3"])

pd.DataFrame(np.random.randn(5, 5),
             index=[f"row_{_}" for _ in range(1, 6)],
             columns=[f"col_{_}" for _ in range(1, 6)])

pd.DataFrame(np.array([['Tom', 7], ['Mike', 15], ['Tiffany', 3]]))

Here's a table of the main ways you can create dataframes (see the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe) for more):

|Create DataFrame from|Code|
|---|---|
|Lists of lists|`pd.DataFrame([['Tom', 7], ['Mike', 15], ['Tiffany', 3]])`|
|ndarray|`pd.DataFrame(np.array([['Tom', 7], ['Mike', 15], ['Tiffany', 3]]))`|
|Dictionary|`pd.DataFrame({"Name": ['Tom', 'Mike', 'Tiffany'], "Number": [7, 15, 3]})`|
|List of tuples|`pd.DataFrame(zip(['Tom', 'Mike', 'Tiffany'], [7, 15, 3]))`|
|Series|`pd.DataFrame({"Name": pd.Series(['Tom', 'Mike', 'Tiffany']), "Number": pd.Series([7, 15, 3])})`|


### Indexing and Slicing DataFrames

There are several main ways to select data from a DataFrame:
1. `[]`
2. `.loc[]`
3. `.iloc[]`
4. Boolean indexing
5. `.query()`

df = pd.DataFrame({"Name": ["Tom", "Mike", "Tiffany"],
                   "Language": ["Python", "Python", "R"],
                   "Courses": [5, 4, 7]})
df

#### Indexing with `[]`
Select columns by single labels, lists of labels, or slices:

df['Name']  # returns a series

df[['Name']]  # returns a dataframe!

df[['Name', 'Language']]

You can only index rows by using slices, not single values (but not recommended, see preferred methods below).

df[0] # doesn't work

df[0:1] # does work

df[1:] # does work

#### Indexing with `.loc` and `.iloc`
Pandas created the methods `.loc[]` and `.iloc[]` as more flexible alternatives for accessing data from a dataframe. Use `df.iloc[]` for indexing with integers and `df.loc[]` for indexing with labels. These are typically the [recommended methods of indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated) in Pandas.

df

First we'll try out `.iloc` which accepts *integers* as references to rows/columns:

df.iloc[0]  # returns a series

df.iloc[0:2]  # slicing returns a dataframe

df.iloc[2, 1]  # returns the indexed object

df.iloc[[0, 1], [1, 2]]  # returns a dataframe

Now let's look at `.loc` which accepts *labels* as references to rows/columns:

df.loc[:, 'Name']

df.loc[:, 'Name':'Language']

df.loc[[0, 2], ['Language']]

Sometimes we want to use a mix of integers and labels to reference data in a dataframe. The easiest way to do this is to use `.loc[]` with a label then use an integer in combinations with `.index` or `.columns`:

df.index

df.columns

df.loc[df.index[0], 'Courses']  # I want to reference the first row and the column named "Courses"

df.loc[2, df.columns[1]]  # I want to reference row "2" and the second column

#### Boolean indexing
Just like with series, we can select data based on boolean masks:

df

df[df['Courses'] > 5]

df[df['Name'] == "Tom"]

#### Indexing with `.query()`
Boolean masks work fine, but I prefer to use the `.query()` method for selecting data. `df.query()` is a powerful tool for filtering data. It has an odd syntax, one of the strangest I've seen in Python, it is more like SQL - `df.query()` accepts a string expression to evaluate and it "knows" the names of the columns in your dataframe.

df.query("Courses > 4 & Language == 'Python'")

Note the use of single quotes AND double quotes above, lucky we have both in Python! Compare this to the equivalent boolean indexing operation and you can see that `.query()` is much more readable, especially as the query gets bigger!

df[(df['Courses'] > 4) & (df['Language'] == 'Python')]

Query also allows you to reference variable in the current workspace using the `@` symbol:

course_threshold = 4
df.query("Courses > @course_threshold")

#### Indexing cheatsheet

|Method|Syntax|Output|
|---|---|---|
|Select column|`df[col_label]`|Series|
|Select row slice|`df[row_1_int:row_2_int]`|DataFrame|
|Select row/column by label|`df.loc[row_label(s), col_label(s)]`|Object for single selection, Series for one row/column, otherwise DataFrame|
|Select row/column by integer|`df.iloc[row_int(s), col_int(s)]`|Object for single selection, Series for one row/column, otherwise DataFrame|
|Select by row integer & column label|`df.loc[df.index[row_int], col_label]`|Object for single selection, Series for one row/column, otherwise DataFrame|
|Select by row label & column integer|`df.loc[row_label, df.columns[col_int]]`|Object for single selection, Series for one row/column, otherwise DataFrame|
|Select by boolean|`df[bool_vec]`|Object for single selection, Series for one row/column, otherwise DataFrame|
|Select by boolean expression|`df.query("expression")`|Object for single selection, Series for one row/column, otherwise DataFrame|

### Reading/Writing Data From External Sources

#### .csv files

A lot of the time you will be loading .csv files for use in pandas. You can use the `pd.read_csv()` function for this. In the following chapters we'll use a real dataset of my cycling commutes to the University of British Columbia. There are so many arguments that can be used to help read in your .csv file in an efficient and appropriate manner, feel free to check them out now (by using `shift + tab` in Jupyter, or typing `help(pd.read_csv)`).

path = 'data/cycling_data.csv'
df = pd.read_csv(path, index_col=0, parse_dates=True)
df

You can print a dataframe to .csv using `df.to_csv()`. Be sure to check out all of the possible arguments to write your dataframe exactly how you want it.

#### url

Pandas also facilitates reading directly from a url - `pd.read_csv()` accepts urls as input:

url = 'https://raw.githubusercontent.com/TomasBeuzen/toy-datasets/master/wine_1.csv'
pd.read_csv(url)

#### Other
Pandas can read data from all sorts of other file types including HTML, JSON, Excel, Parquet, Feather, etc. There are generally dedicated functions for reading these file types, see the [Pandas documentation here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-tools-text-csv-hdf5).

### Common DataFrame Operations

DataFrames have built-in functions for performing most common operations, e.g., `.min()`, `idxmin()`, `sort_values()`, etc. They're all documented in the [Pandas documentation here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) but I'll demonstrate a few below:

df = pd.read_csv('data/cycling_data.csv')
df

df.min()

df['Time'].min()

df['Time'].idxmin()

df.iloc[20]

df.sum()

Some methods like `.mean()` will only operate on numeric columns:

df.mean()

Some methods require arguments to be specified, like `.sort_values()`:

df.sort_values(by='Time')

df.sort_values(by='Time', ascending=False)

Some methods will operate on the index/columns, like `.sort_index()`:

df.sort_index(ascending=False)

## 4. Why ndarrays and Series and DataFrames?

At this point, you might be asking why we need all these different data structures. Well, they all serve different purposes and are suited to different tasks. For example:
- NumPy is typically faster/uses less memory than Pandas;
- not all Python packages are compatible with NumPy & Pandas;
- the ability to add labels to data can be useful (e.g., for time series);
- NumPy and Pandas have different built-in functions available.

My advice: use the simplest data structure that fulfills your needs!

Finally, we've seen how to go from: ndarray (`np.array()`) -> series (`pd.series()`) -> dataframe (`pd.DataFrame()`). Remember that we can also go the other way: dataframe/series -> ndarray using `df.to_numpy()`.