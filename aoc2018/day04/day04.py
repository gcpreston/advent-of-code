import re


def main():
    p = re.compile(r'\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)] (.+)')
    with open('input.txt') as file:
        data = []
        for line in file.readlines():
            m = re.match(p, line.strip())
            data.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5)))
    data = sorted(data, key=lambda x: (x[0], x[1], x[2], x[3]))

    sleep = dict()
    p = re.compile('Guard #(\d+) begins shift')

    # default values will not be used, simply to avoid warnings
    interval = []
    latest = 0
    for d in data:
        m = re.match(p, d[4])

        if m:
            n = int(m.group(1))
            if n not in sleep:
                sleep[n] = []
            latest = n
        elif d[4] == 'falls asleep':
            interval = [d[3]]
        else:
            # organization of sorted data ensures interval and latest have been defined
            interval.append(d[3])
            sleep[latest].append(tuple(interval))

    print('Part 1:', part1(sleep))
    print('Part 2:', part2(sleep))


def part1(sleep):
    guard = max(sleep, key=lambda x: minutes_asleep(sleep[x]))
    minutes = minute_counts((sleep[guard]))
    return guard * max(minutes, key=minutes.get)


def minutes_asleep(intervals):
    return sum([i[1] - i[0] for i in intervals])


def minute_counts(intervals):
    minutes = dict()

    for i in intervals:
        for m in range(i[0], i[1]):

            if m not in minutes:
                minutes[m] = 1
            else:
                minutes[m] += 1

    return minutes


def part2(sleep):
    minutes = dict()

    for guard in sleep:
        minutes[guard] = minute_counts(sleep[guard])

    max_minutes = dict()
    for guard in minutes:
        if minutes[guard]:
            m = max(minutes[guard], key=minutes[guard].get)
            max_minutes[guard] = (m, minutes[guard][m])

    max_guard = max(max_minutes, key=lambda x: max_minutes[x][1])
    return max_guard * max_minutes[max_guard][0]


if __name__ == '__main__':
    main()
