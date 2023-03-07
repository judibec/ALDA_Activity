import unittest
from functions import sorting_methods as sm

listBubble = [50, 36, 71, 115, 4, 29, 61, 279, 43]
bubbleSort = [4, 29, 36, 43, 50, 61, 71, 115, 279]

listMerge = [15, 5, 24, 80, 3, 19, 0, 39, -2, 72, 85]
mergeSort = [-2, 0, 3, 5, 15, 19, 24, 39, 72, 80, 85]

listShell = [120, 30, 5, 1, 500, 4, 7, 52, 10]
shellSort = [1, 4, 5, 7, 10, 30, 52, 120, 500]


class testSortingMethods(unittest.TestCase):
    def test_bubble_sort(self):
        sm.bubbleSort(listBubble)
        self.assertEqual(bubbleSort, listBubble)

    def test_merge_sort(self):
        sm.mergeSort(listMerge)
        self.assertEqual(mergeSort, listMerge)

    def test_shell_sort(self):
        sm.shellSort(listShell)
        self.assertEqual(shellSort, listShell)


if __name__ == "__main__":
    unittest.main
