#!/usr/bin/env python3
import re
from collections import Counter

def reactionExplodes(element1, element2):
    if(element1 == element2 or element1.upper() != element2.upper()):
        return False
    else:
        return True

def react(input):
    i = 0
    while i < len(input)-1:
        explodes = reactionExplodes(input[i], input[i+1])
        if(explodes):
            remove = input[i] + input[i+1]
            input = input.replace(remove, '')
            if(i > 0) : i -= 1
        else:
            i += 1

    return input

def get_length_reaction(input, pattern):
    output = re.sub(pattern, '', input)
    output = react(output)
    #print(output)
    return len(output)

def get_shortest_polymer(input):
    reactions = list()
    characters = (set(list(input.upper())))
    for c in characters:
        pattern = '[{}{}]'.format(c.lower(), c.upper())
        result = get_length_reaction(input, pattern)
        reactions.append(result)
    
    return min(reactions)


with open('input.txt', 'r') as f:
    for line in f:
        input = line.strip()

#Part 1
result1 = react(input)
print(len(result1))

#Part 2
shortest_polymer = get_shortest_polymer(input)
print(shortest_polymer)