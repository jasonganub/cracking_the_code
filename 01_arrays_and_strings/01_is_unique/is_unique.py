def is_unique(s):
    """ ASCII string"""
    s = list(s)

    if len(s) > 128:
        return False

    nums = [False] * 128

    for char in s:
        num = ord(char) - 97
        if nums[num]: # if it exists as true, then it was once changed
            return False
        else:
            nums[num] = True
    return True



print(is_unique('abcd'))