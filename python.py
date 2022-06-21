from operator import truediv


def max_num(*nums):
    maximum_num = 0
    for i in nums:
        if i > maximum_num:
            maximum_num = i
            # print
    print(maximum_num)

# max_num(2,32,-5)


def mult_list(nums):
    nums_multiplied = 1
    for number in nums:
        nums_multiplied *= number
    print(nums_multiplied)

# mult_list([1,2,3,4])


def rev_string(string):
    string_list = []

    for character in reversed(string):
        string_list.append(character)
    reversed_string = ''.join(string_list)
    return reversed_string


# print(rev_string('kayaks'))

def num_within(number, beginning, end):
    num_is_in_range = None
    if number >= beginning and number <= end:
        num_is_in_range = True
    else:
        num_is_in_range = False
    return num_is_in_range


# print(num_within(2, 1, 3))

def pascal():
    triangle_rows = [[1],[1,1]]
