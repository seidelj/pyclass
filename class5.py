# Fibonacci Series:
# The sume of two elements defines the next
# F(n+1) = F(n) + F(n-1)

a = 0
b = 1
while b < 10:
    print b
    a_temp = a
    a = b
    b = a_temp + b

print("Equivently")

a, b = 0, 1
while b < 10:
    print b
    a, b = b, a+b

# Q: How can we print more elements from the series?

'''
# If statements
x = int(raw_input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to 0")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")
'''

# For statements
words = ['dog', 'apple', 'window']
for w in words:
    print w, len(w)

## Range

x = range(10)
print(x)

# Start at 5
y = range(5, 10)
print(y)

# Start at 0, but step
z = range(0,10,3)
print(z)

# Use indexes to iterate
a = ['Cal Ripken', '1982', 'Fleer', 'Card', '#176']
for i in range(len(a)):
    print i, a[i]
# Note "Cal Ripken" althought being 2 words is treated as 1


# break, continue, and else clauses on loops
'''
Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. This is exemplified by the following loop, which searches for prime numbers:
'''

for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # Loop fell through without finding a factor
        print n, "is a prime number"

# continue, continues with the next iteration of the loop
for num in range(2,10):
    if num % 2:
        print "Found an even number", num
        continue
    print "Found a number", num

# Pass statements

# Useful when a statement is required syntaxically but the
# Program requires no actions

#while True:
#   pass #What for keyboard interupt ctrl+c


# Creating a minimal class
class MyEmptyClass:
    pass

# Placeholder for a function you'll write later when working on new code
def fib(*args):
    pass # Implement this later

# Define a function that prints the fib sequence

def fib(n): # write Fibonacci Series up to n
    """Print a Fibonacci Series up to n """ #A doc string
    a, b = 0,1
    while a < n:
        print a,  # observe the comma.  avoids newlines
        a, b = b, a+b

print fib.__doc__

fib(2000)
#Q: Why didnt we need a print statement?

# Techinically, the fib function does return anything which is not typically
#usefull. Let's make a fib that does return something

def fib2(n):
    """Return a list containing the Fibonacci Series up n"""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print # just to make a newline
print(f100)

# Functions can have more than one argument

def madlib(name, adjective="bored", noun="computer"):
    print "-- Please excuse", name,
    print ", who is too", adjective,
    print "to attend", noun, "class."

madlib("Joe")
madlib("Joe", "busy", "management")
