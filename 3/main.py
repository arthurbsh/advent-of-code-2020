with open("input.txt") as f:
    entries =  f.read().splitlines()

def part1(entries):
    x = 0
    trees = 0

    for row in entries:
        if row[x % len(row)] == "#":
            trees += 1
        x += 3

    return trees

def part2(entries):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    total = 1

    for slope in slopes:
        x = 0
        trees = 0

        for i in range(0, len(entries), slope[1]):
            row = entries[i]
            if row[x % len(row)] == "#":
                trees += 1
            x += slope[0]
        
        total *= trees

    return total
        

print "Day 3:"
print "Part 1:",
print part1(entries)
print "Part 2:",
print part2(entries)