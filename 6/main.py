from collections import Counter

with open("input.txt") as f:
    entries = [
        line
        for line in f.read().split("\n\n")
    ]

def part1(entries):
    count = 0
    for entry in entries:
        count += len(Counter(entry.replace("\n", "")).keys())

    return count

def part2(entries):
    count = 0

    for entry in entries:
        answers = entry.splitlines()
        
        yesses = set(answers[0])

        for answer in answers:
            yesses = yesses.intersection(answer)

        count += len(yesses)
    
    return count

print("Day 6:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))