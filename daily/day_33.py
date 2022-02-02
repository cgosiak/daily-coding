import unittest
from typing import List
from statistics import median

def running_median(input_list: List[float]) -> List[float]:
    running_median_list: List[int] = []
    for i in range(len(input_list)):
        subset: List[float] = input_list[:i+1]
        running_median_list.append(median(subset))
    return running_median_list


def running_average(input_list: List[float]) -> List[float]:
    running_average_list: List[float] = []

    average = None
    for i in range(len(input_list)):
        if i == 0:
            average = input_list[i]
        else:
            previous_total: float = average * i
            average = (previous_total + input_list[i]) / (i + 1)

        running_average_list.append(average)
    
    return running_average_list


class TestRunninMedian(unittest.TestCase):

    def test_1(self):
        self.assertEquals(running_median([2, 1, 5, 7, 2, 0, 5]), [2, 1.5, 2, 3.5, 2, 2, 2])

    def test_2(self):
        self.assertEquals(running_average([2, 4, 6]), [2, 3, 4])


unittest.main()
