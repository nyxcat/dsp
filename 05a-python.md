# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are both used to store long information. Tuples are immutable whereas lists are mutable.  Tuples are fixed size, while lists are dynamic. We can add or remove elements in lists while we can't do thoes in tuples. Tuples are created using '()' while lists are created using '[]'.

Since lists are mutable, they can not be used as keys in dictionaries. Only tuples can work as keys in dictionaries. 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both mutable. Lists are ordered and can have repeated elements, while sets are unordered and cannot have repeated elements.

Example of creating a list:

`name = ['Mary','Tom','Mary']`

Name is a list with 3 elements.

Example of creating a set:

`weekday = set(['Mon','Tues','Wed','Thurs','Fri','Sat','Sun','Mon','Tues'])`

Weekday is a set with 7 elements since Mon and Tue are both repeated.

Looking for an element in sets will be much faster than that in lists because a find operation in sets is O(1) while a find operation in lists is O(n).
---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 

Lambda is used to define anonymous functions. When we need to use a nameless function for a short time, we can use lambda function. It is usually used in an argument of another function.


`employees = [('Mary','34','4500'),('Mike','43','12500'),('John','24','3400')]`

`a = sorted(employees, key = lambda x: x[1])`


These codes will sort employees based on the 2nd item for each employee, giving us 'a' as:[('John', '24', '3400'), ('Mary', '34', '4500'), ('Mike', '43', '12500')].

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> 

List comprehensions provide a way to create lists using set-builder notations. A list of squares of 0 to 9 is created as following:

`squares = [i**2 for i in range(10)]`

An equivalent list can be created using `map` function:

`squares_map = list(map(lambda i: i**2, range(10)))`

Another euquivalent list is created using `filter` function:

`squares_list = list(filter(lambda i : i<100, squares))`

A set comprehension is similar to list comprehension except it uses '{}'.
For example:

`squares_set = {i** i for i in range(10)}`

A dictionary comprehension syntax is:

`{key: value for (key, value) in iterable}`

For example, we can create squares as following.

`squares_dic = {i: i**2 for i in range(10)}`

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
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





