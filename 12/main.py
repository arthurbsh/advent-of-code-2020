import time

with open("input.txt") as f:
    entries = [
        line
        for line in f.read().splitlines()
    ]

def part1(entries):
    d_x = 0
    d_y = 0
    direction = 0


    for action in entries:
        move = action[0]
        value = int(action[1:])

        if move == "L":
            direction = (direction + value) % 360
        elif move == "R":
            direction = (direction - value) % 360
        elif move == "F":
            if direction == 0:
                d_x += value
            elif direction == 90:
                d_y += value
            elif direction == 180:
                d_x -= value
            elif direction == 270:
                d_y -= value
        elif move == "N":
            d_y += value
        elif move == "S":
            d_y -= value
        elif move == "E":
            d_x += value
        elif move == "W":
            d_x -= value

    return abs(d_x) +  abs(d_y)

def rotate_waypoint(w_x, w_y, degrees):
    
    degrees = degrees % 360

    if degrees == 0:
        return w_x, w_y
    elif degrees == 90:
        return -w_y, w_x
    elif degrees == 180:
        return -w_x, -w_y
    elif degrees == 270:
        return w_y, -w_x    

def part2(entries):
    d_x = 0
    d_y = 0
    w_x = 10
    w_y = 1

    for action in entries:
        move = action[0]
        value = int(action[1:])

        if move == "L":
           w_x, w_y = rotate_waypoint(w_x, w_y, value)
        elif move == "R":
            w_x, w_y = rotate_waypoint(w_x, w_y, -value)
        elif move == "F":
            d_x += w_x * value
            d_y += w_y * value
        elif move == "N":
            w_y += value
        elif move == "S":
            w_y -= value
        elif move == "E":
            w_x += value
        elif move == "W":
            w_x -= value

    return abs(d_x) +  abs(d_y)
    #return d_x,  d_y

    
print("Day 12:")
print("Part 1:"),
print(part1(entries))
print("Part 2:"),
print(part2(entries))