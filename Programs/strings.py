print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Tim"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
##print(name + " is " + age + " years old") old code
print(name + f" is  + {age}  years old")
print(type(age))

print(f"Pi is approxitamely {22 / 7:12.50f}")  #Pi is approxitamely 3.14285714285714279370154144999105483293533325195312

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}") # Pi is approximately 3.14285714285714279370154144999105483293533325195312
