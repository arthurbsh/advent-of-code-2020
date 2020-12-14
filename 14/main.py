with open("input.txt") as f:
    entries = [
        line
        for line in f.read().splitlines()
    ]

def apply_mask_value(value, mask):
    binary = "{0:b}".format(value)

    binary = "0"*(36-len(binary)) + binary

    binary = list(binary)

    for i in range(36):
        if mask[i] != "X":
            binary[i] = mask[i]

    return int("".join(binary), 2)

def part1(entries):
    memory = {}

    for entry in entries:
        if "mask" in entry:
            mask = entry[7:]
        else:
            value = int(entry.split(" = ")[1])
            mem_space = int(entry.split(" = ")[0][4:-1])
            memory[mem_space] = apply_mask_value(value, mask)

    return sum(memory.values())

def apply_mask_mem(value, mask):
    binary = "{0:b}".format(value)
    binary = "0"*(36-len(binary)) + binary
    binary = list(binary)

    floating = []

    for i in range(36):
        index = -i - 1
        if mask[index] == "1":
            binary[index] = "1"
        elif mask[index] == "X":
            binary[index] = "0"
            floating.append(i)

    mems = [int("".join(binary), 2)]
    
    for p in floating:
        for i in range(len(mems)):
            power = 2 ** p
            mems.append(mems[i] + power)

    return mems
    

def part2(entries):
    memory = {}

    for entry in entries:
        if "mask" in entry:
            mask = entry[7:]
        else:
            value = int(entry.split(" = ")[1])
            mem_space = int(entry.split(" = ")[0][4:-1])
            mem_range = apply_mask_mem(mem_space, mask)

            for mem in mem_range:
                memory[mem] = value

    return sum(memory.values())

print("Day 14:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))
