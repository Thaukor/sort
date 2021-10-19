import unittest
import sort

class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
        
    def test_quick_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.quick_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])
        
    def test_quick_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.quick_sort(a)
        self.assertEqual(a, [1])
    
    def test_selection_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.selection_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
      
    def test_selection_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.selection_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])
    
    def test_selection_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.selection_sort(a)
        self.assertEqual(a, [1])
        
    def test_selection_sort_4(self):
        """
        Prueba para lista ya ordenada
        """
        a = [1, 2, 3, 5, 7, 9]
        sort.selection_sort(a)
        self.assertEqual(a, [1, 2, 3, 5, 7, 9])
        
    def test_bubble_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.bubble_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])
        
    def test_bubble_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.bubble_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])

    def test_bubble_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.bubble_sort(a)
        self.assertEqual(a, [1])

    def test_bubble_sort_4(self):
        """
        Prueba para lista ya ordenada
        """
        a = [1, 2, 3, 5, 7, 9]
        sort.bubble_sort(a)
        self.assertEqual(a, [1, 2, 3, 5, 7, 9])

        
if __name__ == '__main__':
    unittest.main()