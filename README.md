# Introduction to Python
## Introuction to lists and dictionaries
 Lists and dictionaries are built-in data structures in Python. For those of you coming from different programming backgrounds you know a dictionary as a hashmap and a list as an array. They are data structures that are used to store data in in-memory and have different complexities for CRUD operations (CREATE, READ, UPDATE, DELETE). 

In this assignment you will implement a program that will organize data. You will be given two input lists. NAMES, and AGES. Then,
write a function people that takes in an age and returns the names of all the people who are that age.

```
e.g. people(18)
returns: ["Bob", "Cathy"]

```



```

NAMES = [’Alice’, ’Bob’, ’Cathy’, ’Dan’, ’Ed’, ’Frank’,
’Gary’, ’Helen’, ’Irene’, ’Jack’, ’Kelly’, ’Larry’]

AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

These lists match up, so Alice’s age is 20, Bob’s age is 21, and so on. Write a function combine lists that combines
these lists into a dictionary (hint: what should the keys, and what should the values, of this dictionary be?).

```



### Follow up: How can you modify this program to return the names of all people with a certain age.


```

e.g. people("Larry")
returns: [19]

```


## Instructions

- Modify the file src/People.py to return a list of names of people for a specific age. 

- You can also modify the second method "get_reverse(name:string)" to return a list of ages for a given name.

- To run the unit tests and check your code: `python tests/people_test.py` 


## Done

- You have completed the assignment when all your tests pass