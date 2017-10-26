def permutation(a, b):
    # Hash tables take up more space
    if len(a) != len(b):
        return False

    h = {}

    for char in a:
        if char in h:
            h[char] += 1
        else:
            h[char] = 1

    for char in b:
        if char in h:
            h[char] -= 1
            if h[char] == 0:
                del h[char]
        else:
            return False

    return True


print(permutation("abc", "cba"))