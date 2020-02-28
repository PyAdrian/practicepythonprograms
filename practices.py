# num = int(input("show the multiplication table of?"))
#
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)


# Python code to reverse a string
# using loop

# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
#
# s = "Geeksforgeeks"
#
# print ("The original string is : ",end="")
# print (s)
#
# print ("The reversed string(using loops) is : ",end="")
# print (reverse(s))
#
# import collections
# str1 = 'aabbccc'
# d = collections.defaultdict(int)
# for c in str1:
#     d[c] += 1
#
# for c in sorted(d, key=d.get, reverse=True):
#     if d[c] >= 1:
#         print('%d %s' % (d[c], c))

# anagrams

# s1=input("Enter first string:")
# s2=input("Enter second string:")
# if(sorted(s1)==sorted(s2)):
#     print("The strings are anagrams.")
# else:
#     print("The strings aren't anagrams.")

# prime and prime divisor

# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(num,"is not a prime number")
#             print(i,"times",num//i,"is",num)
#             break
#     else:
#         print(num,"is a prime number")
#
# else:
#     print(num,"is not a prime number")

# sum of the numbers in the string:


# inputstr = input("Enter your string: ")
# sum_total = 0
# for x in inputstr:
#     if x.isdigit():
#         sum_total += int(x)
#
#
# print("Total:- ", sum_total)

# Creating class and object:

# class Parrot:
#
#     # class attribute
#     species = "bird"
#
#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))
#
# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# Creating methods in python

# class Parrot:
#
#     # instance attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # instance method
#     def sing(self, song):
#         return "{} sings {}".format(self.name, song)
#
#     def dance(self):
#         return "{} is now dancing".format(self.name)
#
# # instantiate the object
# blu = Parrot("Blu", 10)
#
# # call our instance methods
# print(blu.sing("'Happy'"))
# print(blu.dance())

# # use of inheritsnce in python
#
# # parent class
# class Bird:
#
#     def __init__(self):
#         print("Bird is ready")
#
#     def whoisThis(self):
#         print("Bird")
#
#     def swim(self):
#         print("Swim faster")
#
# # child class
# class Penguin(Bird):
#
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
#
# # Encapsulation
#
# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()
#
# # change the price
# c.__maxprice = 1000
# c.sell()
#
# # using setter function
# c.setMaxPrice(1000)
# c.sell()
#
# # Using polymorphism
#
# class Parrot:
#
#     def fly(self):
#         print("Parrot can fly")
#
#     def swim(self):
#         print("Parrot can't swim")
#
# class Penguin:
#
#     def fly(self):
#         print("Penguin can't fly")
#
#     def swim(self):
#         print("Penguin can swim")
#
# # common interface
# def flying_test(bird):
#     bird.fly()
#
# #instantiate objects
# blu = Parrot()
# peggy = Penguin()
#
# # passing the object
# flying_test(blu)
# flying_test(peggy)

# # Permutation
#
# # A Python program to print all
# # permutations using library function
# from itertools import permutations
#
# # Get all permutations of [1, 2, 3]
# perm = permutations([1, 2, 3])
#
# # Print the obtained permutations
# for i in list(perm):
#     print (i)

# of given length with unsorted input.
# from itertools import combinations
#
# # Get all combinations of [2, 1, 3]
# # and length 2
# comb = combinations([2, 1, 3], 2)
#
# # Print the obtained combinations
# for i in list(comb):
#     print (i)
#
# Unique based on position
#
# A Python program to print all combinations
# of given length with duplicates in input
# from itertools import combinations
#
# # Get all combinations of [1, 1, 3]
# # and length 2
# comb = combinations([1, 1, 3], 2)
#
# # Print the obtained combinations
# for i in list(comb):
#     print (i)
#
# combinations of same element to same element
#
# A Python program to print all combinations
# with an element-to-itself combination is
# also included
# from itertools import combinations_with_replacement
#
# # Get all combinations of [1, 2, 3] and length 2
# comb = combinations_with_replacement([1, 2, 3], 2)
#
# With length L
#
# A Python program to print all
# permutations of given length
# from itertools import permutations
#
# # Get all permutations of length 2
# # and length 2
# perm = permutations([1, 2, 3], 2)
#
# # Print the obtained permutations
# for i in list(perm):
#     print (i)
#
# Lexographic sort order
#
# A Python program to print all combinations
# # Print the obtained combinations
# for i in list(comb):
#     print (i)

# vowels in a string

# string=input("Enter string:")
# vowels=0
# for i in string:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#         vowels=vowels+1
# print("Number of vowels are:")
# print(vowels)

# sort list based on second characters in the string
#
# # Initialising list
# ini_list = ["GeeksForGeeks abc", "manjeet xab", "akshat bac"]
#
# # printing initial list
# print ("initial list", str(ini_list))
#
# # code to sort list
# ini_list.sort(key = lambda x: x.split()[1])
#
# # printing result
# print ("result", str(ini_list))
#
# # using sorted
#
# # Initialising list
# ini_list = ["GeeksForGeeks abc", "manjeet xab", "akshat bac"]
#
# # printing initial list
# print ("initial list", str(ini_list))
#
# # code to sort list
# res = sorted(ini_list, key = lambda x: x.split()[1])
#
# # printing result
# print ("result", res)

# # seperate strings and integer from string into list
#
# # initializing string
# test_string = "There are 2 apples for 4 persons"
#
# # printing original string
# print("The original string : " + test_string)
#
# # using List comprehension + isdigit() +split()
# # getting numbers from string
# resdigit = [int(i) for i in test_string.split() if i.isdigit()]
# resstring = [str(i) for i in test_string.split() if i.isalpha()]
# # print result
# print("The numbers list is : " + str(resdigit))
# print("The string list is : "+str(resstring))



# # Paliandrome
# def reverse(s):
#     return s[::-1]
#
# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
#
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans == 1:
#     print("Yes")
# else:
#     print("No")
#
# def isPalindrome(str):
#
#     # Run loop from 0 to len/2
#     for i in range(0, round(len(str)/2)):
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
#
# # main function
# s = "mom"
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")


# pattern regex

# Python program to illustrate
# Matching regex objects
# import re
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# pythagoras theorem

# from math import sqrt
# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
#
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is", c )
#
#
# from math import sqrt
#
# print('Pythagorean theorem calculator! Calculate your triangle sides.')
# print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
# formula = input('Which side (a, b, c) do you wish to calculate? side> ')
#
# if formula == 'c':
#     side_a = int(input('Input the length of side a: '))
#     side_b = int(input('Input the length of side b: '))
#
#     side_c = sqrt(side_a * side_a + side_b * side_b)
#
#     print('The length of side c is: ' )
#     print(side_c)
#
# elif formula == 'a':
#     side_b = int(input('Input the length of side b: '))
#     side_c = int(input('Input the length of side c: '))
#
#     side_a = sqrt((side_c * side_c) - (side_b * side_b))
#
#     print('The length of side a is' )
#     print(side_a)
#
# elif formula == 'b':
#     side_a = int(input('Input the length of side a: '))
#     side_b = int(input('Input the length of side c: '))
#
#     side_c = sqrt(side_c * side_c - side_a * side_a)
#
#     print('The length of side b is')
#     print(side_c)
#
# else:
#     print('Please select a side between a, b, c')


# from datetime import datetime
#
# datetime_str = '09/19/18 13:55:26'
#
# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S').date()
#
# print(type(datetime_object))
# print(datetime_object)
#
#
# # time stamp to date
#
# from datetime import datetime
#
# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)
#
# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))


# import requests
#
# # Search GitHub's repositories for requests
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Inspect some attributes of the `requests` repository
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')  # Python 3.6+

# f = ['a','b','c','d']
#
# final = map(lambda x: x + str(1) ,f)
# print(list(final))

# s = 'cyqfjhcclkbxpbojgkar'
# from itertools import count
#
# def long_alphabet(input_string):
#     maxsubstr = input_string[0:0] # empty slice (to accept subclasses of str)
#     for start in range(len(input_string)): # O(n)
#         for end in count(start + len(maxsubstr) + 1): # O(m)
#             substr = input_string[start:end] # O(m)
#             if len(substr) != (end - start): # found duplicates or EOS
#                 break
#             if sorted(substr) == list(substr):
#                 maxsubstr = substr
#     return maxsubstr
#
# bla = (long_alphabet(s))
# print ("Longest substring in alphabetical order is: %s" %bla)

import re
s = '  Hello  World   From Pankaj \t\n\r\tHi There  '
print('Remove all spaces using RegEx:\n', re.sub(r"\s+", "", s), sep='')
