with open("input.txt") as f:
    lines = f.read().splitlines()
    earliest = int(lines[0])
    buses = lines[1].split(",")

def part1(earliest, buses):
    min_bus = int(buses[0])

    for bus in buses:
        if bus == "x":
            continue
        bus = int(bus)

        if -(earliest % bus) + bus < -(earliest % min_bus) + min_bus:
            min_bus = bus
        
    return min_bus * (-(earliest % min_bus) + min_bus)


def matches(schedule, timestamp):
    for b in schedule:
        if (timestamp + b[1]) % b[0] != 0:
            return False
    
    return True

def find(schedule, start, increment):
    timestamp = start + increment * 2

    while not matches(schedule, timestamp - increment):
        timestamp += increment    
    
    return timestamp - increment

def part2(buses):
    
    schedule = list()

    for i in range(len(buses)):
        if buses[i] != "x":
            schedule.append((int(buses[i]), i))

    inc_sch = [schedule[0]]

    start = 0
    inc =  inc_sch[0][0]

    for bus in schedule[1:-1]:
        inc_sch.append(bus)

        first = find(inc_sch, start, inc)
        second = find(inc_sch, first, inc)

        inc = second - first
        start = first + inc

    return find(schedule, start, inc)

print("Day 13:")
print("Part 1:"),
print(part1(earliest, buses))
print("Part 2:"),
print(part2(buses))