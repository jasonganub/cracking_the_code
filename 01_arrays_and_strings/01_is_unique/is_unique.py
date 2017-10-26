# O(N)
import unittest


def unique(s):
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



class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()