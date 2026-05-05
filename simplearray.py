# Problem: Sum of Array Elements
# Platform: HackerRank
# Topic: Arrays
# Description:
# Given an array of integers, find and print the sum of all elements.
# Input:
# First line contains an integer n (size of array)
# Second line contains n space-separated integers

# Output:
# Print the sum of the array elements
# Example:
# Input:
# 6
# 1 2 3 4 10 11
# Output:
# 31
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
