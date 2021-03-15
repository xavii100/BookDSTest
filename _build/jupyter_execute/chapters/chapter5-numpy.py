![](../docs/banner.png)

# Chapter 5: Introduction to NumPy

<h2>Chapter Outline<span class="tocSkip"></span></h2>
<hr>
<div class="toc"><ul class="toc-item"><li><span><a href="#1.-Introduction-to-NumPy" data-toc-modified-id="1.-Introduction-to-NumPy-1">1. Introduction to NumPy</a></span></li><li><span><a href="#2.-NumPy-Arrays" data-toc-modified-id="2.-NumPy-Arrays-2">2. NumPy Arrays</a></span></li><li><span><a href="#3.-Array-Operations-and-Broadcasting" data-toc-modified-id="3.-Array-Operations-and-Broadcasting-3">3. Array Operations and Broadcasting</a></span></li><li><span><a href="#4.-Indexing-and-slicing" data-toc-modified-id="4.-Indexing-and-slicing-4">4. Indexing and slicing</a></span></li><li><span><a href="#5.-More-Useful-NumPy-Functions" data-toc-modified-id="5.-More-Useful-NumPy-Functions-5">5. More Useful NumPy Functions</a></span></li></ul></div>

## Chapter Learning Objectives
<hr>

- Use NumPy to create arrays with built-in functions inlcuding `np.array()`, `np.arange()`, `np.linspace()` and `np.full()`, `np.zeros()`, `np.ones()`
- Be able to access values from a NumPy array by numeric indexing and slicing and boolean indexing
- Perform mathematical operations on and with arrays.
- Explain what broadcasting is and how to use it.
- Reshape arrays by adding/removing/reshaping axes with `.reshape()`, `np.newaxis()`, `.ravel()`, `.flatten()`
- Understand how to use built-in NumPy functions like `np.sum()`, `np.mean()`, `np.log()` as stand alone functions or as methods of numpy arrays (when available)

## 1. Introduction to NumPy
<hr>

![](img/chapter5/numpy.png)

NumPy stands for "Numerical Python" and it is the standard Python library used for working with arrays (i.e., vectors & matrices), linear algerba, and other numerical computations. NumPy is written in C, making NumPy arrays faster and more memory efficient than Python lists or arrays, read more: ([link 1](https://www.datadiscuss.com/proof-that-numpy-is-much-faster-than-normal-python-array/), [link 2](https://www.jessicayung.com/numpy-arrays-memory-and-strides/), [link 3](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)).

NumPy can be installed using `conda` (if not already):

```
conda install numpy
```

## 2. NumPy Arrays
<hr>

### What are Arrays?

Arrays are "n-dimensional" data structures that can contain all the basic Python data types, e.g., floats, integers, strings etc, but work best with numeric data. NumPy arrays ("ndarrays") are homogenous, which means that items in the array should be of the same type. ndarrays are also compatible with numpy's vast collection of in-built functions!

![](img/chapter5/numpy_arrays.png)

Source: [Medium.com](https://medium.com/hackernoon/10-machine-learning-data-science-and-deep-learning-courses-for-programmers-7edc56078cde)

Usually we import numpy with the alias `np` (to avoid having to type out n-u-m-p-y every time we want to use it):

import numpy as np

A numpy array is sort of like a list:

my_list = [1, 2, 3, 4, 5]
my_list

my_array = np.array([1, 2, 3, 4, 5])
my_array

But it has the type `ndarray`:

type(my_array)

Unlike a list, arrays can only hold a single type (usually numbers):

my_list = [1, "hi"]
my_list

my_array = np.array((1, "hi"))
my_array

Above: NumPy converted the integer `1` into the string `'1'`!

### Creating arrays

ndarrays are typically created using two main methods:
1. From existing data (usually lists or tuples) using `np.array()`, like we saw above; or,
2. Using built-in functions such as `np.arange()`, `np.linspace()`, `np.zeros()`, etc.

my_list = [1, 2, 3]
np.array(my_list)

Just like you can have "multi-dimensional lists" (by nesting lists in lists), you can have multi-dimensional arrays (indicated by double square brackets `[[ ]]`):

list_2d = [[1, 2], [3, 4], [5, 6]]
list_2d

array_2d = np.array(list_2d)
array_2d

You'll probably use the built-in numpy array creators quite often. Here are some common ones (hint - don't forget to check the docstrings for help with these functions, if you're in Jupyter, remeber the `shift + tab` shortcut):

np.arange(1, 5)  # from 1 inclusive to 5 exclusive

np.arange(0, 11, 2)  # step by 2 from 1 to 11

np.linspace(0, 10, 5)  # 5 equally spaced points between 0 and 10

np.ones((2, 2))  # an array of ones with size 2 x 2

np.zeros((2, 3))  # an array of zeros with size 2 x 3

np.full((3, 3), 3.14)  # an array of the number 3.14 with size 3 x 3

np.full((3, 3, 3), 3.14)  # an array of the number 3.14 with size 3 x 3 x 3

np.random.rand(5, 2)  # random numbers uniformly distributed from 0 to 1 with size 5 x 2

There are many useful attributes/methods that can be called off numpy arrays:

print(dir(np.ndarray))

x = np.random.rand(5, 2)
x

x.transpose()

x.mean()

x.astype(int)

### Array Shapes

As you just saw above, arrays can be of any dimension, shape and size you desire. In fact, there are three main array attributes you need to know to work out the characteristics of an array:
- `.ndim`: the number of dimensions of an array
- `.shape`: the number of elements in each dimension (like calling `len()` on each dimension)
- `.size`: the total number of elements in an array (i.e., the product of `.shape`)

array_1d = np.ones(3)
print(f"Dimensions: {array_1d.ndim}")
print(f"     Shape: {array_1d.shape}")
print(f"      Size: {array_1d.size}")

Let's turn that print action into a function and try out some other arrays:

def print_array(x):
    print(f"Dimensions: {x.ndim}")
    print(f"     Shape: {x.shape}")
    print(f"      Size: {x.size}")
    print("")
    print(x)

array_2d = np.ones((3, 2))
print_array(array_2d)

array_4d = np.ones((1, 2, 3, 4))
print_array(array_4d)

After 3 dimensions, printing arrays starts getting pretty messy. As you can see above, the number of square brackets (`[ ]`) in the printed output indicate how many dimensions there are: for example, above, the output starts with 4 square brackets `[[[[` indicative of a 4D array.

### 1-d Arrays

One of the most confusing things about numpy is 1-d arrays (vectors) can have 3 possible shapes!

x = np.ones(5)
print_array(x)

y = np.ones((1, 5))
print_array(y)

z = np.ones((5, 1))
print_array(z)

We can use `np.array_equal()` to determine if two arrays have the same shape and elements:

np.array_equal(x, x)

np.array_equal(x, y)

np.array_equal(x, z)

np.array_equal(y, z)

The shape of your 1-d arrays can actually have big implications on your mathematical oeprations!

print(f"x: {x}")
print(f"y: {y}")
print(f"z: {z}")

x + y  # makes sense

y + z  # wait, what?

What happened in the cell above is "broadcasting" and we'll discuss it below.

## 3. Array Operations and Broadcasting
<hr>

### Elementwise operations

Elementwise operations refer to operations applied to each element of an array or between the paired elements of two arrays.

x = np.ones(4)
x

y = x + 1
y

x - y

x == y

x * y

x ** y

x / y

np.array_equal(x, y)

### Broadcasting

ndarrays with different sizes cannot be directly used in arithmetic operations:

a = np.ones((2, 2))
b = np.ones((3, 3))
a + b

`Broadcasting` describes how NumPy treats arrays with different shapes during arithmetic operations. The idea is to wrangle data so that operations can occur element-wise.

Let's see an example. Say I sell pies on my weekends. I sell 3 types of pies at different prices, and I sold the following number of each pie last weekend. I want to know how much money I made per pie type per day.

![](img/chapter5/pies.png)

cost = np.array([20, 15, 25])
print("Pie cost:")
print(cost)
sales = np.array([[2, 3, 1], [6, 3, 3], [5, 3, 5]])
print("\nPie sales (#):")
print(sales)

How can we multiply these two arrays together? We could use a loop:

![](img/chapter5/pies_loop.png)

total = np.zeros((3, 3))  # initialize an array of 0's
for col in range(sales.shape[1]):
    total[:, col] = sales[:, col] * cost
total

Or we could make them the same size, and multiply corresponding elements "elementwise":

![](img/chapter5/pies_broadcast.png)

cost = np.repeat(cost, 3).reshape((3, 3))
cost

cost * sales

Congratulations! You just broadcasted! Broadcasting is just Numpy eessentially doing the `np.repeat()` for you under the hood:

cost = np.array([20, 15, 25]).reshape(3, 1)
print(f" cost shape: {cost.shape}")
sales = np.array([[2, 3, 1], [6, 3, 3], [5, 3, 5]])
print(f"sales shape: {sales.shape}")

sales * cost

In NumPy the smaller array is “broadcast” across the larger array so that they have compatible shapes:

![](img/chapter5/broadcasting.png)

Source: [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas (2016)

Why should you care about broadcasting? Well, it's cleaner and faster than looping and it also affects the array shapes resulting from arithmetic operations. Below, we can time how long it takes to loop vs broadcast:

cost = np.array([20, 15, 25]).reshape(3, 1)
sales = np.array([[2, 3, 1],
                  [6, 3, 3],
                  [5, 3, 5]])
total = np.zeros((3, 3))

time_loop = %timeit -q -o -r 3 for col in range(sales.shape[1]): total[:, col] = sales[:, col] * np.squeeze(cost)
time_vec = %timeit -q -o -r 3 cost * sales
print(f"Broadcasting is {time_loop.average / time_vec.average:.2f}x faster than looping here.")

Of course, not all arrays are compatible! NumPy compares arrays element-wise. It starts with the trailing dimensions, and works its way forward. Dimensions are compatible if:
- **they are equal**, or
- **one of them is 1**.

Use the code below to test out array compatibitlity:

a = np.ones((3, 2))
b = np.ones((3, 2, 1))
print(f"The shape of a is: {a.shape}")
print(f"The shape of b is: {b.shape}")
print("")
try:
    print(f"The shape of a + b is: {(a + b).shape}")
except:
    print(f"ERROR: arrays are NOT broadcast compatible!")

### Reshaping Arrays

There are 3 key reshaping methods I want you to know about for reshaping numpy arrays:
- `.rehshape()`
- `np.newaxis`
- `.ravel()`/`.flatten()`

x = np.full((4, 3), 3.14)
x

You'll reshape arrays farily often and the `.reshape()` method is pretty intuitive:

x.reshape(6, 2)

x.reshape(2, -1)  # using -1 will calculate the dimension for you (if possible)

a = np.ones(3)
print_array(a)
b = np.ones((3, 2))
print_array(b)

If I want to add these two arrays I won't be able to because their dimensions are not compatible:

a + b

Sometimes you'll want to add dimensions to an array for broadcasting purposes like this. We can do that with `np.newaxis` (note that `None` is an alias for `np.newaxis`). We can add a dimension to `a` to make the arrays compatible:

print_array(a[:, np.newaxis])  # same as a[:, None]

a[:, np.newaxis] + b

Finally, sometimes you'll want to "flatten" arrays to a single dimension using `.ravel()` or `.flatten()`. `.flatten()` used to return a copy and `.ravel()` a view/reference but now they both return a copy so I can't think of an important reason to use one over the other 🤷‍♂️

x

print_array(x.flatten())

print_array(x.ravel())

## 4. Indexing and slicing
<hr>

Concepts of indexing should be pretty familiar by now. Indexing arrays is similar to indexing lists but there are just more dimensions.

### Numeric Indexing

x = np.arange(10)
x

x[3]

x[2:]

x[:4]

x[2:5]

x[2:3]

x[-1]

x[-2]

x[5:0:-1]

For 2D arrays:

x = np.random.randint(10, size=(4, 6))
x

x[3, 4]  # do this

x[3][4]  # i do not like this as much

x[3]

len(x)  # generally, just confusing

x.shape

x[:, 2]  # column number 2

x[2:, :3]

x.T

x

x[1, 1] = 555555
x

z = np.zeros(5)
z

z[0] = 5
z

### Boolean Indexing

x = np.random.rand(10)
x

x + 1

x_thresh = x > 0.5
x_thresh

x[x_thresh] = 0.5  # set all elements  > 0.5 to be equal to 0.5
x

x = np.random.rand(10)
x

x[x > 0.5] = 0.5
x

## 5. More Useful NumPy Functions

Numpy has many built-in functions for mathematical operations, really it has almost every numerical operation you might want to do in its library. I'm not going to explore the whole library here, but as an example of some of the available functions, consider working out the hypotenuse of a triangle that with sides 3m and 4m:

![](img/chapter5/triangle.png)

sides = np.array([3, 4])

There are several ways we could solve this problem. We could directly use Pythagoras's Theorem:

$$c = \sqrt{a^2+b^2}$$

np.sqrt(np.sum([np.power(sides[0], 2), np.power(sides[1], 2)]))

We can leverage the fact that we're dealing with a numpy array and apply a "vectorized" operation (more on that in a bit) to the whole vector at one time:

(sides ** 2).sum() ** 0.5

Or we can simply use a numpy built-in function (if it exists):

np.linalg.norm(sides)  # you'll learn more about norms in 573

np.hypot(*sides)

### Vectorization

Broadly speaking, "vectorization" in NumPy refers to the use of optmized C code to perform an operation. Long-story-short, because numpy arrays are homogenous (contain the same dtype), we don't need to check that we can perform an operation on elements of a sequence before we do the operation which results in a huge speed-up. You can kind of think of this concept as NumPy being able to perform an operation on the whole array at the same time rather than one-by-one (this is not actually the case, a super-efficient C loop is still running under the hood, but that's an irrelevant detail). You can read more about vectorization [here](https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html) but all you need to know is that most operations in NumPy are vectorized, so just try to do things at an "array-level" rather than an "element-level", e.g.:

# DONT DO THIS
array = np.array(range(5))
for i, element in enumerate(array):
    array[i] = element ** 2
array

# DO THIS
array = np.array(range(5))
array **= 2 

Let's do a quick timing experiment:

# loop method
array = np.array(range(5))
time_loop = %timeit -q -o -r 3 for i, element in enumerate(array): array[i] = element ** 2
# vectorized method
array = np.array(range(5))
time_vec = %timeit -q -o -r 3 array ** 2
print(f"Vectorized operation is {time_loop.average / time_vec.average:.2f}x faster than looping here.")