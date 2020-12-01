with open("input.txt") as f:
    entries = [
        int(line)
        for line in f.readlines()
    ]

def part1(entries):
    for entry in entries:
        if (2020 - entry in entries):
            return entry * (2020 - entry)


def part2(entries):
    for a in entries:
        for b in entries:
            for c in entries:
                if (a + b + c == 2020):
                    return a * b *c



print "Day 1:"
print "Part 1:",
print part1(entries)
print "Part 2:",
print part2(entries)