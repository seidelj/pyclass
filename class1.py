# Using python as a calculator

print(10/2)

print(8 * 4)

print(2 + 3)

# Review Modulo

print(5 % 2)

# example using expentation
# A = P * (1+r)^t

#print(100 * 1.1**7)

# Types, integer, floats, bools, string

savings = 100
factor = 1.1
time = 7
desc = "Compound Interest"

print(type(savings))
print(type(factor))
print(type(desc))


result = savings * factor**time

print(result)

doubledesc = desc + desc

print(type(doubledesc))
print(doubledesc)

# Print out information

print("I started with $"+str(savings)+" and now have $"+str(result)+ " awesome!")

# Def of pi_string
pi_string = "3.1415926"

pi_float = float(pi_string)

# Can python handle everything?

print(desc * 2)

print(True + True)

print(False * 100)


## Lists

austin = 17
eli = 16
joe = 28
noah = 16

ages = [austin, eli, joe, noah]
print(type(ages))
print(ages)

ages = ["Austin", austin, "Eli", eli, "Joe", joe, "Noah", noah]
print(ages)

a = [1,2,3,4]
b = [[1,2,3], [4,5,6]]
c = [1 + 2, "a"*5, 3]

print(a)
print(b)
print(c)

#ages = [["Austin", austin],["Eli", eli], ["Joe", joe], ["Noah", noah]]
#print(ages)
if ages[1] == 17:
    print("Correct!")
else:
    print("WRONG!")

print(ages[-1])
print(ages[-2])
print(ages[5])
print(ages[-3])

print(ages[5] == ages[-3])

eli_plus_austin = ages[1] + ages[3]
print(eli_plus_austin == 17+16)


ages1 = ages[0:4]
print(ages1)

print(len(ages))

ages2 = ages[4:8]

print(ages2)

ages1 = ages[:4]
ages2 = ages[4:]

print(ages1)
print(ages2)

ages = [["Austin", austin],["Eli", eli], ["Joe", joe], ["Noah", noah]]

# Indexing lists within lists
print(ages[1])
print(ages[1][1])

ages[2][1] = 29

print(ages)

ages[1][0] = "Elijah"
print(ages)


ages1 = ages + [["Mason", 11]]

print(ages1)

# remove element from list
ages1.remove(ages1[4])
print(ages1)


