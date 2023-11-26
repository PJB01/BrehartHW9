# sumLines.py
# Created by Phil Brehart, calculates the sum, average and total number of elements
# Invocation: python3 sumLines.py dataInput.txt

import sys

# Initialize global variables
global sumTotal, numElements, average

def calcValues(element):
    global sumTotal
    global numElements
    sumTotal += element
    numElements += 1

    # Open, read, and split file to get each element
    with open(sys.argv[1], 'r') as file:
        # Iterate through each element
        for element in file.read().split():
            # Cast to int and call function recursively
            calcValues(int(element))


# Calculate average
if numElements > 0:
    average = sumTotal / numElements
else:
    average = 0


# Print results
print(f"Sum = {sumTotal}, Number of Elements = {numElements}, and Average = {average}")
