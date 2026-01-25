#Dictionary comprehension is used to create a dictionary in a short and clear way. It allows keys and values to be generated from a loop in one line. This helps in building dictionaries directly without writing multiple statements.

#Finding square.
dic = {x: x**2 for x in range(21)}
print("Square of numbers : ", dic)

#Finding square of even numbers.
dic2 = {x: x**2 for x in range(21) if(x%2 == 0)}
print("Square of even numbers : ", dic2)

#Finding square root.
dic3 = {x: x**0.5 for x in range(21)}
print("Square root of numbers : ", dic3)

