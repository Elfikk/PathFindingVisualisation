import unittest
from Heap import Min_Heap

class HeapTest(unittest.TestCase):

    def test_init_empty_heap(self):
        a = Min_Heap()
        self.assertEqual(a.nodes, [])

    def test_make_heap_one_swap(self):
        b = Min_Heap([15, 2, 6])
        self.assertEqual(b.nodes, [2, 6, 15])

    def test_single_element_heap(self):
        c = Min_Heap([1])
        self.assertEqual(c.nodes, [1])

    def test_make_heap_no_swaps(self):
        d = Min_Heap([1,2])
        self.assertEqual(d.nodes, [1,2])

    def test_two_level_heap_swaps(self):
        #Ends on a left node.
        e = Min_Heap([15, 2, 6, 1])
        self.assertEqual(e.nodes, [1, 2, 15, 6])

    def test_two_level_heap_swags_right(self):
        #Ends on a right node.
        f = Min_Heap([15, 2, 6, 1, 20])
        self.assertEqual(f.nodes, [1, 2, 15, 6, 20])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            g = Min_Heap([15, 2, "a", 1, 20])
        
    def test_mixed_data_types(self):
        h = Min_Heap([15, 2.0, 6.5])
        self.assertEqual(h.nodes, [2.0, 6.5, 15])

    def test_make_heap_three_level(self):
        i = Min_Heap([9,8,7,6,5,4,3,2,1])
        self.assertEqual(i.nodes, [1,2,4,3,8,7,9,5,6])

    def test_make_heap_three_level_right(self):
        j = Min_Heap([10,9,8,7,6,5,4,3,2,1])
        self.assertEqual(j.nodes, [1,2,5,3,6,8,10,4,7,9])

    def test_insert_no_swaps(self):
        k = Min_Heap([1,2,3])
        k.insert(4) 
        self.assertEqual(k.nodes, [1,2,3,4])

    def test_insert_to_empty(self):
        l = Min_Heap([]) 
        l.insert(1)
        self.assertEqual(l.nodes, [1])

    def test_insert_two_levels(self):
        m = Min_Heap([1,2,3]) 
        m.insert(0)
        self.assertEqual(m.nodes, [0,1,3,2])

    def test_insert_three_levels(self):
        n = Min_Heap([1,2,5,3,6,8,10,4,7,9])
        n.insert(0)
        self.assertEqual(n.nodes, [0,1,5,3,2,8,10,4,7,9,6])

    def test_pop_simple(self):
        heap = Min_Heap([0,1,2,5,4])
        head = heap.pop()
        self.assertEqual(head, 0)
        self.assertEqual(heap.nodes, [1,4,2,5])

    def test_pop_case2(self):
        heap = Min_Heap([1,2,3,4,5,6,7,8,9,10])
        root = heap.pop()
        self.assertEqual(root, 1)
        self.assertEqual(heap.nodes, [2,4,3,8,5,6,7,10,9])

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            heap = Min_Heap()
            heap.pop()

    def test_pop_one_node(self):
        heap = Min_Heap([0])
        head = heap.pop()
        self.assertEqual(head, 0)

    def test_insert_then_pop(self):
        heap = Min_Heap([0, 2])
        heap.insert(-1)
        self.assertEqual(heap.nodes, [-1, 2, 0]) #-1 and 0 should be swapped
        root = heap.pop()
        self.assertEqual(root, -1)
        self.assertEqual(heap.nodes, [0,2])

if __name__ == "__main__":
    unittest.main()