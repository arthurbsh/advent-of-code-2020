with open("input.txt") as f:
    entries = [
        line
        for line in f.readlines()
    ]

def part1(entries):
    max_id = 0

    for entry in entries:
        bp = entry
        bp = bp.replace("F", "0")
        bp = bp.replace("B", "1")
        bp = bp.replace("L", "0")
        bp = bp.replace("R", "1")
        id = int(bp, 2)

        if (id > max_id):
            max_id = id
    return max_id


def part2(entries):
    seats = list()

    for entry in entries:
        bp = entry
        bp = bp.replace("F", "0")
        bp = bp.replace("B", "1")
        bp = bp.replace("L", "0")
        bp = bp.replace("R", "1")
        seats.append(int(bp, 2))
    
    seats.sort()

    for i in range(len(seats)):
        if seats[i] + 1 != seats[i+1]:
            return seats[i] + 1



print("Day 5:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))