def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    new_list = []
    for fl in nums:
        if type(fl) == float:
            new_list.append(fl)
    return sum(new_list)

# Solution #2
#     return sum([num for num in nums if isinstance(num, float)])
