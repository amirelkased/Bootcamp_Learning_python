# TODO:
#  ---------------------
#  [1] Tuple within parentheses '()'
#  [2] parentheses is optional
#  [3] Indexing
#  [4] Tuple is Immutable => you can't add or delete
#  [5] Tuple items is not unique
#  [6] Tuple items multi type of data
#  [7] Operator
# ----------------------

# Initialize
myAwesomeTuple1 = ('Amir', 21, 'Ibrahim')
myAwesomeTuple2 = 'Amir', 21, 'Ibrahim'
print(myAwesomeTuple1, myAwesomeTuple2)  # ('Amir', 21, 'Ibrahim') ('Amir', 21, 'Ibrahim')

# Tuple Indexing
myTupleNumber = 1, 2, 3, 4, 5
print(myTupleNumber[2])  # 3
print(myTupleNumber[-1])  # 5

# Tuple Assignment values
myImmutableTuple = 1, 2, 3, 'A', 4
# myImmutableTuple[3] = 500  => this line is errorr
print(myImmutableTuple)

# Tuple is not unique
myTuple = 1, 'A', 3, 'A', 4
print(myTuple) # (1, 'A', 3, 'A', 4)

