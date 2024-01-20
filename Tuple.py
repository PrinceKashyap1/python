# (1) Create a tuple and tuple always in parenthesis
a = ()
print(a)
# Output:() empty tuple

#  (2) creating a tuple in singular element
b = (1,)
print(b)
print(type(b))
# output:(1,) <class 'tuple'>
# to create a singular tuple enter the element in tuple with comma
# if not entering with comma then it is work as a integer


# (3) create a tuple with different datatype
c = (2, 2.3, "hello", 9, "friend")
print(c)
# output: (2, 2.3, "hello", ,"friend")


# (4) access the tuple element in tuple
d = (2, 2.3, "xyz", 7, "abc")
print(d[0])
print(d[2])
# output:2   xyz


#  (5) delete  the tuple del function it is not delete elements of tuple but  it delete whole tuple
e =(1, 2, 3, 4, 5)
print(type(e))
# del e
print(type(e))
# output:<class 'tuple'>    after deletion:  NameError: name 'e' is not defined


# (6) slicing a tuple
f = (2, 3, 4, 5.5, 5.7)
print(f[0:3])  # it slice  0 to 3 of index
print(f[:4])  # starting index not give to  give end index it start always index 0
print(f[:])  # also print all element  to length of tuple
print(f[::2])  # given only increment condition it print index +2 on the given increment
# output:(2, 3, 4)
#        (2, 3, 4, 5.5)
#        (2, 3, 4, 5.5, 5.7)
#        (2, 4, 5.7)


# (7) concatanate a tuple
g = (2, "hello")
h = (3, "Good morning")
print(g + h)
# output: (2, 'hello', 3, 'Good morning')



# (8) finding the length of tuple
i = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(i))
# output:10


# (9) tuple in a loop and tuple is immutable it cannot change or access of value
# whole tuple onlt 1 indexing
j = (1, 2, 3, 4, "hello")
for i in j:
    print(j)
# output:
# (1, 2, 3, 4, 'hello')
# (1, 2, 3, 4, 'hello')
# (1, 2, 3, 4, 'hello')
# (1, 2, 3, 4, 'hello')
# (1, 2, 3, 4, 'hello')



# (10) typecast   one datatype to another
k = (1, 2, 3)
print(list(k))
# output:[1, 2, 3]


# (11) campare the element of tuple
# l =(1, 2, 3)
# m = (1, 2, 3, 4)
# if(cmp(l,m) != 0):
#     print("same")
# else:
#     print("not same")


# (12) Maximum number in tuple
n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(max(n))
# output:10


# (13) Minimum number in tuple
n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(min(n))
# output:1



