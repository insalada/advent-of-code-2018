#!/usr/bin/env python3

def calculateFrequency(numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result

def firstReachTwice(changes):
    frequency = 0
    used = set([0])
    while(True):
        for c in changes:
            frequency += c            
            if frequency in used:
                return frequency
            else:
                used.add(frequency)
    
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        changes = [int(line.strip()) for line in f]
    #Part 1
    print(calculateFrequency(changes))
    #Part 2
    print(firstReachTwice(changes))