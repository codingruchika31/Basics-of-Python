# -*- coding: utf-8 -*-
"""Python Practice

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ubkiHJ7VhAZcudu5eDqNHTHzimUiHEBb

# Data Types
"""

numbers=[1,2,3,4,5]
print(numbers[3])

type(numbers)

number_phrases={
    "number1":1,
    "number2":2,
    "number3":3
}
print(number_phrases)

type(number_phrases)

for number in numbers:
  if number%2==0:
    print(numbers[number])

for x, y in number_phrases.items():
  if y%2!=0:
    print(x)

"""##Lists


"""

furniture = ['Table', 'Chair', 'rack', 'shelf', 'chair']
furniture[0:-1]

'rack' in ['table', 'chair', 'rack', 'shelf']

furniture.index('chair')

furniture.insert(1, 'bed')
furniture

furniture.remove('chair')
furniture

del furniture[2]
furniture

furniture.pop()

furniture

furniture.sort(reverse=True)
furniture

"""##Tuples"""

##The key difference between tuples and lists is that, while tuples are immutable objects, lists are mutable. This means that tuples cannot be changed while the lists can be modified. Tuples are more memory efficient than the lists.
furniture = ('table', 'chair', 'rack', 'bed')

type(furniture)

"""###convert between list() and tuple()"""

new_furniture=list(furniture)

type(new_furniture)

hello = list('hello')
hello

new_hello=tuple(hello)
new_hello
type(new_hello)

"""##Dictionaries"""

books={
    'non-ficion':'psychology of money',
    'fiction':'percy jackson',
    'history':'discovery of india',
    'competitive':'crack ias'
}



"""##Sets"""



"""# Function in Python"""

def furniture_func():
  furniture = ['table', 'chair', 'rack', 'shelf']
  for item in furniture:
   print(f' item: {item}')

furniture_func()

def return_func(x, y):
  z=x*y
  return z

return_func(100,200)

def spam():
  global eggs
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

def spam():
  eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

add = lambda x, y: x + y

add(5, 3)

"""## fibonacci using lamba function"""

fibonacci = lambda x, y: x+y

m=0
n=1
print(m)
print(n)
for i in range(20):
  temp=m
  m=n
  n=fibonacci(temp,n)
  print(n)