![](../docs/banner.png)

# NumPy

**Tomas Beuzen, September 2020**

These exercises complement [Chapter 5](../chapters/chapter5-numpy.ipynb) and [Chapter 6](../chapters/chapter6-numpy-addendum.ipynb).

## Exercises

### 1.

Import numpy under the alias `np`.

# Your answer here.

### 2.

Create the following arrays:

1. Create an array of 5 zeros.
2. Create an array of 10 ones.
3. Create an array of 5 3.141s.
4. Create an array of the integers 1 to 20.
5. Create a 5 x 5 matrix of ones with a dtype `int`.

# Your answer here.

### 3.

Use numpy to:
1. Create an 3D matrix of 3 x 3 x 3 full of random numbers drawn from a standard normal distribution (hint: `np.random.randn()`)
2. Reshape the above array into shape (27,)

# Your answer here.

### 4.

Create an array of 20 linearly spaced numbers between 1 and 10.

# Your answer here.

### 5.

Run the following code to create an array of shape 4 x 4 and then use indexing to produce the outputs shown below.

import numpy as np
a = np.arange(1, 26).reshape(5, -1)

```python
20
```

# Your answer here.

```python
array([[ 9, 10],
       [14, 15],
       [19, 20],
       [24, 25]])
```

# Your answer here.

```python
array([ 6,  7,  8,  9, 10])
```

# Your answer here.

```python
array([[11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]])
```

# Your answer here.

```python
array([[ 8,  9],
       [13, 14]])
```

# Your answer here.

### 6.

Calculate the sum of all the numbers in `a`.

# Your answer here.

### 7.

Calculate the sum of each row in `a`.

# Your answer here.

### 8.

Extract all values of `a` greater than the mean of `a` (hint: use a boolean mask).

# Your answer here.

### 9.

Find the location of the minimum value in the following array `b`:

np.random.seed(123)
b = np.random.randn(10)
b

# Your answer here.

### 10.

Find the location of the maximum value in the following 2D array `c` (hint: there are many ways to do this question, but a quick search on stackoverflow.com will typically help you find the optimum solution for a problem, for example see [post](https://stackoverflow.com/questions/3584243/get-the-position-of-the-biggest-item-in-a-multi-dimensional-numpy-array)):

np.random.seed(123)
c = np.random.randn(3, 2)
c

# Your answer here.

<hr>
<hr>
<hr>

## Solutions

### 1.

Import numpy under the alias `np`.

import numpy as np

### 2.

Create the following arrays:

1. Create an array of 5 zeros.
2. Create an array of 10 ones.
3. Create an array of 5 3.141s.
4. Create an array of the integers 1 to 20.
5. Create a 5 x 5 matrix of ones with a dtype `int`.

print(np.zeros(5))
print(np.ones(10))
print(np.full(5, 3.141))
print(np.array(range(21)))
print(np.ones((5, 5), dtype=int))

### 3.

Use numpy to:
1. Create an 3D matrix of 3 x 3 x 3 full of random numbers drawn from a standard normal distribution (hint: `np.random.randn()`)
2. Reshape the above array into shape (27,)

x = np.random.randn(3, 3, 3)
x

x.reshape(-1) # or x.reshape(27)

### 4.

Create an array of 20 linearly spaced numbers between 1 and 10.

np.linspace(1, 10, 20)

### 5.

Below I've defined an array of shape 4 x 4. Use indexing to procude the given outputs.

a = np.arange(1, 26).reshape(5, -1)
a

```python
20
```

a[3,4]

```python
array([[ 9, 10],
       [14, 15],
       [19, 20],
       [24, 25]])
```

a[1:,3:]

```python
array([ 6,  7,  8,  9, 10])
```

a[1,:]

```python
array([[11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]])
```

```python
array([[ 8,  9],
       [13, 14]])
```

a[1:3,2:4]

### 6.

Calculate the sum of all the numbers in `a`.

a.sum()

### 7.

Calculate the sum of each row in `a`.

a.sum(axis=1)

### 8.

Extract all values of `a` greater than the mean of `a` (hint: use a boolean mask).

a[a > a.mean()]

### 9.

Find the location of the minimum value in the following array `b`:

np.random.seed(123)
b = np.random.randn(10)
b

b.argmin()

### 10.

Find the location of the maximum value in the following 2D array `c` (hint: there are many ways to do this question, but a quick search on stackoverflow.com will typically help you find the optimum solution for a problem, for example see [post](https://stackoverflow.com/questions/3584243/get-the-position-of-the-biggest-item-in-a-multi-dimensional-numpy-array)):

np.random.seed(123)
c = np.random.randn(3, 2)
c

print(f"Location of maximum: {np.unravel_index(c.argmax(), c.shape)}")
print(f"   Value of maximum: {c.max():.2f}")