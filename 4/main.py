with open("input.txt") as f:
    entries =  f.read().split("\n\n")

def part1(entries):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    invalid_count = 0

    for passport in entries:
        for field in req_fields:
            if field not in passport:
                invalid_count += 1
                break
    
    print invalid_count

    return len(entries) - invalid_count


def part1_2(entries):
    valid_count = 0

    for passport in entries:
        size = len(passport.split())
        if (size > 7):
            valid_count += 1
        elif (size == 7 and "cid" not in passport):
            valid_count += 1

    return valid_count

def valid_byr(value):
    if not len(value) == 4:
        return False

    value = int(value)

    return (1920 <= value <= 2002)

def valid_iyr(value):
    if not len(value) == 4:
        return False

    value = int(value)

    return (2010 <= value <= 2020)

def valid_eyr(value):
    if not len(value) == 4:
        return False

    value = int(value)

    return (2020 <= value <= 2030)

def valid_hgt(value):

    if value[-2::] == "cm":
        if len(value) == 5 and (150 <= int(value[0:3]) <= 193):
            return True
    elif value[-2::] == "in":
        if len(value) == 4 and (59 <= int(value[0:2]) <= 76):
            return True
    
    return False

def valid_hcl(value):
    if len(value) != 7:
        return False

    if value[0] != "#":
        return False
    
    for c in value[1:]:
        if not c in "0123456789abcdef":
            return False
    
    return True

def valid_ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def valid_pid(value):
    if len(value) != 9:
        return False
    for c in value:
        if not c in "0123456789":
            return False
            
    return True

def part2(entries):
    passports = list()

    for entry in entries:
        passport = dict()
        for field in entry.split():
            key = field.split(":")[0] 
            value = field.split(":")[1]
            passport[key] = value
        
        passports.append(passport)

    valid_count = 0
    for passport in passports:
        
        if len(passport) == 7 and "cid" in passport:
            continue
        elif len(passport) < 7:
            continue

        valid = True
        for field in passport:
            value = passport[field]
            
            if field == "byr":
                if not valid_byr(value):
                    valid = False
                    break

            elif field == "iyr":
                if not valid_iyr(value):
                    valid = False
                    break
            elif field == "eyr":
                if not valid_eyr(value):
                    valid = False
                    break
            elif field == "hgt":
                if not valid_hgt(value):
                    valid = False
                    break
            elif field == "hcl":
                if not valid_hcl(value):
                    valid = False
                    break
            elif field == "ecl":
                if not valid_ecl(value):
                    valid = False
                    break
            elif field == "pid":
                if not valid_pid(value):
                    valid = False
                    break
        if valid:
            valid_count += 1


    return valid_count
        

print "Day 4:"
print "Part 1:",
print part1_2(entries)
print "Part 2:",
print part2(entries)