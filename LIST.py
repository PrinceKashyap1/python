# creating a List Variable_name =  [ value1,value2...]in sqaure brackets its stores differents datatype values


# num = [1, 2, "set", 'hello', 2.8]
# num is use as list maaximum of code some are codes criteria are not for num where use other list


# Operation on List[]:-
# Insert, append, extend, remove, pop(),del, slice(), reverse(), len(), min(), max(), count()
# concatanate, multiply, index(), sort(), sorted, clear()


# (1) insert(index value, value to add )
# num.insert(0, 5)
# print(num)
# input: [1, 2, "set", 'hello', 2.8]
# output: [5, 1, 2, 'set', 'hello', 2.8]
# _______________________________________

# (2) append(value)  add a element at last of indexing of list
# if we add to list in list it compile as list as one element
# num.append(2)
# num.append([2, 3])
# num.append((7, 5))
# print(num)
# input: [1, 2, "set", 'hello', 2.8]
# output:[1, 2, 'set', 'hello', 2.8, 2, [2, 3], (7, 5)]
# _______________________________________

# (3) extend(val) add  a value of list or tuple in given list
# num.extend([7, 8])
# num.extend((3, 2))
# print(num)
#
# input: [1, 2, "set", 'hello', 2.8]
# output:[1, 2, 'set', 'hello', 2.8, 7, 8, 3, 2]
# __________________________________________

# (4)remove(val) remove given val find to remove at starting first it is find remove the given val
# num.remove(2)
# print(num)

# input:[1, 2, "set", 'hello', 2.8]
# output:[1, "set", 'hello', 2.8]
# ___________________________________________

# (5) pop() it remove from the last element of the list
# num.pop()
# print(num)
# input:[1, 2, "set", 'hello', 2.8]
# output:[1, 2, 'set', 'hello']
# ____________________________________________

# (6) del() is used delete the specific element of the list, here del is a keyword
# can also use to delete variables,list, or a part of list

# del num[1]
# print(num)
# input:[1, 2, "set", 'hello', 2.8]
# output:[1, 'set', 'hello', 2.8]
# ____________________________________________

# (7) slice() -> variable_name[start:end] it can display to specific index
# n = num[2:4]
# print(n)
# input:[1, 2, "set", 'hello', 2.8]
# output:['set', 'hello']
# _____________________________________________

# (8) reverse() reverse the list element list_name.reverse()
# num.reverse()
# print(num)
# input:[1, 2, "set", 'hello', 2.8]
# output:[2.8, 'hello', 'set', 2, 1]
# _____________________________________________

# (9) len() to find length of list
# c = len(num)
# print(c)
# input:[1, 2, "set", 'hello', 2.8]
# output:5
# _______________________________________________

# (10) min() to find minimum number of the list
# num1 = [2, 5, 3, 2, 1, 0, 6, 9]
# d = min(num1)
# print(d)
# input:[2, 5, 3, 2, 1, 0, 6, 9]
# output:0
# _______________________________________________

# (11) max to find max number of list
# min() to find minimum number of the list
# num1 = [2, 5, 3, 2, 1, 0, 6, 9]
# d = max(num1)
# print(d)
# input:[2, 5, 3, 2, 1, 0, 6, 9]
# output:9
# ________________________________________________

# (12) count() is used to count number how many times on list list_name(val)
# num1 = [2, 5, 3, 2, 2,  1, 0, 6, 9]
# f = num1.count(2)
# print(f)
# input:[2, 5, 3, 2, 1, 0, 6, 9]
# output:3
# _________________________________________________

# (13)concatanate -> when two string add to form a one list
# n1 = [1, 2, 3, 4]
# n2 = [5, 6, 7, 8]
# n = n1 + n2
# print(n)
# input():n1 = [1, 2, 3, 4]
#         n2 = [5, 6, 7, 8]
# output:[1, 2, 3, 4, 5, 6, 7, 8]
# __________________________________________________

# (14)multiply -> multiply a number and expand at number times
# c = num*2
# print(c)
# input:[1, 2, "set", 'hello', 2.8]
# output:[1, 2, 'set', 'hello', 2.8, 1, 2, 'set', 'hello', 2.8]
# ___________________________________________________

# (15) index() is return the index value list.index(val)
# c = num.index("hello")
# print(c)
# input:[1, 2, "set", 'hello', 2.8]
# output:3
# ___________________________________________________

# (16) sort()  is sort the  list in ascending order and works on original list
# num1 = [3, 2, 1, 4, 5, 6, 3, 8, 6]
# c = num1.sort()
# print(num1)
# print(c)

# input:[3, 2, 1, 4, 5, 6, 3, 8, 6]
# output:num1: [1, 2, 3, 3, 4, 5, 6, 6, 8]
#        c:  None
# ____________________________________________________

# (17) sorted() is sort the  list in ascending order and works on copy list
# num1 = [3, 2, 1, 4, 5, 6, 3, 8, 6]
# c = sorted(num1)
# print(num1)
# print(c)
# input:[3, 2, 1, 4, 5, 6, 3, 8, 6]
# output:num1:[3, 2, 1, 4, 5, 6, 3, 8, 6]
#           c:[1, 2, 3, 3, 4, 5, 6, 6, 8]
# ______________________________________________________

# (18) clear() is used to clear all element in list ( dictationary and tuple)  list.clear()
# num.clear()
# print(num)
# input:[1, 2, "set", 'hello', 2.8]
# output:[]
# _______________________________________________________

# (19) clone creating method
# num1 = num[:]
# del(num1[1:3])
# print(num)
# print(num1)
# output  means operation works on main variable this property is called clone
# input:[1, 2, 'set', 'hello', 2.8]
# output:[1, 'hello', 2.8]
# _____________________________________________________________________________________
# (20) aliasing method
# num1 = num
# del(num[1:3])
# print(num)
# print(num1)
# output  means operation works on main variable this property is called aliasing
# input:[1, 'hello', 2.8]
# output:[1, 'hello', 2.8]
