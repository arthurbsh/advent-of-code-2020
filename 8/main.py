from collections import Counter

with open("input.txt") as f:
    entries = [
        line
        for line in f.read().splitlines()
    ]


def part1(entries):
    visited_instructions = list()
    global_var = 0
    pointer = 0 

    while True:
        if pointer in visited_instructions:
            return global_var
        visited_instructions.append(pointer)

        instruction = entries[pointer].split(" ")[0]
        argument = int(entries[pointer].split(" ")[1])

        if instruction == "acc":
            global_var += argument
        elif instruction == "jmp":
            pointer += argument
            continue

        pointer += 1

    return global_var

def part2(entries):
    
    
    looping = True
    fixed_instruction = 0

    while looping:
        looping = False
        visited_instructions = list()
        global_var = 0
        pointer = 0
        

        while True:
            if pointer in visited_instructions:
                looping = True
                break
            elif pointer >= len(entries):
                return global_var

            visited_instructions.append(pointer)

            instruction = entries[pointer].split(" ")[0]
            argument = int(entries[pointer].split(" ")[1])

            if fixed_instruction == pointer:
                if instruction == "jmp":
                    instruction = "nop"
                elif instruction == "nop":
                    instruction == "jmp"

            if instruction == "acc":
                global_var += argument
            elif instruction == "jmp":
                pointer += argument
                continue

            pointer += 1
        
        fixed_instruction += 1

    return global_var

print("Day 8:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))