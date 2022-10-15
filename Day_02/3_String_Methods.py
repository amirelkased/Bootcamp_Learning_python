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
