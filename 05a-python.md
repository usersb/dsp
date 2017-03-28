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

>> REPLACE THIS TEXT WITH YOUR RESPONSE

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





