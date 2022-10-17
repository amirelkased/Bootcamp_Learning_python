# TODO:
#  ---------- List ----------
#  [1] List item within '[ items ]'
#  [2] List are Ordered and Zero-based
#  [3] List is mutable can edit, add, remove...
#  [4] List isn't unique
#  [5] List anc have any datatype
#  --------------------------

myList = [10, 20, 30, 40, 'Amir']

print(myList)  # [10, 20, 30, 40, 'Amir']
print(myList[0])  # 10
print(myList[len(myList) - 1])  # Amir
print(myList[-1])  # Amir
print(myList[-2])  # 40

# Slicing
print(myList[:4])  # [10, 20, 30, 40]
print(myList[1:4])  # [20, 30, 40]

# Slicing & step
print(myList[::1])  # [10, 20, 30, 40, 'Amir']
print(myList[::2])  # [10, 30, 'Amir']

# Edit
# [] will delete this pos
myList[1] = 'Twenty'
print(myList)  # [10, 'Twenty', 30, 40, 'Amir']
myList[2:4] = '1', '2'
print(myList)  # [10, 'Twenty', '1', '2', 'Amir']
myList[0:2] = 'A'
print(myList)  # ['A', '1', '2', 'Amir']
