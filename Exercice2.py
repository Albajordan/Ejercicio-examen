class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]   
        del self.items[topIdx]
        return item
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to pop an empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]   
        return item

    def isEmpty (self):
        return len(self.items) == 0
    
    def multipop(self, k):
        #First we create the list in which we store the pop items
        list1=[]
        #We pop k number of items from the stack
        for num in range(0,k):
            item=self.pop()
            list1.append(item)
            #If the stack is empty, we stop the function
            if self.isEmpty()==True:
                break
        #The function returns the lists with all the pop items from the stack
        return list1
    
            
            

my_stack = Stack()
 
# append() function to push
# element in the stack
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
my_stack.push('d')
my_stack.push('e')
my_stack.push('f')
my_stack.push('g')
my_stack.push('h')


print ("pop one item")
item = my_stack.pop()
print(item)
print("multipop")
items_parciales = my_stack.multipop(4)
for item_iter in items_parciales:
    print(item_iter)
print("normal")
while my_stack.isEmpty()==False:
    item = my_stack.pop()
    print(item)
    
