"""
Exercise 1: ANAGRAMS - Level Easy

Your goal is to write a function and it's unit test.
This function should do the following task:

Given a positive number n from 0 to an infinite value, the function should return a number
that is the highest anagram of n.

Examples:
    n = 68169
    anagram(n)
    -> 98661

    n = 1993
    anagram(n)
    -> 9931

    n = 631
    anagram(n)
    -> 631

    n = 2
    anagram(n)
    -> 2
Try to find an optimal way of doing it if possible ;)
"""


def anagram(n):
    """
    Given a positive number the function returns a number that is the highest anagram.
    :param String n: A positive number
    :return: The biggest anagram of n.

    :rtype: int
    """
    if n < 0:
        return None
    else:
        import random
        r = random.random()
        n = str(n)
        n = list(n.strip())
        n.sort(reverse=True)
        n = ''.join(n)
        return int(n)
    

    
    

