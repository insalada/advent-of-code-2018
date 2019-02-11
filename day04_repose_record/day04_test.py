import pytest
import day04

input = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split("\n")


@pytest.fixture
def guards():
    events = [day04.parse(line.strip()) for line in input]
    return day04.getGuards(events)


def test_solution1(guards):
    guard_sleep_max = day04.getGuardSleptMost(guards)
    assert guard_sleep_max.id == '10'

    minute_guard_slept_most = day04.getMinuteSleptMost(guard_sleep_max)
    assert minute_guard_slept_most == 24


def test_solution2(guards):
    sleepyGuard, minute = day04.getMostFrequenlyAsleepGuard(guards)
    assert sleepyGuard == '99'
    assert minute == '45'
