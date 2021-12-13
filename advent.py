# day 1 part 1
def count_increases():
    file = open("data.txt")
    content = file.read()
    nums_list = content.splitlines()
    int_nums = []
    for num in nums_list:
        int_num = int(num)
        int_nums.append(int_num)
    increase_count = 0
    for i in range(len(int_nums)-1):
        if int_nums[i+1] > int_nums[i]:
            increase_count += 1
    print(increase_count)

# day 1 part 2
def count_sum_increase():
    file = open("data.txt")
    content = file.read()
    nums_list = content.splitlines()
    int_nums = []
    for num in nums_list:
        int_num = int(num)
        int_nums.append(int_num)
    sum3_ls = []
    for i in range(len(int_nums)-2):
        sum3 = int_nums[i] + int_nums[i+1] + int_nums[i+2]
        sum3_ls.append(sum3)
    increase_sum_count = 0 
    for i in range(len(sum3_ls)-1):
        if sum3_ls[i+1] > sum3_ls[i]:
            increase_sum_count += 1
    print(increase_sum_count)


# day 2 part 1
def calculate_position():
    file = open("data2.txt")
    content = file.read()
    direction_ls = content.splitlines()
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

