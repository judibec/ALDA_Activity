import unittest
from functions import sorting_methods as sm

listBubble = [50, 36, 71, 115, 4, 29, 61, 279, 43]
bubbleSort = [4, 29, 36, 43, 50, 61, 71, 115, 279]

listMerge = []
mergeSort = []

listShell = []
shellSort = []


class testSortingMethods(unittest.TestCase):

    def test_bubble_sort(self):
        sm.bubbleSort(listBubble)
        self.assertEqual(bubbleSort, listBubble)

    def test_merge_sort(self):
        sm.bubbleSort(listBubble)
        self.assertEqual(bubbleSort, listBubble)

    def test_shell_sort(self):
        sm.bubbleSort(listBubble)
        self.assertEqual(bubbleSort, listBubble)


if __name__ == '__main__':
    unittest.main
