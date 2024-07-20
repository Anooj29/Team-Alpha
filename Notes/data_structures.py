# Definition: A list is a collection of ordered, mutable items.
# Lists allow duplicate elements.
lst = [1, 2, 3, 4, 5]

print("List - First element:", lst[0]) 

lst[1] = 10
print("Modified List:", lst)  

lst.append(6)
print("List after append:", lst)  

lst.remove(3)
print("List after removal:", lst)  



# Definition: A set is a collection of unordered, unique items.
# Sets do not allow duplicate elements.
sset = {1, 2, 3, 4, 5}

sset.add(6)
print("Set after adding an element:", sset)  

sset.remove(3)
print("Set after removal:", sset)  



# Definition: A dictionary is a collection of key-value pairs.
# Dictionaries allow fast retrieval, addition, and removal of key-value pairs.
dctry = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Dictionary - Name:", dctry["name"]) 

dctry["age"] = 26
print("Modified Dictionary:", dctry)  

dctry["email"] = "alice@example.com"
print("Dictionary after addition:", dctry)  

del dctry["city"]
print("Dictionary after deletion:", dctry)  



# Definition: A tuple is a collection of ordered, immutable items.
# Tuples allow duplicate elements.
tple = (1, 2, 3, 4, 5)

print("Tuple - First element:", tple[0]) 

new_tuple = tple[:1] + (10,) + tple[2:]
print("New Tuple:", new_tuple)  



#List Comprehension:
#List comprehensions provide a compact way to create lists in Python
#contains for and addionally if and for as per requirement

squares = [x ** 2 for x in range(10)]
print(squares)

table_5 = [x * 5 for x in range(1,11)]
print(table_5)

#Generator expression:
#Generator expressions are similar to list comprehensions but return an iterator instead of a list
#consume less memory compared to list comprehensions

squares_gen = (x ** 2 for x in range(10))
print(squares_gen)

even_numbers_gen = (x for x in range(1, 11) if x % 2 == 0)
print(even_numbers_gen)