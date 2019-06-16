import pytest
import day05

def test_same_case_doesnt_explode():
    element1 = 'A'
    element2 = 'A'
    actual = day05.reactionExplodes(element1, element2)
    assert actual == False

def test_same_diferent_case_explode():
    element1 = 'a'
    element2 = 'A'
    actual = day05.reactionExplodes(element1, element2)
    assert actual == True

def test_diferent_doesnt_explode():
    element1 = 'a'
    element2 = 'b'
    actual = day05.reactionExplodes(element1, element2)
    assert actual == False

def test_react_input():
    input = 'dabAcCaCBAcCcaDA'
    actual = day05.react(input)
    assert actual == 'dabCBAcaDA'

def test_shortest_polymer():
    input = 'dabAcCaCBAcCcaDA'
    actual = day05.get_shortest_polymer(input)
    assert actual == 4