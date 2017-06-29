# More on lists,

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')

# Insert an item at a given position. The first argument is the index of the element before which to insert
a.insert(2, -1)
a.append(333)
print(a)

print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
print(a.pop())

print(a)


# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

# splicing
del a[2:4]
print(a)

# Guess what this does
del a[:]
print(a)

# An example of list comprehension
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)


# Dictionaries

tel = {'ryan': 4098, 'jordan': 4139}
print(tel)

# add to an existing dictionary
tel['andrew'] = 4127
print(tel)

# access items as such
tel['ryan']

del tel['ryan']
tel['matt'] = 4127

print
tel

# view all the key values of the dictionary
print(tel.keys())

# check to see if a key exists
'jordan' in tel

# iterating over dictionaries

for key, value in tel.items():
    print key, value



# Review some example where we've seen class objects
# http://selenium-python.readthedocs.io webdriver API

class Athlete:
    # class variable shared by all instances
    status = "active"

    # define sports later
    sports = []

    # Do this later in the lesson
    def __init__(self):
        # self.status = status
        self.sports = []  #Creates a new empty list for each Athlete instance

    def info(self):
        print("Current athletic status: {}".format(self.status))

    def add_sport(self, sport):
        self.sports.append(sport)

    def get_batting_average(self, atBats):
        hits = sum(atBats)
        ab = len(atBats)
        return float(hits)/ab

# Initialize and instance of the our class
mason = Athlete()

# Run the function
mason.info()

# We can also access our class variable
print(mason.status)

# Explore the behavior of the variable
# First, create another class instance

joe = Athlete()
joe.status = "retired"

# Check that each status is still correct
print(joe.status)
print(mason.status)


# demonstrate unexepected behavior of shared class variables
# add sports
mason.add_sport('baseball')
joe.add_sport('swimming')

print(joe.sports)

# WHOAH! joe doesn't play baseball.  The list
# sports is being shared by all Athlete instances
# add __init__ to rememdy

# Now run the code and we are okay
print(mason.sports)

# In fact, we should define status in the __init__ fuction
# since it is not consistent accross all instances.


# we can define functions that return usefull stuff
# eg, batting average

atBats = [1,0,0,1,1,0,0,0]

# This function includes a return statement, so we can
# expect a value and store it in a variable and
# use it for something
battingAvg = mason.get_batting_average(atBats)

print(battingAvg)
