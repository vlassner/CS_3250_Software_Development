'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: A model for a BST (Binary Search Tree)
'''

class BSTNode: 

    def __init__(self): 
        self.__value = None
        self.__left  = None
        self.__right = None   

    def add(self, value): 
        if not self.__value: 
            self.__value = value   
        elif value < self.__value: 
            self.__left = BSTNode.__add(self.__left, value)
        elif value > self.__value: 
             self.__right = BSTNode.__add(self.__right, value)

    @staticmethod
    def __add(current, value):
        if not current: 
            bst_node = BSTNode()
            bst_node.__value = value 
            return bst_node
        if value < current.__value: 
            current.__left = BSTNode.__add(current.__left, value)
        elif value > current.__value: 
             current.__right = BSTNode.__add(current.__right, value)
        return current

    @staticmethod
    def __print(current, tabs = ""): 
        out = ""
        if current:
            out += tabs + str(current.__value) + '\n'
            out += BSTNode.__print(current.__left, tabs + '   ')
            out += BSTNode.__print(current.__right, tabs + '   ')            
        return out
        
    def __str__(self):
        return BSTNode.__print(self, '')
    
    @staticmethod
    def __in_order(current) -> list: 
        values = []
        if (current):
            values += BSTNode.__in_order(current.__left)
            values.append(current.__value)
            values += BSTNode.__in_order(current.__right)
        return values
    
    # TODO: implement an iterator
    def __iter__(self):
        self.__lst = BSTNode.__in_order(self)
        return self
    
    def __next__(self):
        if self.__lst:
            #curr = self.__lst[0]
            #self.lst = self.__lst[1:]
            #return curr
            return self.__lst.pop(0)
        raise StopIteration

    # TODO: replace the iterator with a generator
    def __iter__(self): 
        if (self):
            if self.__left:
                yield from iter(self.__left)
            yield self.__value
            if self.__right:
                yield from iter(self.__right)
         
