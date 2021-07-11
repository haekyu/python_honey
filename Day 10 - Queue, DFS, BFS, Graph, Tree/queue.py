class Queue:

    # Attribute
    def __init__(self):
        self.store = []

    # Functions
    def is_empty(self):
        return len(self.store) == 0

        '''
        if len(self.store) == 0:
            return True
        else:
            return False
        '''

    def enqueue(self, e):
        self.store.append(e)

    def dequeue(self):

        if self.is_empty():
            return None
        else:
            first_in = self.store[0]
            self.store = self.store[1:]
            return first_in


Q = Queue()
Q.enqueue("abc")
Q.enqueue("wer")
Q.enqueue("2343")
print(Q.store)

first = Q.dequeue()
print("first:", first)
print(Q.store)
