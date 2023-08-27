"""
Capital indexes

Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
From: https://pythonprinciples.com/challenges/Capital-indexes/
"""

"""
Func: capital_indexes
Input: string
Output: List
Desc: Provides a list of positions of each capital letter located in the string.
"""
def capital_indexes(word):
    caps = []
    y = 0
    for x in word:
        #check only for values between 'A' to 'Z'.
        if ord(x) >= 65 and ord(x) <= 90:
            caps.append(y)
        y += 1
    return caps
positions = capital_indexes("HiLLo- '/.,ThERE")
print (positions)