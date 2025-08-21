'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: OOP Practice
'''

from models import Rectangle, SingletonRectangle, Vehicle, Car, Truck, StackAdapter
from bst import BSTNode

# TODO instantiate a rectangle using the default constructor and show its perimeter
rec = Rectangle(-1,3)
print(f'{rec}\'s perimeter is {rec.perimeter()}')

# TODO check if you can change the rectangle's width by accessing its width variable directly
rec.width = 2

# TODO instantiate another rectangle with width=2 and height=3 and show its area
rec2 = Rectangle(2,3)
print(f'{rec2}\'s perimeter is {rec2.area()}')

# TODO instantiate a Honda Civic Si FG4 2012 sedan car and show it as a string
v1 = Car("Honda", "Civic Si FG4", 2012, "Sedan")
print(v1)

# TODO instantiate a Ford F350 2000 with classification set to 3 and show it as a string
v2 = Truck("Ford", "F350", 2000, 3)
print(v2)

# TODO using BSTNode, create a BST with [15, 6, 56, 23, 1, 8, 9, 77]; display the BST after
bst = BSTNode()
for v in [15, 6, 56, 23, 1, 8, 9, 77]:
    bst.add(v)
print(bst)

# TODO iterate over the BST
for e in bst:
    print(e)

gen = iter(bst)
print(next(gen))
print(next(gen))

# TODO use list comprehension to get the even numbers only
lst = [15, 6, 56, 23, 1, 8, 9, 77]
lst_even = [ x for x in lst if x % 2 == 0]
print(lst_even)

# TODO use list comprehension to get the odd numbers only
lst = [15, 6, 56, 23, 1, 8, 9, 77]
lst_odd = [ x for x in lst if x % 2 != 0]
print(lst_odd)

# TODO use list comprehension to generate another list doubling the numbers
lst_double = [ x*2 for x in lst]
print(lst_double)

# TODO use filter with lambda to get the even numbers only 
lst_even = list(filter(lambda _ : _ % 2 == 0, lst)) 
print(lst_even)
# (_) placeholder variable

# TODO use filter with lambda to get the odd numbers only
lst_odd = list(filter(lambda _ : _ % 2 == 1, lst)) 
print(lst_odd)

# TODO use map with a lambda to double each number
lst_double = list(map(lambda _ : _ * 2, lst)) 
print(lst_double)

rec_a = SingletonRectangle.get_instance(2,3)
print(rec_a)
rec_b = SingletonRectangle.get_instance(5,10)
print(rec_b) #original rectangle a will be maintained and not replaced with a new rectangle


stk = StackAdapter()
stk.push(5)
stk.push(2)
stk.push(3)
print(stk)
stk.pop()
print(stk)
stk.pop()
stk.pop()
stk.pop()
print(stk)