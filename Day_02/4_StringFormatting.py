# TODO: [1] formatting by using '%s => string,d => number,f => floating point number'
import locale

name = 'Amir Ibrahim'
age = 21
rank = 100.5

print("My name is: %s\nMy age is: %d\nMy Rank is: %f" % (name, age, rank))
# My name is: Amir Ibrahim
# My age is: 21
# My Rank is: 100.500000

print("--------------------------------------------------------------------------------")

# TODO: [2] control floating point number %.2f

print("My Rank with 2 number after decimal point is: %.2f" % rank)  # My Rank with 2 num after decimal point is: 100.50

print("--------------------------------------------------------------------------------")

# TODO: [3] Truncate String %.3s "print only first 3 char"

myLongString = "Hello Peoples of El-zero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.35s" % myLongString)  # Message is Hello Peoples of El-zero Web School '35 char'

print("--------------------------------------------------------------------------------")

# TODO: [4] new formatting is by use '{}' with '.format' fun
#  you can specified type of data by place {:s,d,f}
#  {:s} => String   {:d} => decimal  {:f} => floating point

print("My name is: {}, My age is: {}, My Rank is: {}".format(name, age, rank))
# My name is: Amir Ibrahim, My age is: 21, My Rank is: 100.5

print("My name is: {:s}, My age is: {:d}, My Rank is: {:f}".format(name, age, rank))
# My name is: Amir Ibrahim, My age is: 21, My Rank is: 100.500000

print("My Rank with 2 number after decimal point is: {:.2f}".format(rank))
# My Rank with 2 num after decimal point is: 100.50

print("--------------------------------------------------------------------------------")

# TODO: [5] Formatting Number
#  available _ , .
balanced = 462974060494096
print("{:,d}".format(balanced))  # 462,974,060,494,096

print("--------------------------------------------------------------------------------")

# TODO: [6] Rearrange items
a, b, c = "A", "B", 30
print("Rearrange : {1} {2} {0}".format(a, b, c))  # Rearrange : B 30 A
print("Rearrange : {1} {2:f} {0}".format(a, b, c))  # Rearrange : B 30.000000 A
print("Rearrange : {1} {2:.1f} {0}".format(a, b, c))  # Rearrange : B 30.0 A
print(f"Rearrange : {a} {c:f} {b}")  # Rearrange : A 30.000000 B
