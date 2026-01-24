#A generator expression is a concise way to create iterators (generators) in Python, similar to list comprehensions but using parentheses () instead of square brackets [], which produces values lazily (on demand) for memory efficiency, making them ideal for large datasets or infinite sequences by generating items one at a time as needed. They return a generator object, which can be iterated over, and are exhausted after one pass. 

import sys 

PowNumGenerator = (elements**elements for elements in range(21))
PowNumGenerator2 = [elements**elements for elements in range(21)]

#Use next() manually as many time you want to print OR
print(next(PowNumGenerator))
print(next(PowNumGenerator))
print(next(PowNumGenerator))
print(next(PowNumGenerator))
print(next(PowNumGenerator))

#Use the iteration to get the entire data
for num in PowNumGenerator:
    print(num)

#We can see how using generator expression is memory efficient than list comprehension. 
print(sys.getsizeof(PowNumGenerator))
print(sys.getsizeof(PowNumGenerator2))
