# -*- coding: utf-8 -*-
"""
    foobar-google challenge
    By Baptiste PICARD
    05/11/2021

    https://github.com/n3a9/google-foobar/blob/master/Level%201/minion_task_scheduling/problem.md
"""
# Imports
import unittest
from functools import reduce
from itertools import islice, product

# Environment
# Show full diff in unittest
unittest.util._MAX_LENGTH=2000

# Part 1
def answer(data, n):
    '''
        Level 1: Minion task scheduling

        Entries
        --------
        data: list
        n: int
        
        -> OK
    '''
    if not isinstance(data, list) and isinstance(n, int):
        raise TypeError('Bad types')
    if len(data) >= 100:
        raise ValueError('List length')
    results = []
    for item in sorted(set(data), key=data.index):
        if not data.count(item) > n:
            results.append(item)
    return results

# Part 2
def answer_2(path):
    '''
        Level 2: En route salutate

        Entries
        --------
        path: str
        
        -> OK
    '''
    if not isinstance(path, str):
        raise TypeError('Bad Type')
    if not all([character in ['<', '>', '-'] for character in list(path)]):
        raise ValueError('Bad character')
    if not (list(path).count('<') >= 1
            and list(path).count('<') <= 100
            and list(path).count('>') >= 1
            and list(path).count('>') <= 100):
                raise ValueError('count(<) = {} | count(>) = {}'\
                                 .format(list(path).count('<'),
                                         list(path).count('>')))
    total = 0
    for i,j in enumerate(path):
        if j == '>':
           total = total + 2 * path[i:].count('<')
    return total


# Part 3
def answer_3(my_list, my_int):
    '''
        Level 2: Number station coded messages

        Entries
        --------
        my_list: list
        my_int: int
    '''
    if not (isinstance(my_list, list)
            and isinstance(my_int, int)):
        raise TypeError('Bad types')
    if len(my_list) >= 100:
        raise ValueError('List length')
    if not my_list:
        raise EmptyListError(message='Empty list')
    if not all([item>=0 for item in my_list]):
        raise NotAllNonEmptyError(message='Not all ')
    if not my_int >= 0:
        raise ValueError
    for idx_x in range(len(my_list)):
        for idx_y in range(len(my_list[idx_x:])):
            if sum(my_list[idx_x:idx_x + idx_y]) == my_int:
                return [idx_x, idx_x + idx_y - 1]
    return [-1, 1]

def answer_4(my_list):
    '''
        Find the access codes

        Entries
        --------
        my_list: list
    '''
    if not isinstance(my_list, list):
        raise TypeError('Bad type')
    results = []
    for idx_x, item_x in enumerate(my_list):
        tmp_list = my_list.copy()
        tmp_list.pop(idx_x)
        for idx_y, item_y in enumerate(tmp_list):
            if not item_y % item_x:
                tmp_list_1 = tmp_list.copy()
                tmp_list_1.pop(idx_y)
                for item_z in tmp_list_1:
                    if not item_z % item_y:
                        if not (item_x, item_y, item_z) in results:
                            results.append((item_x, item_y, item_z))
    return len(results)

def answer_5(start, length):
    '''
         Queue To Do
    :param start: int
    :param length: int
    :return: int
    '''

    def queue_to_subqueue(my_list, chunck_size):
        '''
            Transform queue=list into list of sublist usiçng chunkc_size
        :param my_list:
        :param chunck_size: int
        :return: list
        '''
        sub_queues = []
        for size in range(len(my_list)):
            sub_queues = sub_queues + my_list[size][size:]
        return sub_queues

    if not (isinstance(start, int) and isinstance(length, int)):
        raise TypeError('Bad type.')
    if not (start >=0 and start <= 2000000000):
        raise ValueError(' 0<= start <= 20*10e+9')
    queue = [start]
    for i, j in product(range(length + 1), range(length)):
        if j == length - 1:
            queue.append('/')
            continue
        if queue[-1] == '/':
            queue.append(queue[-2] + 1)
        else:
            queue.append(queue[-1] + 1)
    queue_to_subqueues, subqueue = [], []
    for i in range(len(queue[:-1])):
        if queue[i] == '/':
            queue_to_subqueues.append(subqueue)
            subqueue = list(['/'])
        else:
            subqueue.append(queue[i])
    queue_to_subqueuea = queue_to_subqueue(queue_to_subqueues, length)
    return reduce(lambda x, y: x ^ y, queue_to_subqueuea)

def answer_6(n):
    '''
        The Grandest Staircase Of Them All
    :param n: int
    :return:
    '''
    if n<3 or n>200:
        raise ValueError(' 3=> n is > 200')

    def get_all_decomposition(my_integer):
        '''
        https://cs.stackexchange.com/questions/24552/divide-an-integer-into-the-sum-of-consecutive-positive-numbers
        :param my_integer: int
        :return: list
        '''
        x =  
        y =
        results = []
        return results
    def test_result(my_tuple):
        '''

        :param my_tuple: tuple
        :return: bool
        '''
        return True
    return n

# Class
class EmptyListError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class NotAllNonEmptyError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class TestStringMethods(unittest.TestCase):
    
    def test_answer(self):
        self.assertEqual(0, 0)
        with self.assertRaises(TypeError):
            assert answer(1, 1)
            assert answer([], [])
        with self.assertRaises(ValueError):
            assert answer(list(range(101)), 1)
        assert answer([], 1) == []
        assert answer([1, 2, 3], 0) == []
        assert answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1, 4]
        assert answer([1, 2, 3], 6) == [1, 2, 3]
        assert answer([5, 10, 15, 10, 7] , 1) == [5, 15, 7]

    def test_answer_2(self):
        with self.assertRaises(TypeError):
            answer_2(1)
            answer_2([])
        with self.assertRaises(ValueError):
            answer_2('aeaeza')
            answer_2('aeae ')
        assert answer_2(">----<") == 2
        assert answer_2("<<>><") == 4
        assert answer_2("--->-><-><-->-") == 10
    
    def test_answer_3(self):
        with self.assertRaises(TypeError):
            answer_3(1, 1)
            answer_3([], {})
        with self.assertRaises(EmptyListError):
            answer_3([], 1)
        with self.assertRaises(NotAllNonEmptyError):
            answer_3([1, -1, 5], 1)
            answer_3([1, -1, 5], -4)
        with self.assertRaises(ValueError):
            answer_3([1, 1, 5], -6)
            answer_3(list(range(101)), 1)
        assert answer_3([4, 3, 10, 2, 8], 12) == [2, 3]
        assert answer_3([1, 2, 3, 4], 15) == [-1, 1]

    def test_answer_4(self):
        with self.assertRaises(TypeError):
            answer_4(1)
            answer_4({})
        assert answer_4([1, 1, 1]) == 1
        assert answer_4([1, 2, 3, 4, 5, 6]) == 3

    def test_answer_5(self):
        with self.assertRaises(TypeError):
            answer_5([], [])
            answer_5(0, [])
            answer_5(0, {})
        with self.assertRaises(ValueError):
            answer_5(-1, 0)
            answer_5(200000000000, 0)
        answer_5(0, 3) == 2
        answer_5(17, 4) == 14

    def test_answer_6(self):
        with self.assertRaises(ValueError):
            answer_6(201)
            answer_6(2032148)
            answer_6(0)
            answer_6(1)
            answer_6(2)
        answer_6(3) == 3
        answer_6(6) == 6

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # print(answer_5(0, 3))
    # print(answer_5(17, 4))
