# TODO: [1] Fun len(object):int => length of object
print(len("Amir"))  # output 4

print("------------------------------------------------")

# TODO: [2] strip-"both", lstrip-"left", rstrip-"right"  => used to remove extra space in a string

name = "  Amir Ibrahim   "
print(len(name))
print(name.strip() + ".")
print(name.lstrip() + ".")
print(name.rstrip() + ".")

print("------------------------------------------------")

# TODO: [3] uses strip to remove specified char at leading and trailing

name = "#@###Amir##@##"
print(name.strip("@#@"))  # will remove all char "# or @ at lead and trail
print(name.lstrip("@#@"))
print(name.rstrip("@#@"))

print("------------------------------------------------")

# TODO: [4] title() => it convert all First char or any char after number at all word to capital

collage = "faculty of electronic engineering, el-menofia university"
print(collage.title())  # Faculty Of Electronic Engineering, El-Menofia University

print("------------------------------------------------")

# TODO: [5] capitalize() => convert only first char in all line word

print(collage.capitalize())  # Faculty of electronic engineering, el-menofia university

print("------------------------------------------------")

# TODO: [6] zfill (str var) is used to print number in format width like: 001,011,111 is width '3'

a = "1"
b = "11"
c = "111"
print(a.zfill(3))  # 001
print(b.zfill(3))  # 011
print(c.zfill(3))  # 111

print("------------------------------------------------")

# TODO: [7] upper convert word to upper case

print(collage.upper())  # FACULTY OF ELECTRONIC ENGINEERING, EL-MENOFIA UNIVERSITY
print("TODO".lower())  # todo

print("------------------------------------------------")

# TODO: [8] index(str,start (in),end (ex)) fun is used to search to occurrence of char or substr return index (0-Based)
name = "I love java"
print(name.index("j", 0, 8))  # start default = 0 && end default all length

print("------------------------------------------------")

# TODO: [9] find(Substr, Start, End)  to solve error that occur when index not found str in the range
#  return -1 if not found substr in the string
print(name.find("j", 0, 8))

print("------------------------------------------------")

# TODO: [10] rjust(Require width, Fill char) & ljust(Require width, Fill char)
#  is used to append specified *char or whitespace* to *right or left* of string
#  with width - len
name = "amir"
print(name.ljust(8, "%"))  # amir%%%%
print(name.rjust(5, "*"))  # *amir

print("------------------------------------------------")

# TODO: [11] splitlines() convert multiline to list
name = """Amir
Ibrahim
Mahmoud"""
print(name.splitlines())  # ['Amir', 'Ibrahim', 'Mahmoud']

print("------------------------------------------------")

# TODO: [12] expandtabs(num of space) is used to control num of space for tab \t
t = "i\tlove\tjava"
print(t.expandtabs(2))

print("------------------------------------------------")

# TODO: [13] Boolean Fun
#  istitle() is has every word capital letter?
#  isspace()
#  islower()
name = 'Amir'
print(name.istitle())  # true

# isidentifier() can you use this word as a variable?
name = 'Amir_Ibrahim-100'
print(name.isidentifier())  # false

# isalpha()   this is word contain a-z only
name = 'amir'
print(name.isalpha())  # true

# isalnum()   this is word contain a-z and 0-9
name = 'amir100'
print(name.isalnum())  # true

print("------------------------------------------------")

# TODO: [14] replace(old value, new value, count)

a = 'Hello One Two Three One One'
print(a.replace('One', '1'))

print("------------------------------------------------")

# TODO: [15] <"separator".join(Iterable)> take list, tuple and return string
myList = ['Amir', 'Ibrahim']
print("-".join(myList))  # Amir-Ibrahim
