#min-binary heap implementation
#A binary heap is a binary tree, in which the children of any node 
#are always smaller/larger than the parent (max/min heaps respectively)
#The heap is a complete tree - each level is filled before the next 
#depth level is started.

class Min_Heap():

    def __init__(self, nodes = []):
        self.nodes = nodes
        if len(self.nodes):
            self.make_heap()

    def parent_index(self, child_index):
        #Works out the index of the parent node in the node list for a 
        #given index.
        if child_index % 2: #True if odd
            parent_index = (child_index - 1)//2
        else:
            parent_index = child_index//2 - 1

        return parent_index

    def child_indices(self, parent_index):
        max_index = len(self.nodes) - 1
        left = 2 * parent_index + 1
        if left > max_index:
            return []
        elif left == max_index:
            return [left]
        else:
            return [left, left + 1]

    def swap(self, child_index, parent_index):
        #Swaps two elements of the heap.
        #Completely symmetrical so can pass child or parent indices 
        #either way around.
        child = self.nodes[child_index]
        self.nodes[child_index] = self.nodes[parent_index]
        self.nodes[parent_index] = child

    def swap_up(self, child_index):
        #Swaps child with parent.
        parent_index = parent_index(child_index)
        self.swap(child_index, parent_index)

    def insert(self, value):
        #Inserts a new value to the min heap. Checks if the new value is 
        #smaller than its parent and swaps if so, repeating the check until
        #it has risen appropriately.
        self.nodes.append(value)
        value_index = len(self.nodes) - 1

        legitimate = False

        while not legitimate:

            parent_index = self.parent_index(value_index)

            if self.nodes[value_index] >= parent_index:
                legitimate = True
            else:
                self.swap(value_index, parent_index)

    def make_heap(self):
        #Checks if the heap is legitimate, by visiting each node and swapping
        #appropriately. 

        max_index = len(self.nodes) - 1

        to_visit = list(range(max_index, 0, -1))

        while len(to_visit) != 0:

            child_index = to_visit[0]

            child_value = self.nodes[child_index]
            parent_index = self.parent_index(child_index)
            parent_value = self.nodes[parent_index]

            if child_value < parent_value:
                self.swap(child_index, parent_index)

                children_indices = self.child_indices(child_index)

                #Always visiting from the right most, deepest node possible.
                to_visit = children_indices[::-1] + to_visit[1:]
            else:
                to_visit = to_visit[1:]

if __name__ == "__main__":

    a = Min_Heap() #Initiliases with no input.
    print("a:", a.nodes)

    b = Min_Heap([15, 2, 6]) #15 and 2 should be swapped.
    print("b:", b.nodes) #Passed.

    c = Min_Heap([1]) #Throws a fit with checker if only one element present?
    print("c:", c.nodes) #No - passed.

    d = Min_Heap([1,2]) #What about for 2 elements.
    print("d:", d.nodes) #No - passed.

    e = Min_Heap([15, 2, 6, 1]) #Final config: [1, 2, 6, 15]
    print("e:", e.nodes) #Failed. Left 

    f = Min_Heap([15, 2, 6, 1, 20]) #Final config: [1, 2, 15, 6, 20]
    print("f:", f.nodes) #Passed

    # g = Min_Heap([15, 2, "a", 1, 20]) #Should throw Type Error
    # #Passed.

    h = Min_Heap([15, 2.0, 6.5]) #Should work fine even with floats + ints
    print("h:", h.nodes) #Passed.
    #(A test for my sanity)

    i = Min_Heap([9,8,7,6,5,4,3,2,1]) #A long boi for the sake of it.
    #Expected: [1,2,4,3,6,7,9,5,6]
    print("i:", i.nodes) #Passed.

    j = Min_Heap([10,9,8,7,6,5,4,3,2,1]) #A long boi for the sake of it.
    #Expected: [1,2,5,3,6,8,10,4,7,9]
    print("j:", j.nodes) #Passed.
    #Deviates from http://btv.melezinek.cz/binary-heap.html but I reckon
    #this is down to biases to left and right edges, as following my algo
    #on paper gives the output - the bias shouldnt matter at the end of 
    #the day, thats arbitrary.