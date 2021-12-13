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


# day 3 part 1
def binaryToDecimal(n): # n is of string type
    return int(n,2)


def find_common_bit_gamma(binary_ls):
    common_count_1 = 0
    common_count_0 = 0
    for bi in binary_ls:
        if bi == '1':
            common_count_1 += 1
        else:
            common_count_0 += 1
    if common_count_1 > common_count_0:
        common = 1
    else:
        common = 0
    return common

def find_common_bit_eps(binary_ls):
    common_count_1 = 0
    common_count_0 = 0
    for bi in binary_ls:
        if bi == '1':
            common_count_1 += 1
        else:
            common_count_0 += 1
    if common_count_1 < common_count_0:
        common = 1
    else:
        common = 0
    return common

def convert_ls_to_int(list):
    s = [str(i) for i in list]
    res = "".join(s)
    return(res)

def calculate_power_consumption():
    file = open("data3.txt")
    content = file.read()
    binary_list = content.splitlines()
    binary1_ls, binary2_ls, binary3_ls, binary4_ls, binary5_ls, binary6_ls,  = [], [], [], [], [], []
    binary7_ls, binary8_ls, binary9_ls, binary10_ls, binary11_ls, binary12_ls = [], [], [], [], [], []

    for binary in binary_list:
        binary1_ls.append(binary[0])
        binary2_ls.append(binary[1])
        binary3_ls.append(binary[2])
        binary4_ls.append(binary[3])
        binary5_ls.append(binary[4])
        binary6_ls.append(binary[5])
        binary7_ls.append(binary[6])
        binary8_ls.append(binary[7])
        binary9_ls.append(binary[8])
        binary10_ls.append(binary[9])
        binary11_ls.append(binary[10])
        binary12_ls.append(binary[11])

    common1 = find_common_bit_gamma(binary1_ls)
    common2 = find_common_bit_gamma(binary2_ls)
    common3 = find_common_bit_gamma(binary3_ls)
    common4 = find_common_bit_gamma(binary4_ls)
    common5 = find_common_bit_gamma(binary5_ls)
    common6 = find_common_bit_gamma(binary6_ls)
    common7 = find_common_bit_gamma(binary7_ls)
    common8 = find_common_bit_gamma(binary8_ls)
    common9 = find_common_bit_gamma(binary9_ls)
    common10 = find_common_bit_gamma(binary10_ls)
    common11 = find_common_bit_gamma(binary11_ls)
    common12 = find_common_bit_gamma(binary12_ls)
    gamma_bit = []
    gamma_bit.extend([common1,common2,common3,common4,common5,common6,common7,common8,common9,common10,common11,common12])
    gamma_rate = convert_ls_to_int(gamma_bit)
    gamma_rate_decimal = binaryToDecimal(gamma_rate)
    
    common1_e = find_common_bit_eps(binary1_ls)
    common2_e = find_common_bit_eps(binary2_ls)
    common3_e = find_common_bit_eps(binary3_ls)
    common4_e = find_common_bit_eps(binary4_ls)
    common5_e = find_common_bit_eps(binary5_ls)
    common6_e = find_common_bit_eps(binary6_ls)
    common7_e = find_common_bit_eps(binary7_ls)
    common8_e = find_common_bit_eps(binary8_ls)
    common9_e = find_common_bit_eps(binary9_ls)
    common10_e = find_common_bit_eps(binary10_ls)
    common11_e = find_common_bit_eps(binary11_ls)
    common12_e = find_common_bit_eps(binary12_ls)
    eps_bit = []
    eps_bit.extend([common1_e,common2_e,common3_e,common4_e,common5_e,common6_e,common7_e,common8_e,common9_e,common10_e,common11_e,common12_e])
    eps_rate = convert_ls_to_int(eps_bit)
    eps_rate_decimal = binaryToDecimal(eps_rate)

    result = gamma_rate_decimal * eps_rate_decimal
    print(result)
