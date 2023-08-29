"""
    Online status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.

Challenge From: https://pythonprinciples.com/challenges/Online-status/
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

"""
Func: online_count
Input: Dictionary
Output: Int
Desc: Returns count of online users based on "online" status
"""
def online_count(dict):
    count = 0
    for x in dict.values():
        if x == "online":
            count += 1
    return count

"""
Func: online_count
Input: Dictionary
Output: List
Desc: Returns list of online users names based on "online" status
"""
def online_users(dict):
    userlist = []
    count = 0
    for x in dict:
       if dict[x] == "online":
        userlist.append(x)
    
    if len(userlist) == 0:
        userlist.append("No users online") 
    return userlist

x = online_count(statuses)
print ("Friends online: ", x)
onlist = online_users(statuses)
print(onlist)
