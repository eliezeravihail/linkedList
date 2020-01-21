import linkedList as L

myLL = L.linkedList()
myLL.pushToHead("last item")
myLL.pushToHead("first item")
print(myLL.popFirst())
print(myLL.popFirst())

#output:
#first item
#last item
