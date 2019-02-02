
import day01

def test_calculate_frequency():
    numbers = [+1, +1, +1]
    result = day01.calculateFrequency(numbers)
    assert result == 3

def test_first_reach_twice():
    numbers = [+1, -2, +3, +1]
    result = day01.firstReachTwice(numbers)
    assert result == 2
    
    numbers = [+1, -1]
    result = day01.firstReachTwice(numbers)
    assert result == 0

    numbers = [+3, +3, +4, -2, -4]
    result = day01.firstReachTwice(numbers)
    assert result == 10

    numbers = [-6, +3, +8, +5, -6]
    result = day01.firstReachTwice(numbers)
    assert result == 5

    numbers = [+7, +7, -2, -7, -4]
    result = day01.firstReachTwice(numbers)
    assert result == 14