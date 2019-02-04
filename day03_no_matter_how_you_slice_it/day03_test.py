import pytest
import day03


@pytest.fixture
def claim1():
    return day03.Claim('#1', 1, 3, 4, 4)


@pytest.fixture
def claim2():
    return day03.Claim('#2', 3, 1, 4, 4)


@pytest.fixture
def claim3():
    return day03.Claim('#3', 5, 5, 2, 2)


def test_putClaim_empty_matrix(claim1):
    matrix = {}
    squares = day03.putClaim(claim1, matrix)
    assert squares == 16
    assert len(matrix) == 16
    assert matrix == {(1, 3): '#1', (1, 4): '#1', (1, 5): '#1', (1, 6): '#1', (2, 3): '#1', (2, 4): '#1', (2, 5): '#1', (2, 6)                      : '#1', (3, 3): '#1', (3, 4): '#1', (3, 5): '#1', (3, 6): '#1', (4, 3): '#1', (4, 4): '#1', (4, 5): '#1', (4, 6): '#1'}


def find_overlapsed_empty():
    matrix = {}
    overlapsed = day03.findOverlapsed(matrix)
    assert overlapsed == 0


def test_overlapsed_all(claim1):
    matrix = {}
    day03.putClaim(claim1, matrix)
    day03.putClaim(claim1, matrix)
    overlapsed = day03.findOverlapsed(matrix)
    assert overlapsed == 16


def test_overlapsed_none(claim1):
    matrix = {}
    day03.putClaim(claim1, matrix)
    overlapsed = day03.findOverlapsed(matrix)
    assert overlapsed == 0


def test_overlapsed_some(claim1, claim2):
    matrix = {}
    day03.putClaim(claim1, matrix)
    day03.putClaim(claim2, matrix)
    overlapsed = day03.findOverlapsed(matrix)
    assert overlapsed == 4


def test_all_intact(claim1):
    matrix = {}
    day03.putClaim(claim1, matrix)
    intact = day03.findIntact(claim1, matrix)
    assert intact == 16


def test_none_intact(claim1):
    matrix = {}
    day03.putClaim(claim1, matrix)
    day03.putClaim(claim1, matrix)
    intact = day03.findIntact(claim1, matrix)
    assert intact == 0
