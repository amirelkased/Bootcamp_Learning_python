# --------------------------
# fun type(data) -> builtin fun to determine type of data
# All data in python is Object
# --------------------------

print(type(100))  # int "<class 'int'>"

print(type(100.34))  # float "<class 'float'>"

print(type("Amir Ibrahim"))  # str -> String "<class 'str'>"
print(type('Amir Ibrahim'))  # str -> String "<class 'str'>"
print(type('A'))  # str -> String "<class 'str'>"

print(type(['A', 2, 3, 4, 5]))  # list it is like array "<class 'list'>"

print(type((1, 2, 3, 4, 'Amir')))  # tuple "<class 'tuple'>"

print(type({"Amir": 1094372934, "Ibrahim": 1117742771}))  # dict -> dictionary "<class 'dict'>"

print(type(2 != 2))  # boolean True of False "Case Sensitive" "<class 'bool'>"
