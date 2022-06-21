def max_num(*nums):
    maximum_num = nums[0]
    for i in nums:
        if i > maximum_num:
            maximum_num = i
            # print
    print(maximum_num)


# max_num(-12, -5, -3, -2, 1, 100)


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

    return number >= beginning and number <= end


# print(num_within(0, 1, 3))


def pascal(n):
    triangle_rows = []
# if we have an input of greater number than the length of rows we already have, we want to add it to list of rows in the triangle
    new_row = [1]
    for num in range(1, n+1):
        for n in range(1, num):
            new_row.append([1])
        print(new_row)


pascal(3)
