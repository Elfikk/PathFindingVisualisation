#min-binary heap implementation
#A binary heap is a binary tree, in which the children of any node 
#are always smaller/larger than the parent (max/min heaps respectively)
#The heap is a complete tree - each level is filled before the next 
#depth level is started.

class Min_Heap():

    def __init__(self, nodes = [], data = None):
        self.nodes = nodes

        #No passed data possible - backwards compability.
        if data == None:
            self.data = [None for x in range(len(nodes))]
        else:
            self.data = data
            
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
        #Returns indices of a node's children, if they exist.
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
        child_data = self.data[child_index]

        self.nodes[child_index] = self.nodes[parent_index]
        self.data[child_index] = self.data[parent_index]

        self.nodes[parent_index] = child
        self.data[parent_index] = child_data

    def swap_up(self, child_index):
        #Swaps child with parent given the childs index.
        parent_index = parent_index(child_index)
        self.swap(child_index, parent_index)

    def insert(self, value, data = None):
        #Inserts a new value to the min heap. Checks if the new value is 
        #smaller than its parent and swaps if so, repeating the check until
        #it has risen appropriately.
        self.nodes.append(value)
        self.data.append(data)
        value_index = len(self.nodes) - 1

        legitimate = False

        while not legitimate and value_index > 0:

            parent_index = self.parent_index(value_index)

            if self.nodes[value_index] >= self.nodes[parent_index]:
                legitimate = True
            else:
                self.swap(value_index, parent_index)
                value_index = parent_index

    def make_heap(self):
        #Checks if the heap is legitimate, by visiting each node and swapping
        #appropriately. Run in __init__ only.

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

    def pop(self):
        #Swaps element at the extreme and root and then makes fixes as it 
        #goes along, by always swapping with the smallest value possible.

        true_value = self.nodes[0]
        true_data = self.data[0]

        extreme_value = self.nodes[-1]

        self.swap(0, -1)

        self.nodes = self.nodes[:-1]
        self.data = self.data[:-1]

        extreme_index = 0
        children_indices = self.child_indices(extreme_index)
        stop = False #When no swaps made, can stop earlier.

        while len(children_indices) > 1 and stop == False:

            stop = True
            left_index, right_index = children_indices
            left, right = self.nodes[left_index], self.nodes[right_index]

            if left < right:
                if left < extreme_value:
                    self.swap(left_index, extreme_index)
                    extreme_index = left_index
                    stop = False
            else:
                if right < extreme_value:
                    self.swap(right_index, extreme_index)
                    extreme_index = right_index
                    stop = False

            children_indices = self.child_indices(extreme_index)

        if len(children_indices) == 1:
            if extreme_value > self.nodes[children_indices[0]]:
                self.swap(extreme_index, children_indices[0])

        return true_value, true_data

    def __len__(self):
        return len(self.nodes)

    def remove_by_data(self, data, data_index = None):

        subset = self.data
        if data_index != None:
            subset = [x[data_index] for x in self.data]

        index = None
        length = len(subset)
        i = 0
        while i < length and index == None:
            if subset[i] == data:
                index = i
            i += 1

        if index == None:
            raise IndexError("No data.") 

        extreme_value = self.nodes[-1]

        self.swap(index, -1)

        self.data = self.data[:-1]
        self.nodes = self.nodes[:-1]

        # print(index)

        extreme_index = index
        children_indices = self.child_indices(extreme_index)

        # print(children_indices)

        stop = False #When no swaps made, can stop earlier.

        # print(self.nodes)
        # print(self.data)

        while len(children_indices) > 1 and stop == False:

            stop = True
            left_index, right_index = children_indices
            left, right = self.nodes[left_index], self.nodes[right_index]

            if left < right:
                if left < extreme_value:
                    # print(1)
                    self.swap(left_index, extreme_index)
                    extreme_index = left_index
                    stop = False
            else:
                if right < extreme_value:
                    # print(2)
                    self.swap(right_index, extreme_index)
                    extreme_index = right_index
                    stop = False

            children_indices = self.child_indices(extreme_index)

            # print(self.nodes)
            # print(self.data)


        if len(children_indices) == 1:
            # print(3)
            if extreme_value > self.nodes[children_indices[0]]:
                self.swap(extreme_index, children_indices[0])
    
        # print(self.nodes)
        # print(self.data)        


if __name__ == "__main__":
    #I should just write unit tests - automation is nice...
    #Actually definitely - Ive written 13 tests abd adding more and checking
    #I havent broken more stuff in the process is too much for me.

    a = Min_Heap() #Initiliases with no input.
    print("a:", a.nodes)

    b = Min_Heap([15, 2, 6]) #15 and 2 should be swapped.
    print("b:", b.nodes) #Passed.

    c = Min_Heap([1]) #Throws a fit with checker if only one element present?
    print("c:", c.nodes) #No - passed.

    d = Min_Heap([1,2]) #What about for 2 elements.
    print("d:", d.nodes) #No - passed.

    e = Min_Heap([15, 2, 6, 1]) #Final config: [1, 2, 15, 6]
    print("e:", e.nodes) #Passed

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

    k = Min_Heap([1,2,3]) #Does insert work? 
    print("k1:", k.nodes) #Expect [1,2,3] - Passed
    k.insert(4) 
    print("k2:", k.nodes) #Expect[1,2,3,4] - Passed

    l = Min_Heap([]) #Does insert work for empty heaps?
    l.insert(1)
    print("l:", l.nodes) #Expected [1] - Passed

    m = Min_Heap([1,2,3]) #Minimum moving up from second level.
    m.insert(0)
    print("m:", m.nodes) #Expected [0, 1, 3, 2] - Passed

    n = Min_Heap([1,2,5,3,6,8,10,4,7,9])
    n.insert(0) #Expected [0,1,5,3,2,8,10,4,7,9,6]
    print("n:", n.nodes) #Passed.

    # o = Min_Heap([0,1,2,3,4,5], data = ["a", "b", "c", "d", "e", "f"])
    # print(o.nodes, o.data)
    # o.remove_by_data("a")
    # print("Post-op:", o.nodes, o.data)