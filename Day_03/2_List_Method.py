myList = ['One', 2, 2.5, 3.0, 'Four', True]
print(myList)  # ['One', 2, 2.5, 3.0, 'Four', True]

# [1] append()
myOldList = [101, 102, 103]
myList.append(False)
print(myList)  # ['One', 2, 2.5, 3.0, 'Four', True, False]
myList.append(myOldList)
print(myList)  # ['One', 2, 2.5, 3.0, 'Four', True, False, [101, 102, 103]]
print(myList[-1][1])  # 102

# [2] extend(list)   =>     Add Second List to current list
myList.extend(myOldList)
print(myList)  # ['One', 2, 2.5, 3.0, 'Four', True, False, [101, 102, 103], 101, 102, 103]

# [3] remove(value)     remove first occur only
myList.remove(myOldList)
print(myList)  # ['One', 2, 2.5, 3.0, 'Four', True, False, 101, 102, 103]

# [4] sort  'by default ascending' and by pass reverse=Ture is become descending
myNum = [10, 80, 90, 4, 0, 3.3]
myNum.sort()  # in ascending
print(myNum)  # [0, 3.3, 4, 10, 80, 90]
myNum.sort(reverse=True)
print(myNum)  # [90, 80, 10, 4, 3.3, 0]

# [5] reverse List not sort-reverse
myName = ['Amir', 'Ibrahim']
myName.reverse()
print(myName)  # ['Ibrahim', 'Amir']

# [6] clear()
# [7] copy() return list
# [8] count(value) return number of occur of value
# [9] index(value) return index of value, if not found make Error

# [10] insert(index,value)  will put value at 'index-1'
List = [20, 30, 10]
List.insert(0, 404)
print(List)  # [404, 20, 30, 10]
List.insert(-1, 404)
print(List)  # [404, 20, 30, 404, 10]

# [11] pop() return the value and remove it from the list
print(List.pop(-2))  # 404
print(List.pop(1))  # 20
