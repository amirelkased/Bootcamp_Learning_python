# [1] How to define one data is a Tuple
tuple1 = ('Amir')
tuple2 = 'Amir'
print(type(tuple1), '\n', type(tuple2))  # two is <str>

realTuple1 = ('Amir',)
realTuple2 = 'Amir',
print(type(realTuple1), type(realTuple2))  # two is <tuple>

# [2] Tuple Concatenation
a, b = (1, 2, 3), (4, 5)
c = a + b
print(c)  # (1, 2, 3, 4, 5)

# [3] Tuple, List, Sting Repeat by (*)
String = 'A'
print(String * 2)  # AA

# [4] count(value) and return no of count
print(a.count(1))  # 1
print(a.count(4))  # 0

# [5] index(value,start,end)
print(f'The Position of {3} is {a.index(3)}')  # The Position of 3 is 2

# Tuple Destruct
# used to destruct tuple to variable and num of var must equal num of item in tuple
x, y, z = a
print(x, y, z)  # 1 2 3

# if you have item and need to ignore it you can use _
x, _, z = a
print(x, z)  # 1 3
