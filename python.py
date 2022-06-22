from calendar import c
from operator import index


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
    triangle_rows = [[1], [1, 1]]
# if we have an input of greater number than the length of rows we already have, we want to add it to list of rows in the triangle
    if n < 1:
        print('needs to be greater than zero')
        return
# create a row, using the values of the previous row
# create a new row for each number in range of the first row to the nth row
    if n == 1:
        print(triangle_rows[0])
    elif n == 2:
        print(triangle_rows[0])
        print(triangle_rows[1])
    else:
        # new_rows = []
        # here I am creating the amount of rows based on the input (if input is 4 there should be 4 rows)
        while n > len(triangle_rows):
            # print(n)
            next_row = []
            triangle_rows.append(next_row)

            --n
# in this foor loop I am trying to create place holders for each index that a row should have
# the index equals the indices in the triangle rows list
        for index_of_row in range(2, n):
            # print(index_of_row)
            current_row = triangle_rows[index_of_row]
# using one as a place holder just to create indices to have something to compare to previous row
# because we know that every row has the same number as the row number itself (row five has five indices)
# has to add one because we start counting rows at 0
            current_row.extend([1] * (index_of_row + 1))
            prev_row = triangle_rows[index_of_row-1]
            # print(prev_row, 'prev row')
            for item_in_row in current_row[1:-1]:
                current_row[item_in_row] = prev_row[item_in_row -1] + prev_row[item_in_row]
                print(item_in_row, index_of_row)

    print(triangle_rows)


pascal(5)
# for index in range(3, n+1):
#     print(index)
#     row_content = []
#     while index > 0:
#         row_content.append(1)
#         n -= n
#     new_rows.append(row_content)
#     # print('this is row:', row)

# triangle_rows.append(row_content)

# print(triangle_rows)
