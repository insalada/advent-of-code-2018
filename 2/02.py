#!/usr/bin/env python3

#Part 1: Find checksum
def countLetters(box):
    counter = {}
    for letter in box:
        counter[letter] = counter.get(letter,0) + 1
    return counter

def sortByValue(dict):
    sortedDict = {}
    for s in sorted(dict, key=dict.get, reverse=True):
        sortedDict[s] = dict[s]
    return sortedDict

two = 0
three = 0
with open("input.txt") as input:
    for i in input:
        letters = countLetters(i)
        if 2 in letters.values() : two += 1
        if 3 in letters.values() : three += 1

checksum = three * two
print ("checksum is {}".format(checksum))

#Part 2: Find prototype
def compareBoxes(box1, box2):
    result = ""
    for pos in range(0, length):
        if box1[pos] == box2[pos]:
            result += box1[pos]
    return result

boxes = [line.rstrip('\n') for line in open('input.txt')]
prototypes = []
for box1 in boxes:
    length = len(box1)
    for box2 in boxes:
        if box1 != box2:
            result = compareBoxes(box1, box2)
            if len(result) >= length-1 and result not in prototypes:
                prototypes.append(result)

print("Prototypes found: {}".format(prototypes))
