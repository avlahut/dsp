# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and Tuples are similar in that both enable iteration and slicing in the same way and allow the ability to hold different data types. However, the big difference lies in that tuples are immutable while lists are considered mutable. This means that once created, tuples can not be changed.  Lists, however, can be changed in place. Because of this difference and the corresponding consequence that lists do not implement the interface *hashable*, only tuples can be used as keys in dictionaries. If a list were to be used as a key and then changed in place, it would invalidate the uniqueness of keys within the dictionary and the corresponding hash search algorithm. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and Sets are both collection of objects that allow for one to query for an elements inclusion as well as iterate over the collection. However, Sets do not allow for duplicate objects to be contained within it and do not allow mutable objects to be held within the Set. (However, the Set itself it considered mutable). Performance for finding an element within it is much faster for a Set as it implements the *hashable* interface as long as you are using the built in methods. Iterating over a Set is slower than iterating over a List.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` construct is used to simplify functions that have a single line so it may exist inline to where it is called rather than defined separately. 
```python
#assuming a list of positive or negative numbers, sort by the absolute value of the number
>>> numbers = [15,-3,2,-4,-10,25]
>>> sorted(numbers,key=lambda num: abs(num))
[2, -3, -4, -10, 15, 25]
>>> 
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allows one to specify the contents of a list using mathematical or set based expressions rather than explicit expressions. There is a lot of overlap in the functionality with `map` and `filter`, especially when combined with a `lambda` expression. However, not all functions can be written in both ways in the same manner. If the definiton rule can not be defined with a `for` or `if` statement, it can not be created with a list comprehension and a map/filter would be more appropriate.
```python
>>>#output the list of states that I have visited but have not lived in based on a given list
>>> statesIveLived = ['CA','WV','OH','NJ','NY','LA']
>>> statesIveVisited = ['CA','WV','OH','NJ','NY','LA','FL','NV','TX','MO','MN']
>>>#list comprehension creating new list based on the differences between the two lists
>>> visitedButNotLived = [ x for x in statesIveVisited if x not in statesIveLived]
>>> list(visitedButNotLived)
['FL', 'NV', 'TX', 'MO', 'MN']
>>>#by using filter and a lambda function to filter out all that is in one list but not the other
>>> visitedButNotLived2 = filter(lambda x: x not in statesIveLived, statesIveVisited)
>>> list(visitedButNotLived2)
['FL', 'NV', 'TX', 'MO', 'MN']
>>>#by using the map function, which applies a function to all values in the given list
>>> visitedButNotLived3 = map(lambda x: (x, x not in statesIveLived) , statesIveVisited)
>>> list(visitedButNotLived3)
[('CA', False), ('WV', False), ('OH', False), ('NJ', False), ('NY', False), ('LA', False), ('FL', True), ('NV', True), ('TX', True), ('MO', True), ('MN', True)]
```
Set comprehensions are very similar to list comprehensions except it returns a set rather than a list.
```python
>>> setVisitedNotLived = { x for x in statesIveVisited if x not in statesIveLived }
>>> setVisitedNotLived
{'MN', 'TX', 'MO', 'FL', 'NV'}
>>> type(setVisitedNotLived)
<class 'set'>
```
Dictionary comprehensions also act in a similar manner but takes two function arguments, one for the keys of the dictionary and one for the values, separated by a `:`.
```python
>>> dictVisitedNotLived = { x:  x not in statesIveLived for x in statesIveVisited }
>>> dictVisitedNotLived
{'OH': False, 'LA': False, 'MO': True, 'TX': True, 'MN': True, 'NY': False, 'CA': False, 'NJ': False, 'WV': False, 'FL': True, 'NV': True}
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7,850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





