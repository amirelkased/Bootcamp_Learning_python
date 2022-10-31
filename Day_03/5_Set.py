# [1] items in curly braces
# [2] items are not ordered and not indexed
# [3] items are not slicing
# [4] items are any type except list
# [5] items are Uniqe
mySet = {"amir", 21, 55.5}
print(mySet)

# [6] clear()
# mySet.clear()
print(mySet)

# [7] union() or | => concat mutli set
set1 = {10, 100, 'A'}
set2 = {11, 101, 'B'}
set3 = {505}
print(set1.union(set2, set3))
print(set1 | set2 | set3)

# [8] add(value) => add value to my set
set3.add(404)
print(set3)

# [9] copy() => shallow copy that mean not referenced
# [10] remove(value) => remove to exists value if not found make
# error KeyError
# [11] discard(value) => is working effecint of remove
# [12] pop() => return random element
# [13] update(set_value)

# [14] difference() "first set - second set"
a = {1, 2, 3, 4}
b = {'Amir', 1}
print(a.difference(b))  # {2,3,4}

# [14] difference_update()
aa = {1, 2, 3, 4}
bb = {'Amir', 1, 2}
aa.difference_update(bb)  # {3, 4}
print(aa)  # {3, 4}

# [15] intersection() a & b
g = {1, 2, 3, 4}
h = {'Amir', 1}
print(g.intersection(h))  # {1}
print(g)

# [16] intersection_update() a & b
g = {1, 2, 3, 4}
h = {'Amir', 1}
g.intersection_update(h)  # {1}
print(g)  # {1}

# [17] symmetric_difference() g ^ h
i = {1, 2, 3, 4, 'X'}
j = {'Amir', 'S', 1, 3, 4}
print(i.symmetric_difference(j))  # {'X', 2, 'S', 'Amir'}

# [17] symmetric_difference_update()
i = {1, 2, 3, 4, 'X'}
j = {'Amir', 'S', 1, 3, 4}
print(i)  # {1, 2, 3, 4, 'X'}
i.symmetric_difference_update(j)
print(i)  # {'X', 2, 'S', 'Amir'}

# [18] bool methods
# [1] issuperset() if second set is already in first set or not
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}
print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

# [2] issubset() if first is completly in second set
print(a.issubset(c)) # True 
print(a.issubset(b)) # False
print(b.issubset(a)) # True

# [3] isdisjoint()  not intersect
print(a.isdisjoint(b)) # False
j = {5,6,7}
print(a.isdisjoint(j)) # True