#!/usr/bin/env python3
import re


class Claim:
    def __init__(self, id, x, y, wide, tall):
        self.id = id
        self.x = x
        self.y = y
        self.wide = wide
        self.tall = tall
        self.squares = 0


def parse(line):
    parsed = re.split(' @ |,|: |x', line)
    claim = Claim(parsed[0], int(parsed[1]), int(
        parsed[2]), int(parsed[3]), int(parsed[4]))
    return claim


def putClaim(claim, matrix):
    '''Fills a given matrix with provided claim. Returns total square inches'''
    squares = 0
    for x in range(claim.wide):
        for y in range(claim.tall):
            squares += 1
            point = (claim.x + x, claim.y + y)
            if point in matrix:
                matrix[point] = 'X'
            else:
                matrix[point] = claim.id
    return squares


def findOverlapsed(matrix):
    '''Finds square inches overlapsing'''
    return sum(v == 'X' for v in matrix.values())


def findIntact(claim, matrix):
    '''Finds the amount of squares intact in the given claim and matrix'''
    return sum(v == claim.id for v in matrix.values())


if __name__ == "__main__":
    # Read and parse claims
    with open("input.txt", "r") as f:
        claims = [parse(line.strip()) for line in f]
    # Fill the general matrix
    matrix = {}
    for claim in claims:
        squares = putClaim(claim, matrix)
        claim.squares = squares

    # PART1: Find squares overlapsing
    overlapsed = findOverlapsed(matrix)
    print("{} overlapsed".format(overlapsed))

    # PART2: Find intact claims
    for claim in claims:
        intact = findIntact(claim, matrix)
        if intact == claim.squares:
            print("{} is intact".format(claim.id))
