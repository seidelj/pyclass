
try:
    10 * (1/0)
except ZeroDivisionError:
    pass # do nothing

try:
    4 + spam*3
except NameError:
    print "We never defined spam"

try:
    '2' + 2
except TypeError:
    int('2') + 2

# Another example
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."

# There is also an else clause which can be included
try:
    y = int(raw_input("Enter a number: "))
except ValueError:
    print "You didn't enter a number, so we'll choose one for you"
    y = 3
else:
    print "You choose", y, ". A fine a choice!"
