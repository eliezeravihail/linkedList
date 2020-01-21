class node(object):
    """simple node to linked list"""
    _value = None
    _next = None
    _prev = None

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value


class linkedList(object):
    """simple linked list"""
    _head = None  # to be iterator
    _tail = None  # to be iterator

    def __init__(self):
        self._tail = self._head = None

    def getHead(self):
        # return pointer to first, it is return pointer, bcuse _head is mutable object
        return self._head

    def getTail(self):
        # return pointer to tail, it is return pointer, bcuse _tail is mutable object
        return self._tail

    def popFirst(self):
        """return value of First item and remove it from list (to fact not remove, python use GG)"""
        temp = self._head._value
        self._head = self._head._next
        if self._head is not None:
            self._head._prev = None
        return temp

    def popLast(self):
        """return  value of last item and remove it from list (to fact not remove, python use GG)"""
        temp = self._tail._value
        if self._tail._prev is not None:
            self._tail = self._tail._prev
            self._tail._next = None
        return temp

    def pushToHead(self, value):
        if self._head is not None:
            tempHead = self._head
            temp = node(value)
            self._head._prev = temp
            self._head = temp
            self._head._next = tempHead
        else:
            self._tail = self._head = node(value)

    def pushToLast(self, value):
        if self._tail is not None:
            temp = node(value)
            temp._prev = self._tail
            self._tail._next = temp
            self._tail = temp
        else:
            self._tail = node(value)

    def __str__(self):
        str = ""
        iterator =self._head
        while iterator is not None:
            str += f"=> {iterator._value}"
            iterator = iterator._next
        if str != "":
            return str
        else:
            return " "
