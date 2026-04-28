# Problem: Reverse an Array
# Platform: HackerRank
# Topic: Arrays

# Description:
# Given an array of integers, reverse the array and print the result.

def reversearray(a):
    return a[::-1]
n=int(input())
arr = list(map(int,input().split()))
result= reversearray(arr)
print(*result)
 
