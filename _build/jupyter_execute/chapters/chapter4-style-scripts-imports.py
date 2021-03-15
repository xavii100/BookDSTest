![](../docs/banner.png)

# Chapter 4: Style Guides, Scripts, Imports

<h2>Chapter Outline<span class="tocSkip"></span></h2>
<hr>
<div class="toc"><ul class="toc-item"><li><span><a href="#1.-Style-Guide" data-toc-modified-id="1.-Style-Guide-1">1. Style Guide</a></span></li><li><span><a href="#2.-Python-Scripts" data-toc-modified-id="2.-Python-Scripts-2">2. Python Scripts</a></span></li><li><span><a href="#3.-Importing" data-toc-modified-id="3.-Importing-3">3. Importing</a></span></li><li><span><a href="#4.-Intriguing-Behaviour-in-Python" data-toc-modified-id="4.-Intriguing-Behaviour-in-Python-4">4. Intriguing Behaviour in Python</a></span></li></ul></div>

## Chapter Learning Objectives
<hr>

- Describe why code style is important.
- Differentiate between the role of a linter like `flake8` and an autoformatter like `black`.
- Implement linting and formatting from the command line or within Jupyter or another IDE.
- Write a Python module (`.py` file) in VSCode or other IDE of your choice.
- Import installed or custom packages using the `import` syntax.
- Explain the notion of a reference in Python.
- Explain the notion of scoping in Python.
- Anticipate whether changing one variable will change another in Python.
- Anticipate whether a function changes the caller's version of an argument variable in Python.
- Select the appropriate choice between `==` and `is` in Python.

## 1. Style Guide
<hr>

![](img/chapter4/xkcd.png)

Source: [xkcd.com](https://imgs.xkcd.com/comics/code_quality.png).

It is incorrect to think that if your code works then you are done. Code has two "users" - the computer (which turns it into machine instructions) and humans, who will likely read and/or modify the code in the future. This section is about how to make your code suitable to that second audience, humans.

Styling is particularly important for sharing your code to other users (including your future self!). Remember: "Code is read much more often than it is written". [PEP8](https://www.python.org/dev/peps/pep-0008/) is the Python Style Guide. It is worth skimming through PEP 8, but here are some highlights:
- Indent using 4 spaces
- Have whitespace around operators, e.g. `x = 1` not `x=1`
- But avoid extra whitespace, e.g. `f(1)` not `f (1)`
- Single and double quotes both fine for strings, but use `"""`triple double quotes`"""` for docstrings, not `'''`triple single quotes`'''`
- Variable and function names use `underscores_between_words`
- And much more...

There's lots to remember but luckily **linters** & **formatters** can help you adhere to uniform styling!

### Linters

Linting refers to highlighting programmatic and stylistic problems in your Python source code. Think of it like "spell check" in word processing software. Common linters include `pycodestyle`, `pylint`, `pyflakes`, `flake8`, etc. We'll use [flake8](https://flake8.pycqa.org/en/latest/) in this chapter, which, if you don't have it, you can install with:

```
conda install -c anaconda flake8
```

`flake8` can be used from the command line to check files:

```
flake8 path/file_to_check.py
```

You can execute shell commands in Jupyter by prepending a command with an exclamation mark `!`. I've included an example script called [`bad_style.py`](https://github.com/TomasBeuzen/python-programming-for-data-science/blob/main/chapters/data/bad_style.py) in the data sub-directory of this directory, let's use `flake8` on that now:

!flake8 data/bad_style.py

### Formatters

Formatting refers to restructuring how code appears by applying specific rules for line spacing, indents, line length, etc. Common formatters include `autopep8`, `black`, `yapf`, etc. We'll use [black](https://black.readthedocs.io/en/stable/?badge=stable) in this chapter, which, if you don't have it, you can install with:

```
conda install -c conda-forge black
```

`black` can also be used from the command line to format your files:

```
black path/file_to_check.py --check
```

The `--check` argument just checks if your code conforms to black style but doesn't reformat it in place, if you want your file reformatted, remove the argument.

!black data/bad_style.py --check

Here's the file content before formatting:

x = {  'a':37,'b':42,
'c':927}
very_long_variable_name = {'field': 1,
                        'is_debug': True}
this=True

if very_long_variable_name is not None and very_long_variable_name["field"] > 0 or very_long_variable_name['is_debug']:
 z = 'hello '+'world'
else:
 world = 'world'
 a = 'hello {}'.format(world)
 f = rf'hello {world}'
if (this): y = 'hello ''world'#FIXME: https://github.com/python/black/issues/26
class Foo  (     object  ):
  def f    (self   ):
    return       37*-2
  def g(self, x,y=42):
      return y
# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5
]
# fmt: on
regular_formatting = [
    0,  1,  2,
    3,  4,  5
]

ANd here it is after formatting (note how you can toggle formatting on or off in your code using the `# fmt: off`/`# fmt: on` tags):

x = {"a": 37, "b": 42, "c": 927}
very_long_variable_name = {"field": 1, "is_debug": True}
this = True

if (
    very_long_variable_name is not None
    and very_long_variable_name["field"] > 0
    or very_long_variable_name["is_debug"]
):
    z = "hello " + "world"
else:
    world = "world"
    a = "hello {}".format(world)
    f = rf"hello {world}"
if this:
    y = "hello " "world"  # FIXME: https://github.com/python/black/issues/26


class Foo(object):
    def f(self):
        return 37 * -2

    def g(self, x, y=42):
        return y


# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5
]
# fmt: on
regular_formatting = [0, 1, 2, 3, 4, 5]

### Comments

Comments are important for understanding your code. While docstrings cover what a function _does_, your comments will help document _how_ your code achieves its goal. There are PEP 8 guidelines on the length, spacing, etc of comments.
- **Comments**: should start with a `#` followed by a single space and be preceded by at least two spaces.
- **Block Comments**: each line of a block comment should start with a `#` followed by a single space and should be indented to the same level as the code it precedes.
- Generally, comments should not be unnecessarily verbose or just state the obvious, as this can be distracting and can actually make your code more difficult to read!

Here is an example of a reasonable comment:

def random_walker(T):
    x = 0
    y = 0

    for i in range(T): 
        
        # Generate a random number between 0 and 1.
        # Then, go right, left, up or down if the number
        # is in the interval [0,0.25), [0.25,0.5),
        # [0.5,0.75) or [0.75,1) respectively.
        
        r = random() 
        if r < 0.25:
            x += 1      # Go right
        elif r < 0.5:
            x -= 1      # Go left
        elif r < 0.75:
            y += 1      # Go up
        else:
            y -= 1      # Go down

        print((x,y))

    return x**2 + y**2

Here are some **bad examples** of comments, because they are unnecessary or poorly formatted:

def random_walker(T):
    # intalize coords
    x = 0
    y = 0

    for i in range(T):# loop T times
        r = random()
        if r < 0.25:
            x += 1  # go right
        elif r < 0.5:
            x -= 1  # go left
        elif r < 0.75:
            y += 1       # go up
        else:
            y -= 1

        # Print the location
        print((x, y))

    # In Python, the ** operator means exponentiation.
    return x ** 2 + y ** 2

## 2. Python Scripts
<hr>

Jupyter is a fantastic data science tool which allows you to code and create visualisations alongside text and images to create narratives. However, as your project grows, eventually you're going to need to create python scripts, `.py` files `.py` files are also called "modules" in Python and may contain functions, classes, variables, and/or runnable code. I typically start my projects in Jupyter, and then begin to offload my functions, classes, scripts, etc to `.py` files as I formalise, structure and streamline my code.

### IDEs

You don't need any special software to write Python modules, you can write your code using any text editor and just save your file with a `.py` extension. But software exists to make your life much easier!

IDE stands for "integrated development environment" and refers to software that provides comprehensive functionality for code development (e.g., compiling, debugging, formatting, testing, linting, etc). In my experience the most popular out-of-the-box Python IDEs are [PyCharm](https://www.jetbrains.com/pycharm/) and [Spyder](https://www.spyder-ide.org/). There are also many editors available that can be customized with extensions to act as Python IDEs, e.g., [VSCode](https://code.visualstudio.com/), [Atom](https://atom.io/), [Sublime Text](https://www.sublimetext.com/). The benefit of these customisable editors is that they are light-weight and you can choose only the extensions you really need (as opposed to downloading a big, full-blown IDE like PyCharm).

VSCode is my favourite editor at the moment and they have a [great Python tutorial online](https://code.visualstudio.com/docs/languages/python) which I'd highly recommend if you're interested! We'll do some importing of custom `.py` files in these chapters but won't do any work in an IDE.

## 3. Importing
<hr>

Python can access code in another module by importing it. This is done using the `import` statement, which you've probably seen a few times already. We'll discuss importing more in DSCI 524 and you can read all about it in the [Python documentation](https://docs.python.org/3/reference/import.html) but for now, it's easiest to see it in action.

### Ways of Importing Things

I've written a `.py` file called `wallet.py` that contains a class `Wallet` that can be used to store, spend, and earn cash. I recommend taking a look at that file on GitHub before moving on.

Let's `import` the code from `wallet.py` . We can import our `.py` file (our module) simply by:

import wallet

We can take a look at all the useable parts of that module by typing `dir(wallet)`:

dir(wallet)

We can import a package using an alias with the `as` keyword:

import wallet as w

w.Wallet(100)

w.InsufficientCashError()

And we can import just a specific function/class/variable from our module:

from wallet import Wallet

Wallet(100) # now I can refer to it without the module name prefix

You can even mix up all these methods:

from wallet import Wallet as w

w(100)

It's also possible to import everything in a module, though this is generally not recommended:

from wallet import *

Wallet(100)

InsufficientCashError()

#### Importing Functions from Outside your Working Directory

I could do `import wallet` above because `wallet.py` is in my current working directory. But there are a few extra steps needed if it is in a different location. I've included a script called `hello.py` in a `data/` sub-directory of the directory housing this notebook. All it has in it is:

```python
PLANET = "Earth"


def hello_world():
    print(f"Hello {PLANET}!")
```

Unfortunately I can't do this:

from hello import hello_world

What I need to do is add this directory location to the paths that Python searches through when looking to import something. I usually do this using the `sys` module:

import sys
sys.path.append('data/')
sys.path # display the current paths Python is looking through

See that `data/` is now a valid path. So now I can import from `hello.py`:

from hello import hello_world, PLANET

PLANET  # note that I can import variable defined in a .py file!

hello_world()

### Packages

As your code gets more complex, grows in modules, and you wish to share it, you'll want to turn it into a Python package. Packages are logical collections of modules that can be easily imported. If you're interested in creating your own packages, take a look at the [py-pkgs book](https://ubc-mds.github.io/py-pkgs/). For now, we'll be using other people's popular data science packages, specifically, next chapter we'll look at `numpy`: "the fundamental package for scientific computing with Python".

#### Importing Installed Packages

In the next few chapters we'll be using the `numpy` and `pandas` packages, which are probably the most popular for data science. When you install those packages, they are put in a location on your computer that Python already knows about, so we can simply import them at will.

import numpy as np

np.array([1, 2, 3])

np.random.randint(0, 10, 3)

There are plenty of packages that come with the [Python Standard Library](https://docs.python.org/3/library/) - these do not require installation with `conda` and you'll come across them throughout your data science journey, I'll show one example, `random`, below. But for more advanced stuff you'll to install and use packages like `numpy`, `pandas` and others. If you need some specific functionality, make sure you check if there's a package for it (there often is!). For example, one functionality I often want is a progress bar when looping over a `for` loop. This is available in the [tqdm package](https://github.com/tqdm/tqdm):

from tqdm import tqdm
for i in tqdm(range(int(10e5))):
    i ** 2

## 4. Intriguing Behaviour in Python
<hr>

### References

What do you think the code below will print?

x = 1
y = x
x = 2
y

And how about the next one?

x = [1]
y = x
x[0] = 2
y

In Python, the list `x` is a **reference** to an object in the computer's memory. When you set `y = x` these two variables now refer to the same object in memory - the one that `x` referred to. Setting `x[0] = 2` modifies the object in memory. So `x` and `y` are both modified (it makes no different if you set `x[0] = 2` or `y[0] = 2`, both modify the same memory).
 
Here's an analogy that might help understand what's going on:
- I share a Dropbox folder (or git repo) with you, and you modify it -- I sent you _the location of the stuff_ (this is like the list case)
- I send you an email with a file attached, you download it and modify the file -- I sent you _the stuff itself_ (this is like the integer case)

Okay, what do you think will happen here:

x = [1]
y = x
x = [2] # before we had x[0] = 2
y

Here we are not modifying the contents of `x`, we are setting `x` to refer to a new list `[2]`.

### Additional Weirdness

We can use `id()` to return the unique id of an object in memory.

x = np.array([1, 2, 3, 4, 5])  # this is a numpy array which we'll learn more about next chapter
y = x
x = x + 5

print(f"x has the value: {x}, id: {id(x)}")
print(f"y has the value: {y}, id: {id(y)}")

x = np.array([1, 2, 3, 4, 5])
y = x
x += 5

print(f"x has the value: {x}, id: {id(x)}")
print(f"y has the value: {y}, id: {id(y)}")

So, it turns out `x += 5` is not identical `x = x + 5`. The former modifies the contents of `x`. The latter first evaluates `x + 5` to a new array of the same size, and then overwrites the name `x` with a reference to this new array.

But there's good news - we don't need to memorize special rules for calling functions. Copying happens with `int`, `float`, `bool`, (maybe some other ones I'm forgetting?), the rest is "by reference". Now you see why we care if objects are mutable or immutable... passing around a reference can be dangerous! General rule - if you do `x = ...` then you're not modifying the original, but if you do `x.SOMETHING = y` or `x[SOMETHING] = y` or `x *= y` then you probably are.

### `copy` and `deepcopy`

We can force the certain copying behaviour using the `copy` library if we want to:

import copy  # part of the standard library

x = [1]
y = x
x[0] = 2
y

x = [1]
y = copy.copy(x)  # We "copied" x and saved that new object as y
x[0] = 2
y

Ok, so what do you think will happen here?

x = [[1], [2, 99], [3, "hi"]]  # a list of lists

y = copy.copy(x)
print("After copy.copy():")
print(x)
print(y)

x[0][0] = "pikachu"
print("")
print("After modifying x:")
print(x)
print(y)

But wait.. we used `copy`, why are `x` and `y` both changed in the latter example? `copy` makes the _containers_ different, i.e., only the outer list. But the outer lists contain references to objects which were not copied! This is what happens after `y = copy.copy(x)`:

![](img/chapter4/copy.png)

We can use `is` to tell apart these scenarios (as opposed to `==`). `is` tells us if two objects are referring to the same object in memory, while `==` tells us if their contents are the same:

x == y # they are both lists containing the same lists

x is y # but they are not the *same* lists of lists

So, by that logic we should be able to append to `y` without affecting `x`:

y.append(5)

print(x)
print(y)

x == y

That makes sense, as weird as it seems:

![](img/chapter4/copy-append.png)

In short, `copy` only copies one level down. What if we want to copy everything? i.e., even the inner lists in our outer list... Enter our friend `deepcopy`:

x = [[1], [2, 99], [3, "hi"]]

y = copy.deepcopy(x)

x[0][0] = "pikachu"
print(x)
print(y)

![](img/chapter4/deep-copy.png)

```{tip}
If you're interested, you can find a whole compilation of more intriguing behaviour in Python [here](https://github.com/satwikkansal/wtfpython/blob/master/README.md)!
```