# --------------------------------------------------------
# Syntax -> [variable name] [Assignment Operator] [value]
#
# Name Convention and Rules
# [1] start with a-z | A-Z | _
# [2] not start with 0-9 | special character
# [3] Can include (0-9) or _
# [4] Can't included Special Character
# [5] Case Sensitive
# [6] Words that reserved by Python can't use at naming variable
# -------------------------------------------
# Source code : original code you write it in computer
# Translation : convert source code to machine language
# Compilation : translate your code before run time
# Interpreted : code translate on the fly during execution
# ---------------------------------------------------------

# reserved words
help("keywords")

name = "Amir"  # Normal case
myName = "Amir"  # camelCase
my_name = "Amir"  # snake_case

print(name)
print(myName)
print(my_name)

# why python is interpreted? can change type of data at run time
# look for prev name variable
name = 21
print(name)

# multi variable inline
a, b, c = 10, 20, 30
print(a, b, c)
