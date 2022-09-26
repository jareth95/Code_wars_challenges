from parameterized import parameterized
import unittest
import math


'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def square_digits(num):
    return int(''.join(str(int(digit)**2) for digit in str(num)))


class TestSquareDigits(unittest.TestCase):
    @parameterized.expand([
        [9119, 811181],
        [0, 0],
    ])
    
    def test_square_digits(self, num, answer):
        self.assertEqual(square_digits(num), answer)


'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.
'''

def are_you_playing_banjo(name):
    return f'{name} plays banjo' if name[0].upper() == 'R' else f'{name} does not play banjo'


class TestPlayingBingo(unittest.TestCase):
    @parameterized.expand([
        ["martin", 'martin does not play banjo'],
        ["Rikke", 'Rikke plays banjo'],
        ["rolf", 'rolf plays banjo']
    ])
    
    def test_filter_list(self, name, answer):
        self.assertEqual(are_you_playing_banjo(name), answer)


'''
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


class TestDisemvowel(unittest.TestCase):
    
    def test_disemvowel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")


'''
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
'''

def filter_list(l):
    return [number for number in l if type(number) is int]


class TestFilterList(unittest.TestCase):
    @parameterized.expand([
        [[1, 2, 'a', 'b'], [1, 2]],
        [[1, 'a', 'b', 0, 15], [1, 0, 15]],
        [[1, 2, 'aasf', '1', '123', 123], [1, 2, 123]]
    ])
    
    def test_filter_list(self, l, answer):
        self.assertEqual(filter_list(l), answer)


'''
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
    return 'Even' if number%2 == 0 else 'Odd'


class TestEvenOrOdd(unittest.TestCase):
    @parameterized.expand([
        [2, 'Even'],
        [1, 'Odd'],
        [0, 'Even']
    ])
    
    def test_even_or_odd(self, number, answer):
        self.assertEqual(even_or_odd(number), answer)


'''
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
'''

def make_negative( number ):
    return -abs(number)


class TestMakeNegative(unittest.TestCase):
    @parameterized.expand([
        [42, -42],
        [9, -9],
        [0, 0]
    ])
    
    def test_make_negative(self, string, answer):
        self.assertEqual(make_negative(string), answer)

'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
'''

def is_isogram(string):
    return len(string) == len(set(string.lower()))


class TestIsIsogram(unittest.TestCase):
    @parameterized.expand([
        ["Dermatoglyphics", True],
        ["isogram", True],
        ["aba", False],
        ["moOse", False],
        ["", True]
    ])
    
    def test_is_isogram(self, string, answer):
        self.assertEqual(is_isogram(string), answer)

'''
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

"1234" --> 1234
"605"  --> 605
"1405" --> 1405

'''

def string_to_number(s):
    return int(s)


class TestStringToNumber(unittest.TestCase):
    @parameterized.expand([
        ["1234", 1234],
        ["605", 605],
        ["-7", -7]
    ])
    
    def test_string_to_number(self, numbers, answer):
        self.assertEqual(string_to_number(numbers), answer)


'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


class TestSumTwoSmallest(unittest.TestCase):
    @parameterized.expand([
        [[5, 8, 12, 18, 22], 13],
        [[7, 15, 12, 18, 22], 19],
        [[25, 42, 12, 18, 22], 30]
    ])
    
    def test_sum_two_smallest_numbers(self, numbers, answer):
        self.assertEqual(sum_two_smallest_numbers(numbers), answer)


'''
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.
'''

def open_or_senior(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]


class TestOpenSenior(unittest.TestCase):
    @parameterized.expand([
        [[(45, 12),(55,21),(19, -2),(104, 20)], ['Open', 'Senior', 'Open', 'Senior']],
        [[(16, 23),(73,1),(56, 20),(1, -1)], ['Open', 'Open', 'Senior', 'Open']],
    ])
    
    def test_open_or_senior(self, data, answer):
        self.assertEqual(open_or_senior(data), answer)


'''
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).
'''

def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


class TestValidWalk(unittest.TestCase):
    @parameterized.expand([
        [['n','s','n','s','n','s','n','s','n','s'], True],
        [['w','e','w','e','w','e','w','e','w','e','w','e'], False],
        [['w'], False],
        [['n','n','n','s','n','s','n','s','n','s'], False]
    ])
    
    def test_is_valid_walk(self, walk, answer):
        self.assertEqual(isValidWalk(walk), answer)


'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(s):
    for char in 'abcdefghijklmnopqrstuvwxyz':
        return False if char not in s.lower() else True


class TestIsPangram(unittest.TestCase):
    @parameterized.expand([
        ["The quick, brown fox jumps over the lazy dog!", True],
        ["1bcdefghijklmnopqrstuvwxyz", False]
    ])

    def test_is_pangram(self, s, bool):
        self.assertEqual(is_pangram(s), bool)


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
