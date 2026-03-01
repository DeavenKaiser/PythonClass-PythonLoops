# --------------------------------------------
# Name:
# Date:
# Program: Chapter 4 Practice
# Description:
# Complete each section by following the
# directions in the comments.
# --------------------------------------------


# ------------------------------------------------
# Practice 1: Basic while Loop
# ------------------------------------------------
# TODO:
# 1. Create a variable named count and set it to 1
# 2. Use a while loop to print numbers 1 through 5
# 3. Increase count by 1 each iteration
# 4. Make sure the loop stops properly

print()  # blank line


# ------------------------------------------------
# Practice 2: Basic for Loop
# ------------------------------------------------
# TODO:
# 1. Use a for loop with range()
# 2. Print numbers 1 through 5
# 3. Then print numbers 5 down to 1

print()


# ------------------------------------------------
# Practice 3: Running Total
# ------------------------------------------------
# TODO:
# 1. Create a variable named total and set it to 0
# 2. Use a for loop that runs 3 times
# 3. Ask the user to enter a number each time
# 4. Add each number to total
# 5. Print the final total

print()


# ------------------------------------------------
# Practice 4: Sentinel Loop
# ------------------------------------------------
# TODO:
# 1. Create a variable named total and set it to 0
# 2. Ask the user to enter a number
# 3. Continue asking for numbers until the user enters 0
# 4. Add each number to total (except 0)
# 5. When finished, print the total

print()


# ------------------------------------------------
# Practice 5: Debug the Loop
# ------------------------------------------------
# TODO:
# The program below is supposed to:
# - Ask the user for 3 numbers
# - Add them together
# - Print the total
#
# There are 3 errors in this code.
# Fix them so the program works correctly.


total = 0

for i in range(1, 3):
    number = input("Enter a number: ")
    total += number

print("Total:", total)
