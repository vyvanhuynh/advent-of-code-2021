# day 2 part 1
def calculate_position():
    file = open("data2.txt")
    content = file.read()
    direction_ls = content.splitlines() #list of strings
    horizontal = 0
    depth = 0

    for direction in direction_ls:
        split_dir = direction.split()
        command = split_dir[0]
        weight = int(split_dir[1])
        if command == "forward":
            horizontal += weight
        elif command == "up":
            depth -= weight
        else:
            depth += weight
    result = horizontal*depth
    print(result)

# day 2 part 2
def calculate_position_with_aim():
    file = open("data2.txt")
    content = file.read()
    direction_ls = content.splitlines()
    horizontal = 0
    depth = 0
    aim = 0

    for direction in direction_ls:
        split_dir = direction.split()
        command = split_dir[0]
        weight = int(split_dir[1])
        if command == "down":
            aim += weight
        elif command == "up":
            aim -= weight
        else:
            horizontal += weight
            depth += aim * weight
    result = horizontal*depth
    print(result)


