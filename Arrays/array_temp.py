# def findNumbers(nums):
#     number_with_even_digits = 0
#     for num in nums:
#         digits = 0
#         while num != 0:
#             digits += 1
#             num = num // 10
#         if digits % 2 == 0:
#             number_with_even_digits += 1
#     return number_with_even_digits
#

# def sortedSquares(nums):
#     nums = [x * x for x in nums]
#     return nums


if __name__ == "__main__":
    # a = findNumbers([555, 901, 482, 1771])
    # print(a)
    nums = [-1, 0, 2, 4, 5]

    a = list(map(lambda x: x * x, nums))
    print(a)
