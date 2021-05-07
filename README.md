# Python

## Table of Contents

1. [What is Python](#What-is-Python)
2. [Types in Python](#Types-in-Python)
3. [Operators in Python](#Operators-in-Python)
4. [Data Structures](#data-structures)
5. [Loops in Python](#loops)
6. [Functions in Python](#functions)
7. [Lambdas](#lambdas)
8. [Dealing with errors](#errors)

## 1. What is Python <a name="What-is-Python"></a>

<img src="https://www.python.org/static/img/python-logo.png" style="width:400px;"/>

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. *Text takem from Python.org*

### How Python works

An interpreter is a kind of program that executes other programs. When you write Python programs , it converts source code written by the developer into intermediate language which is again translated into the native language / machine language that is executed. Python code, written in .py file is first compiled to what is called bytecode which is stored with a .pyc or .pyo format.

- Pros

    - One popular advantage of interpreted languages is that they are platform-independent. As long as the Python bytecode and the Virtual Machine have the same version, Python bytecode can be executed on any platform (Windows, MacOS, etc).
    - Dynamic typing is another advantage. In static-typed languages like C++, you have to declare the variable type and any discrepancy like adding a string and an integer is checked during compile time. In strongly typed languages like Python, it is the job of the interpreter to check the validity of the variable types and operations performed.

- Cons

    - Dynamic typing provides a lot of freedom, but simultaneously it makes your code risky and sometimes difficult to debug.
    - Python is often accused of being ‘slow’. Now while the term is relative and argued a lot, the reason for being slow is because the interpreter has to do extra work to have the bytecode instruction translated into a form that can be executed on the machine.



## 2. Types in Python <a name="Types-in-Python"></a>

### Primitive Types

There are four (4) primitive types in Python which are integers, floats, booleans and strings. Below a brief explanation of each one.

- Integers(```int```):  are used when you want to represent numeric data, whole number specifically. Whole numbers can take negative as well.

    ```integer_number = 2021```

- Floats(```float```): are used to represent floating point numbers.

    ```float_number = 5.3```

- Booleans(```bool```): are dicotomic data types that can take up the values: True and False

    ```bolean_type = True```

- Strings(```str```) = are used when you want to store words, characters and alphabets. You can create a string variable by enclosing a sequence of characters in a single, double or triple quote.

    ```string_quote = 'Hello World!'```
    
### Built-in Data Types

Further primitive types, Python stores data in different types by default:

- Text Type: ```str```
- Numeric Types: ```int```, ```float```, ```complex```
- Sequence Types: ```list```, ```tuple```, ```range```
- Mapping Type: ```dict```
- Set Types: ```set```, ```frozenset```
- Boolean Type:	```bool```
- Binary Types:	```bytes```, ```bytearray```, ```memoryview```

## 2. Operators in Python <a name="Operators-in-Python"></a>

### Arithmetic Operators

The following table lists the arithmetic operators supported by Python:

|Operator|Example|Meaning|Result|
| :-:    | :-:   | :-:   | :-:  |
|+| a + b | Addition | Sum of a and b|
|-| a - b | Subtraction	| b subtracted from a|
|* | a * b | Multiplication | Product of a and b|
|/|	a / b |	Division | Quotient when a is divided by b (The result always has type float).|
|% | a % b | Modulo | Remainder when a is divided by b|
|//| a // b | Floor Division (also called Integer Division)	| Quotient when a is divided by b, rounded to the next smallest whole number|
|** | a ** b | Exponentiation |	a raised to the power of b|

Some real examples are shown below:

- ```python 
    5 + 7 = 12```
- ```python
    4 - 8 = -4```
- ```python
    3 * 2 = 6```
- ```python
    5 / 2 = 2.5```
- ```python
    9 % 2 = 1```
- ```python
    10 // 3 = 3```
- ```python
    2 ** 3 = 8```

### Comparison Operators

It is possible to compare two variables in Python using comparison operators:

|Operator|	Example|	Meaning|	Result|
| :-:    | :-:   | :-:   | :-:  |
|==|	a == b|	Equal to|	```True``` if the value of a is equal to the value of b ```False``` otherwise|
|!=|	a != b|	Not equal to|	```True``` if a is not equal to b ```False``` otherwise|
|<|	a < b|	Less than|	```True``` if a is less than b ```False``` otherwise|
|<=|	a <= b|	Less than or equal to|	```True``` if a is less than or equal to b ```False``` otherwise|
|>|	a > b|	Greater than|	```True``` if a is greater than b ```False``` otherwise|
|>=|	a >= b|	Greater than or equal to|	```True``` if a is greater than or equal to b ```False``` otherwise|


### Logical Operators

As you have seen, some objects and expressions in Python actually are of Boolean type. with logical operators you can deal with it.


|Operator|	Example|	Meaning|
| :-:    | :-:   | :-:   |
|not	|not x|	```True``` if x is ```False``` or   ```False``` if x is ```True```|
|or|	x or y|	```True``` if either x or y is ```True```, ```False``` otherwise|
|and|	x and y|	```True``` if both x and y are ```True```, ```False``` otherwise

## 4. Data Structures <a name="data-structures"></a>

Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly. 

<img src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/10/TreeStructure-Data-Structures-in-Python-Edureka1.png" style="width:800px;"/>

### Built-in Data Structures

#### Lists: 

Lists are used to store data of different data types in a sequential manner. There are addresses assigned to every element of the list, which is called as Index. The index value starts from 0 and goes on until the last element called the positive index. There is also negative indexing which starts from -1 enabling you to access elements from the last to first. Let us now understand lists better with the help of an example program.

Example:

```python
my_list = [] #create empty list
print(my_list)
other_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(other_list)
```

Some methods you can work with on lists are:

|Method|	Description|
|:-:|:-:|
|append()|	Adds an element at the end of the list|
|clear()|	Removes all the elements from the list|
|copy()|	Returns a copy of the list|
|count()|	Returns the number of elements with the specified value|
|extend()|	Add the elements of a list (or any iterable), to the end of the current list|
|index()|	Returns the index of the first element with the specified value|
|insert()|	Adds an element at the specified position|
|pop()|	Removes the element at the specified position|
|remove()|	Removes the first item with the specified value|
|reverse()|	Reverses the order of the list|
|sort()|	Sorts the list|


- Indexing: Python uses zero-based indexing. That means, the first element of the list has an index 0, the second one has index 1, and so on.

    ```python
        other_list[0] = 1
        other_list[3] = 'example'
    ```
- Slicing: As it was shown, indexing allows you to access/change/delete only a single cell of a list. What if we want to get a sublist of the list.

    ```python
      other_list[1:3:] = [2, 3] #[start index (included):final index (not included):jump size (one by one by default)]
      other_list[1::2] = [2, 'example']
    ```

#### Dictionaries:

Dictionaries are used to store key-value pairs. To understand better, think of a phone directory where hundreds and thousands of names and their corresponding numbers have been added. Now the constant values here are Name and the Phone Numbers which are called as the keys. And the various names and phone numbers are the values that have been fed to the keys. If you access the values of the keys, you will obtain all the names and phone numbers.

```python
my_dict = {} #empty dictionary
print(my_dict)
my_dict = {'Víctor': 3215463721, 'Manuel': 3545647567} #dictionary with elements
print(my_dict)
```

If you call for ```my_dict['Víctor']```, you will have the next Output ```3215463721```. On the other hand, some methods you can work with on dictionaries are:

|Method|	Description|
|:-:|:-:|
|clear()|	Removes all the elements from the dictionary|
|copy()|	Returns a copy of the dictionary|
|fromkeys()|	Returns a dictionary with the specified keys and value|
|get()|	Returns the value of the specified key|
|items()|	Returns a list containing a tuple for each key value pair|
|keys()|	Returns a list containing the dictionary's keys|
|pop()|	Removes the element with the specified key|
|popitem()|	Removes the last inserted key-value pair|
|setdefault()|	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value|
|update()|	Updates the dictionary with the specified key-value pairs|
|values()|	Returns a list of all the values in the dictionary|

#### Tuples:

Tuples are the same as lists are with the exception that the data once entered into the tuple cannot be changed no matter what. 

```python
my_tuple = (1, 2, 3, 'This is a tutorial') #access elements
```

Some methods you can work with on tuples are

|Method|	Description|
|:-:|:-:|
|count()|	Returns the number of times a specified value occurs in a tuple|
|index()|	Searches the tuple for a specified value and returns the position of where it was found|

#### Sets:

Sets are a collection of unordered elements that are unique. Meaning that even if the data is repeated more than one time, it would be entered into the set only once. It resembles the sets that you have learnt in arithmetic. 

```python
my_set = {1, 2, 3, 4, 5, 5, 5} #create set
my_set = {1,2,3,4,5} # This will be the Output
```

|Method|	Description|
|:-:|:-:|
|add()|	Adds an element to the set|
|clear()|	Removes all the elements from the set|
|copy()|	Returns a copy of the set|
|difference()|	Returns a set containing the difference between two or more sets|
|difference_update()|	Removes the items in this set that are also included in another, specified set|
|discard()|	Remove the specified item|
|intersection()|	Returns a set, that is the intersection of two other sets|
|intersection_update()|	Removes the items in this set that are not present in other, specified set(s)|
|isdisjoint()|	Returns whether two sets have a intersection or not|
|issubset()|	Returns whether another set contains this set or not|
|issuperset()|	Returns whether this set contains another set or not|
|pop()|	Removes an element from the set|
|remove()|	Removes the specified element|
|symmetric_difference()|	Returns a set with the symmetric differences of two sets|
|symmetric_difference_update()|	inserts the symmetric differences from this set and another|
|union()|	Return a set containing the union of sets|
|update()|	Update the set with another set, or any other iterable|

## 5. Loops in Python <a name="loops"></a>

### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. On Pyhton most of IDE's do the indentation by default

```python
if x<y:
    pass
```

On the code shown before, the whitespace before 'pass' are called indentation space and this is used on all the loops in Python

### If... Else

Knowing the logical operators, it is simple to work with. These conditions can be used in several ways, most commonly in "if statements" and loops.

```python
if b > a:
    print("b is greater than a") # you will get an error
```

But what would you do if you need another option? Well, there's the next possibility

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  ```

As you can see ```elif``` let us to append another if statement to the code. 

To close an If statment you can use ```else```, which catches anything which isn't caught by the preceding conditions (this part of the statement is optional).

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

#### Nested If..Else

You can have if statements inside if statements, this is called nested if statements.

```python
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

### While

With the while loop we can execute a set of statements as long as a condition is true.

```python
i = 1 # This is called a counter
while i < 6:
  print(i)
  i += 1 # This sum an unit to the counter
```

#### ```break``` and ```continue``` statements

With the ```break``` statement you can stop the loop even if the while condition is true, meanwhile with the ```continue``` statement you can stop the current iteration, and continue with the next, for example:

```python
i = 1
while i < 6:
  print(i)
  if i == 5:
    print('This is a break statement')
    break
   elif i == 3:
    print('This is a continue statement')
    i += 1
```

Note that, in While loops it is possible to use ```else``` statement to close the loop as If..Else loop.

### For Loops

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set among others.

```python
names = ['Víctor','Manuel','Felipe','Juan', 'Andrés']
for x in fruits:
    print(x)
```

Even strings can be used for iterate, as you can see:

```python
for i in 'Hello World':
    print(i)
```

On this kinf of loops it is possible to use ```break```, ```pass```, ```else``` and ```continue``` statement too.

For the last, for loops can be used on range of numbers, like this:

```python
for i in range(10):
    print(i)
```

This loop is by far, the most used on Python.



## 6. Functions in Python <a name="functions"></a>

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. At the ende a function can return data as a result.

In Python, it is possible to create a function using the statement ```def```

```python
def first_fuction():
    print('Hello World)
```

To call a created functions, use the function name followed by parenthesis:

```python
first_fuction()
```

### Arguments

Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma. 

```python
def saludo(name):
    print('Hello {}, this is a greeting for you'.format(name))
```

#### Default  arguments

If we call the function without argument, it uses the default value

```python
def your_city(city='Medellín'):
    print('You live in {}'.format(city))
```

### Recursion in functions

Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result. 

```python
def factorial(k):
    if k <= 0:
        result = 0
    elif k == 1:
        result = 1
    else:
        result = k * factorial(k-1)
    return result

number = 5
print('the factorial of {} is {}'.format(number,factorial(number)))
```

## 7. Lambdas <a name="lambdas"></a>

In Python, an anonymous function is a function that is defined without a name. While normal functions are defined using the ```def``` keyword in Python, anonymous functions are defined using the ```lambda``` keyword. Hence, anonymous functions are also called lambda functions.

```python
triple = lambda x : x * 3
```

### Why use lambda functions

The power of lambda is better shown when you use them as an anonymous function inside another function.

```python
def double(lista):
    return list(map(lambda x : x * 2, lista))
```

## 8. Dealing with errors <a name="errors"></a>

Dealing with errorrs is something normal in any lenguage, but Python has some specific statements to deal with it.

### Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message. TO handle this, we can use ```try``` stamenent.

```python
try:
    print(x)
except:
    print('x is not defined') # NameError: As x is not defined, it is necessary to handle it with an exception
```

Also, you can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error

```python
try:
    print(1/x)
except NameError: #NameError
    print('x is not defined')
except ZeroDivisionError: #ZeroDivisionError
    print('x is equal to 0, it is not possible')
else:
    print('Try was applied correctly')
finally:
    print('End of try statement')
```
