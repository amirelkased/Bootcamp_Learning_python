# -------------------------------
# [1] All datatype in Python is Object
# [2] Object contain elements
# [3] Every element have index
# [4] indexing start from zero
# -------------------------------

# Indexing
testString = 'Amir'
print(testString[0])
print(testString[-1])  # first char from end

# Slicing
# (name of var)[start (in):End (ex)]
# (name of var)[start (in):End (ex):Steps]
# if Start not specified it start at index "0"
# if End not specified worked to the end
# steps by default is one else it will walk when i specified it
# that mean when it == 1 it walk 0-1-2-3 and so on
# when i told it 2 it will walk 0-2-4-6 and so on

test = "I am java developer"
print(test[5:9])
print(test[:1])  # start from zero by default
print(test[5:])
print(test[::2])
