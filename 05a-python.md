# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> 
* Python lists and tuples are both types of Python data structures that can be used to store information. However, while lists   are mutable (can be changed), tuples are immutable (cannot be changed).
Only tuples work as dictionary keys because dictionary keys must be immutable. 

Interesting answer from [Stackoverflow.com](http://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples)

* Difference between list and tuple
1. Literal
   ```Python
   someTuple = (1,2)
   someList  = [1,2] 
   ```
   
2. Size
   ```Python
   a = tuple(range(1000))
   b = list(range(1000))

   a.__sizeof__() # 8024
   b.__sizeof__() # 9088
   ```
   
   Due to the smaller size of a tuple operation with it a bit faster but not that much to mention about until you have a huge      amount of elements.
   
 3. Permitted operations
    ```Python
    b    = [1,2]   
    b[0] = 3       # [3, 2]

    a    = (1,2)
    a[0] = 3       # Error
    ```
   that also mean that you can't delete element or sort tuple. At the same time you could add new element to both list and t   tuple with the only difference that you will change id of the tuple by adding element
   ```Python
   a     = (1,2)
   b     = [1,2]  

   id(a)          # 140230916716520
   id(b)          # 748527696

   a   += (3,)    # (1, 2, 3)
   b   += [3]     # [1, 2, 3]

   id(a)          # 140230916878160
   id(b)          # 748527696
   ```
4. Usage
   List being mutable can't be used as a key in the dictionary, while tuple can be used. as key in dictionary.
   ```Python
   a    = (1,2)
   b    = [1,2] 

   c = {a: 1}     # OK
   c = {b: 1}     # Error
   ```
---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 
* Lists and sets are similar in that both are used to store information.
  -Use sets to remove duplicates or check membership  
  -Use list to iterate over elements
* Lists are ordered and can repeat while sets are unordered and unique.
  -Sets are faster for checking membership (for example, x in a Set)
  -Sets are faster than lists for finding an element because it uses an underlying hash table as its data structure while lists  are arrays.
  
* Sets allows you to do operations such as intersection, union, difference, and symmetric difference, i.e operations of math's set theory. Sets doesn't allow indexing and are implemented on hash tables.

* In lists, the elements are accessed by indices.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 
* Python supports a style of programming called functional programming where you can pass functions to other functions to do stuff.

* Lambda expressions (or lambda forms) can be used to create anonymous functions that can be used to define functions needed on the fly. It takes any number of arguments and returns the value of a single expression.

* Examples:
1.
```Python
input_list = [(1,'a'),(2,'c'),(3,'b')]
sorted(input_list, key=lambda x:x[1])

Out[2]:
[(1, 'a'), (3, 'b'), (2, 'c')]
```
2.
```Python
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```
* sets mult3 to [3, 6, 9], those elements of the original list that are multiples of 3.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> 
** List Comprehensions**

Indexing through lists and performing calculations is a frequent task.  Python allows you to combine looping and list manipulation into one operation.
List comprehension is a quick way to create lists. Usually it is used in situations where an operation is applied to each element of another sequence

```Python
iStr = "hello, Are you learning python?"
(' '.join([x.upper() for x in iStr.split()]))

Out[2]: 'HELLO, ARE YOU LEARNING PYTHON?'
```
* Below is an example that returns a list of numbers corresponding to 3 + 4*n+n\**2 for 0<= n <= 10.

```Python
 [3+4*n+n**2 for n in range(0,11)]
 Out[1]: [3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143]
```

**Map**

Map applies a function to all the items in an input_list. Here is the blueprint:

```Python
map(function_to_apply, list_of_inputs)
```
Most of the times we want to pass all the list elements to a function one-by-one and then collect the output.
Map allows us to implement this in a simpler and nicer way.

```Python
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
```

Instead of a list of inputs we can even have a list of functions!
```Python
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
```

**filter**

filter creates a list of elements for which a function returns true. 
example:

```Python
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
```
The filter resembles a for loop but it is a builtin function and faster.

**Difference between map and filter**

filter(), as its name suggests, filters the original iterable and retains the items that returns True for the function provided to filter().

map() on the other hand, applies the supplied function to each element of the iterable and return a list of results for each element.

*example to compare them:
```Python

>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> range(11)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> map(f, range(11)) #the ones that returns TRUE are 1, 5 and 7
[False, True, False, False, False, True, False, True, False, False, False]
>>> filter(f, range(11)) #So, filter returns 1, 5 and 7
[1, 5, 7]
```

**Set Comprehensions**





**Dictionary Comprehensions**



---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





