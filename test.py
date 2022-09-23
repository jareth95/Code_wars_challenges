from parameterized import parameterized
import unittest
import math


'''
The Story:
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview:
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting
'''

def enough(cap, on, wait):
    return max(0, wait - (cap - on))


class TestEnough(unittest.TestCase):
    @parameterized.expand([
        [10, 5, 5, 0],
        [100, 60, 50, 10],
        [20, 5, 5, 0],
    ])

    def test_enough(self, cap, on, wait, answer):
        self.assertEqual(enough(cap, on, wait), answer)

'''
Code as fast as you can! You need to double the integer and return it.
'''

def double_integer(i):
    return i*2


class TestDoubleIntegerMethods(unittest.TestCase):

    def test_double_integer(self):
        self.assertEqual(double_integer(2), 4)
        self.assertEqual(double_integer(-10), -20)
        self.assertEqual(double_integer(0), 0)
        self.assertEqual(double_integer(100), 200)

'''
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''

def add_binary(a,b):
    return bin(a+b)[2:]


class TestAddBinary(unittest.TestCase):

    def test_add_binary(self):
        self.assertEqual(add_binary(1,1),"10")
        self.assertEqual(add_binary(0,1),"1")
        self.assertEqual(add_binary(1,0),"1")
        self.assertEqual(add_binary(2,2),"100")
        self.assertEqual(add_binary(51,12),"111111")
       
'''
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
'''

def find_smallest_int(arr):
    return min(arr)

class TestFindSmallest(unittest.TestCase):

    def test_find_smallest_int(self):
        self.assertEqual(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        self.assertEqual(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        self.assertEqual(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)

'''
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''

def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'
    

class TestGetGrade(unittest.TestCase):

    def test_get_grade_a(self):
        self.assertEqual(get_grade(95, 90, 93), "A", "get_grade(95, 90, 93)")

    def test_get_grade_b(self):
        self.assertEqual(get_grade(70, 70, 100), "B", "get_grade(70, 70, 100)")
    
    def test_get_grade_c(self):
        self.assertEqual(get_grade(70, 70, 70), "C", "get_grade(70, 70, 70)")

    def test_get_grade_d(self):
        self.assertEqual(get_grade(65, 70, 59), "D", "get_grade(65, 70, 59)")

    def test_get_grade_f(self):
        self.assertEqual(get_grade(44, 55, 52), "F", "get_grade(44, 55, 52)")
 

'''
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
'''

def smash(words):
    return ' '.join(words)


class TestSmash(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(smash([]), "")

    def test_word(self):
        self.assertEqual(smash(["hello"]), "hello")

    def test_multiple(self):
        self.assertEqual(smash(["hello", "world"]), "hello world")


'''
Simple, remove the spaces from the string, then return the resultant string.
'''

def no_space(x):
    return x.replace(' ', '')


class TestNoSpace(unittest.TestCase):

    def test_no_space(self):
        self.assertEqual(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')

'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
'''

def grow(arr):
    return math.prod(arr)


class TestGrow(unittest.TestCase):
    @parameterized.expand([
        [6 , [1, 2, 3]],
        [16, [4, 1, 1, 1, 4]],
        [64, [2, 2, 2, 2, 2, 2]],
    ])

    def test_grow(self, answer, array):
        self.assertEqual(grow(array), answer)


'''
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
'''

def other_angle(a, b):
    return 180 - (a+b)


class TestOtherAngle(unittest.TestCase):
    @parameterized.expand([
        [30, 60, 90],
        [60, 60, 60],
        [43, 78, 59],
    ])

    def test_other_angle(self, a, b, answer):
        self.assertEqual(other_angle(a, b), answer)


'''
The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.
'''

def cockroach_speed(s):
    return math.floor(s*27.7778)


class TestSpeed(unittest.TestCase):
    @parameterized.expand([
        [1.08,30],
        [1.09,30],
        [0,0],
    ])

    def test_cockroach_speed(self, a, answer):
        self.assertEqual(cockroach_speed(a), answer)


'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''

def row_sum_odd_numbers(n):
    return n**3


class TestRowSum(unittest.TestCase):
    @parameterized.expand([
        [1, 1],
        [2, 8],
        [13, 2197],
        [19, 6859],
        [41, 68921]
    ])

    def test_row_sum_odd_numbers(self, a, answer):
        self.assertEqual(row_sum_odd_numbers(a), answer)
