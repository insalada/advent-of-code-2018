#!/usr/bin/env python3
import re
from collections import Counter
from datetime import datetime, timedelta


class Guard:
    def __init__(self, id):
        self.id = id
        self.turns = {}
        self.totalminutes = float(0)

    def __str__(self):
        return "Guard #{} totalminutes {}...".format(self.id, self.totalminutes)

    def __repr__(self):
        return "\nGuard #{} totalminutes: {}".format(self.id, self.totalminutes)


class Turn:
    def __init__(self, id):
        self.id = id
        self.periods = []
        self.totalminutes = 0

    def __str__(self):
        return "Turn #{} Periods {}".format(self.id, self.periods)

    def __repr__(self):
        return "\n\t*Turn #{} Minutes {}*".format(self.id, self.totalminutes)


class Period:
    def __init__(self, start, end, totalminutes):
        self.start = start
        self.end = end
        self.totalminutes = totalminutes

    def __str__(self):
        return "{} - {}".format(self.start, self.end)

    def __repr__(self):
        return "{} - {}".format(self.start, self.end)


def parse(line):
    regex = r"\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})] (.*)"
    time, text = re.match(regex, line).groups()
    minute = datetime.strptime(time, '%Y-%m-%d %H:%M')
    event = (minute, text)
    return event


def getMinuteSleptMost(guard: Guard):
    minutes = Counter()
    for k, turn in guard.turns.items():
        for period in turn.periods:
            for minute in range(period.start.minute, period.end.minute):
                minutes[minute] += 1

    return minutes.most_common(1)[0][0]


def getTotalMinutes(guard: Guard):
    totalminutes = 0
    for k, v in guard.turns.items():
        totalminutes += v.totalminutes

    return totalminutes


def getGuards(events):
    guards = {}
    turn_id = 0
    for event in sorted(events):
        time = event[0]
        fact = event[1]
        extract = re.search('Guard #(.*) begins shift', fact)
        if(extract):
            # Starts a turn
            turn_id += 1
            id = extract.group(1)
        elif "asleep" in fact:
            # Falls sleep
            asleep_time = time
        else:
            # Wakes up
            minutes_sleeping_period = (time-asleep_time).total_seconds()/60
            period_asleep = Period(asleep_time, time, minutes_sleeping_period)
            guard = guards.get(id, Guard(id))
            turn = guard.turns.get(turn_id, Turn(turn_id))
            turn.periods.append(period_asleep)
            turn.totalminutes += minutes_sleeping_period
            guard.turns[turn_id] = turn
            guard.totalminutes = getTotalMinutes(guard)
            guards[id] = guard

    return guards


def getGuardSleptMost(guards):
    return max(guards.items(), key=lambda g: getTotalMinutes(g[1]))[1]


def getMostFrequenlyAsleepGuard(guards):
    minutes = Counter()
    for k, guard in guards.items():
        for k, turn in guard.turns.items():
            for period in turn.periods:
                for minute in range(period.start.minute, period.end.minute):
                    id = str(guard.id) + "#" + str(minute)
                    minutes[id] += 1

    sleepyGuardMinute = minutes.most_common(1)[0][0]
    return re.split("#", sleepyGuardMinute)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        events = [parse(line.strip()) for line in f]

    # Part 1
    guards = getGuards(events)
    guard_sleep_max = getGuardSleptMost(guards)
    print("Guard slept the most {}".format(guard_sleep_max))
    minute_guard_slept_most = getMinuteSleptMost(guard_sleep_max)
    print("Minute the guard slept the most: {}".format(minute_guard_slept_most))
    solution1 = int(guard_sleep_max.id) * minute_guard_slept_most
    print("Solution1: {}".format(solution1))

    # Part 2
    sleepyGuard, minute = getMostFrequenlyAsleepGuard(guards)
    print("Most sleepy guard {} at minute {}".format(sleepyGuard, minute))
    solution2 = int(sleepyGuard) * int(minute)
    print("Solution2: {}".format(solution2))