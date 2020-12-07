from collections import Counter

with open("input.txt") as f:
    entries = [
        line
        for line in f.read().splitlines()
    ]

def qtt_inside(bag, rules):

    if not rules[bag]:
        return 0
    
    total = 0

    for content in rules[bag]:
        total += content[0] + (content[0] * qtt_inside(content[1], rules))


    return total

def part1(entries):
    rules = dict()

    for entry in entries:
        container = entry.split(" bags contain ")[0]
        contents = entry.split(" bags contain ")[1].split(", ")
        rules[container] = list()

        for c in contents:
            rules[container].append((" ".join(c.split(" ")[1:3])))
    
    good_containers = set()

    good_containers.add("shiny gold")

    new_found = True
    while (new_found):
        new_found = False
        for container in rules:
            for color in rules[container]:
                if color in good_containers and not container in good_containers:
                    good_containers.add(container)
                    new_found = True

    good_containers.remove("shiny gold")
    
    return len(good_containers)

def part2(entries):
    rules = dict()

    for entry in entries:
        container = entry.split(" bags contain ")[0]
        contents = entry.split(" bags contain ")[1].split(", ")
        rules[container] = list()

        for c in contents:
            if c.split(" ")[0] == "no":
                continue

            rules[container].append((int(c.split(" ")[0]), " ".join(c.split(" ")[1:3])))

    
    return qtt_inside("shiny gold", rules)

print("Day 7:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))