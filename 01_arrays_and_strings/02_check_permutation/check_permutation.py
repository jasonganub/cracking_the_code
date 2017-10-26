import unittest


def check_permutation(s):
    # Array has better performance assuming the input are ASCII strings
    str1 = s[0]
    str2 = s[1]

    if len(str1) != len(str2):
        return False

    letters = [0] * 128

    for char in str1:
        letters[ord(char)] += 1

    for char in str2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False

    return True

def check_permutation_hash_solution(s):
    # Hash tables take up more space
    str1 = s[0]
    str2 = s[1]

    if len(str1) != len(str2):
        return False

    h = {}

    for char in str1:
        if char in h:
            h[char] += 1
        else:
            h[char] = 1

    for char in str2:
        if char in h:
            h[char] -= 1
            if h[char] == 0:
                del h[char]
        else:
            return False

    return True


class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()