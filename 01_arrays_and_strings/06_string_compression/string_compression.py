# O(n)
import unittest


def string_compression(string):
    result = ""
    current = string[0]
    count = 1

    for char in string[1:]:
        if char == current:
            count += 1
        else:
            result += "{}{}".format(current, count)
            current = char
            count = 1
    result += "{}{}".format(current, count)

    if len(result) >= len(string):
        return string
    return result


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()