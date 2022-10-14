# -----------------------------------
# [1] \b => back space  "remove one left character"
# [2] \n => new line
# [3] \  => Escape newline
# [4] \' , \"
# [5] \r => Carriage Return
# [6] \xhh => character hex value
# -----------------------------------

# [1]
print("Amir@\b Ibrahim")  # will remove '@'

# [2]
print("Amir\nIbrahim")
# equal
print("""Amir
Ibrahim""")

# [3]
print("Amir\
 Ibrahim\
 Elka-sed")

# [5]
print("Amira\rAmir ")  # will replace all char after \r with the length before this where length <= new length
# out "Amir "

# [6]
print('\x41')  # print char 'A' of hex value 41
