with open("input.txt") as f:
    entries =  f.read().splitlines()

def check_entry_old_policy(entry):
    rule = entry.replace(":","").replace("-"," ").split(" ")

    at_least = int(rule[0])
    at_most = int(rule[1])   
    letter = rule[2]
    password = rule[3]

    count = password.count(letter)

    return at_least <= count <= at_most

def check_entry_new_policy(entry):
    rule = entry.replace(":","").replace("-"," ").split(" ")

    position_yes = int(rule[0]) - 1 
    position_no = int(rule[1]) - 1 
    letter = rule[2]
    password = rule[3]

    return (password[position_yes] == letter) ^ (password[position_no] == letter)

def part1(entries):
    correct_count = 0

    for entry in entries:
        if (check_entry_old_policy(entry)):
            correct_count += 1

    return correct_count

def part2(entries):
    correct_count = 0

    for entry in entries:
        if (check_entry_new_policy(entry)):
            correct_count += 1

    return correct_count

print "Day 2:"
print "Part 1:",
print part1(entries)
print "Part 2:",
print part2(entries)