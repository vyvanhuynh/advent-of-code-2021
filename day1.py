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
