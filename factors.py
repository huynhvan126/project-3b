# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/17/2024
# Description: only enter positive integers and divide them evenly
integer = int(input(f"Please enter a positive integer: "))
factors = []
for i in range(1, int(integer**0.5) + 1):
    if integer % i == 0:
        factors.append(i)
        if i != integer // i:
            factors.append(integer // i)
    factors.sort()
print(f"The factors of {integer} are: ")
for factor in factors:
    print(factor)
