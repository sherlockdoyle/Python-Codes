# Distinct Alphabets Problem Description
# We are all familiar with alpha numeric keypad that was used for messaging in earlier days. Given sequence of numbers 2-9 (both inclusive), find out the number of distinct alphabets that can be formed.
# The rules of interpreting keypad strokes are as follows
# 1) Let's understand with example. 25 can mean AJ but it can also mean pressing button 5 two times. In that case it becomes K. See Examples section for better understanding.
# 2) Maximum number of distinct alphabets that can be formed cannot exceed 26
# 3) Alphanumeric keyboard used is as follows
# · key 2 has letters "A B C"
# · key 3 has letters "D E F"
# · key 4 has letters "G H I"
# · key 5 has letters "J K L"
# · key 6 has letters "M N O"
# · key 7 has letters "P Q R S"
# · key 8 has letters "T U V"
# · key 9 has letters "W X Y Z"
# 4) Input does not contain either 1 or 0 because no keypad buttons are associated with these numbers.
# Constraints
# 1 <= Length of Input Literals <= 40
# Input Format
# Single Line contains a number with literals [2-9]
# Output
# Number of distinct alphabets after factoring all possible interpretations of the input
#
# Explanation Example 1
# Input
# 253
# Output
# 5
# Explanation
# It can be interpreted as AJD, KD , AE,  thus distinct alphabets formed- A , J , D ,K , E = 5 distinct alphabets. Example 2
# Input
# 294
# Output
# 5

# Assumes, multiple key-presses doesn't contain the number itself. ie. 94 is I(GHIGHIGHI), not G(GHI4GHI4G)

num = [int(c) for c in input("Enter the literals: ")]  # get the input

alphbt = [0] * 26  # to store if an alphabet is pressed
n2a = [0, 0, [0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17, 18], [19, 20, 21], [22, 23, 24, 25]]  # alphanumeric keymap

for i in range(len(num) - 1):  # iterate all but the last number
    alphbt[n2a[num[i]][0]] = 1  # check if it itself is pressed
    alphbt[n2a[num[i + 1]][(num[i] - 1) % len(n2a[num[i + 1]])]] = 1  # if the next key is pressed this many times
alphbt[n2a[num[-1]][0]] = 1  # check the last number

# count and print the number of alphabets
print(alphbt.count(1))
