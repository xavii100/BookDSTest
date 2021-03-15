![](../docs/banner.png)

# Unit Tests & Classes

**Tomas Beuzen, September 2020**

These exercises complement [Chapter 3](../chapters/chapter3-tests-classes.ipynb).

import math

## Exercises

### 1.

The function `area()` accepts the argument `radius` and calculates the area of a circle. Write three tests using `assert` statements for the following conditions:
1. Assert that `area(1)` returns a `float`;
2. Assert that `area(0)` returns a value of 0;
3. Assert that `area(5)` is approximately equal to 78.5 (hint: `math.isclose(..., abs_tol=0.1)`)

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    return math.pi * radius ** 2

# Your answer here.

### 2.

In the spirit of the EAFP (easier to ask for forgiveness than permission) philosophy. Modify the code of the function `area()` and add a `try`/`except` statement to catch the type error raised by passing a string to `area()` as shown below:

area('10')

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    pass # Remove this line and add your answer here.

### 3.

In the spirit of the LBYL (look before you leap) philosophy. Modify the code of the function `area()` and add a conditional `if`/`else` statement to make sure that a user has passed a number (`int` or `float`) to the `area()` function. If they pass something else, raise a `TypeError`.

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    pass # Remove this line and add your answer here.

### 4.

For this exercise I want you to create a class called `Circle`. It should have the following characteristics:
1. It should be initiated with the argument `radius` and store this as an instance attribute.
2. Have a method `area()` which calculates the area of the circle.
3. Have a method `circumference()` which calculates the circumference of the circle.
4. Have the method `__str__()` which is a special method in Python and controls what is output to the screen when you `print()` an instance of your class (learn more [here](https://realpython.com/lessons/how-and-when-use-__str__/)). The `print()` statement should print the string `f"A Circle with radius {self.radius}"`.

I've provided some tests for you to check your class.

class Circle:
    """A circle with a radius r."""

    pass # Remove this line and add your answer here.

assert Circle(3).radius == 3, "Test 1 failed."
assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert Circle(3).__str__() == "A Circle with radius 3", "Test 4 failed."

### 5.

Now, let's create a new class `sphere` that inherits from the `circle` class we created above. It should have the following characteristics:

1. It should be initiated exactly the same as `Circle` was, with the single argument `radius` which is stored as an instance attribute.
2. Have a method `volume()` which calculates the volume of the sphere ($\frac{4}{3}{\pi}{r^3}$).
3. Outputs the string `f"A Sphere with volume 4.19"` when you call `print(Sphere(1))` (hint: recall the `__str__()` method from the previous question).

I've provided some tests for you to check your class.

# Your answer here.

assert Sphere(3).radius == 3, "Test 1 failed."
assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

### 6.

Imagine that users of our `Sphere` class often want to instantiate our class with a `circumference` instead of a `radius`. Add a [class method](https://pages.github.ubc.ca/MDS-2020-21/DSCI_511_py-prog_students/lectures/lecture3-tests-classes.html#methods-class-methods-static-methods) called `from_circ()` to the `Sphere` class that allows users to do this. The method should calculate the `radius` from the passed `circumference`, and then use that `radius` to make an instance of `Sphere`.

I've provided some tests for you to check your modified class.

# Your answer here.

assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed." 
assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."

<hr>
<hr>
<hr>

## Solutions

### 1.

The function `area()` accepts the argument `radius` and calculates the area of a circle. Write three tests using `assert` statements for the following conditions:
1. Assert that `area(1)` returns a `float`;
2. Assert that `area(0)` returns a value of 0;
3. Assert that `area(5)` is approximately equal to 78.5 (hint: `math.isclose(..., abs_tol=0.1)`)

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    return math.pi * radius ** 2

assert isinstance(area(1), float), 'Test 1 failed!'
assert area(0) == 0, 'Test 2 failed!'
assert math.isclose(area(5), 78.5, abs_tol=0.1)

### 2.

In the spirit of the EAFP (easier to ask for forgiveness than permission) philosophy. Modify the code of the function `area()` and add a `try`/`except` statement to catch the type error raised by passing a string to `area()` as shown below:

area('10')

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    try:
        return math.pi * radius ** 2
    except TypeError:
        print(f"radius should be a number but you entered a {type(radius)}")
    except:
        print("Some other error occurred!")

### 3.

In the spirit of the LBYL (look before you leap) philosophy. Modify the code of the function `area()` and add a conditional `if`/`else` statement to make sure that a user has passed a number (`int` or `float`) to the `area()` function. If they pass something else, raise a `TypeError`.

def area(radius):
    """Calculate the area of a circle based on the given radius."""
    if isinstance(radius, (int, float)):
        return math.pi * radius ** 2
    else:
        raise TypeError(f"radius should be a number but you entered a {type(radius)}")

### 4.

For this exercise I want you to create a class called `circle`. It should have the following characteristics:
1. It should be initiated with the argument `radius` and store this as an instance attribute.
2. Have a method `area()` which calculates the area of the circle.
3. Have a method `circumference()` which calculates the circumference of the circle.
4. Have the method `__str__()` which is a special method in Python and controls what is output to the screen when you `print()` an instance of your class (learn more [here](https://realpython.com/lessons/how-and-when-use-__str__/)). The `print()` statement should print the string `f"A Circle with radius {self.radius}"`.

I've provided some tests for you to check your class.

class Circle:
    """A circle with a radius r."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2.0 * math.pi * self.radius

    def __str__(self):
        return f"A Circle with radius {self.radius}"

assert Circle(3).radius == 3, "Test 1 failed."
assert math.isclose(Circle(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Circle(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert Circle(3).__str__() == "A Circle with radius 3", "Test 4 failed."

### 5.

Now, let's create a new class `sphere` that inherits from the `circle` class we created above. It should have the following characteristics:

1. It should be initiated exactly the same as `Circle` was, with the single argument `radius` which is stored as an instance attribute.
2. Have a method `volume()` which calculates the volume of the sphere ($\frac{4}{3}{\pi}{r^3}$).
3. Outputs the string `f"A Sphere with volume 4.19"` when you call `print(Sphere(1))` (hint: recall the `__str__()` method from the previous question).

I've provided some tests for you to check your class.

class Sphere(Circle):
    """A sphere with a radius r."""
    
    def volume(self):
        """Calculate the volume of the sphere."""
        return 4 / 3 * math.pi * self.radius ** 3

    def __str__(self):
        return f"A Sphere with volume {self.volume():.2f}"

assert Sphere(3).radius == 3, "Test 1 failed."
assert math.isclose(Sphere(3).area(), 28.3, abs_tol=0.1), "Test 2 failed."
assert math.isclose(Sphere(3).circumference(), 18.8, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere(3).volume(), 113.1, abs_tol=0.1), "Test 3 failed."
assert Sphere(1).__str__() == "A Sphere with volume 4.19", "Test 4 failed."

### 6.

Imagine that users of our `Sphere` class often want to instantiate our class with a `circumference` instead of a `radius`. Add a [class method](https://pages.github.ubc.ca/MDS-2020-21/DSCI_511_py-prog_students/lectures/lecture3-tests-classes.html#methods-class-methods-static-methods) called `from_circ()` to the `Sphere` class that allows users to do this. The method should calculate the `radius` from the passed `circumference`, and then use that `radius` to make an instance of `Sphere`.

I've provided some tests for you to check your modified class.

class Sphere(Circle):
    """A sphere with a radius r."""
    
    def volume(self):
        """Calculate the volume of the sphere."""
        return 4 / 3 * math.pi * self.radius ** 3
    
    @classmethod
    def from_circ(cls, circumference):
        """Make an instance of Sphere from a circumference."""
        radius = circumference / (2 * math.pi)
        return cls(radius)

    def __str__(self):
        return f"A Sphere with volume {self.volume():.2f}"

assert Sphere.from_circ(0).radius == 0, "Test 1 failed."
assert Sphere.from_circ(3 * math.pi).radius == 1.5, "Test 2 failed." 
assert math.isclose(Sphere.from_circ(6).radius, 0.95, abs_tol=0.1), "Test 3 failed."
assert math.isclose(Sphere.from_circ(6).volume(), 3.65, abs_tol=0.1), "Test 4 failed."
assert Sphere.from_circ(6).__str__() == "A Sphere with volume 3.65", "Test 5 failed."