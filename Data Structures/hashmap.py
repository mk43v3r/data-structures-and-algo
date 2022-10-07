from linked_list import LinkedList

class HashMap:
    def __init__(self, hashfunc, arrsize = 100):
        self.arr = [None for _ in range(arrsize)]
        self.arrsize = arrsize
        self._hashfunc = hashfunc

    def insert(self, key, value):
        hashedkey = self._hashfunc(key) % self.arrsize
        elem = self.arr[hashedkey]
        if (elem == None):
            elem = LinkedList()
            self.arr[hashedkey] = elem

        for n in elem.iterator():
            if (n.value[0] == key):
                raise Exception("An entry with the same key value already exists")
        
        elem.append((key, value))

    def find(self, key):
        hashedkey = self._hashfunc(key) % self.arrsize
        elem = self.arr[hashedkey]

        if (elem == None):
            return None

        for n in elem.iterator():
            if (n.value[0] == key):
                return n.value[1]
        
        return None
    
    def delete(self, key):
        hashedkey = self._hashfunc(key) % self.arrsize
        elem = self.arr[hashedkey]

        if (elem == None):
            return None
        
        prev, curr = None, None

        for n in elem.iterator():
            prev =  curr
            curr = n
            if (n.value[0] == key):
                if (prev == None):      # Found node is the first one
                    return elem.remove()
                else:
                    prev.next = curr.next
                    return curr
        
        return None