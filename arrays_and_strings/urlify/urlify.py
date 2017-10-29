# O(n)
import unittest


def urlify(string, length):
    """function replaces single spaces with $20 and removes trailing spaces"""
    j = len(string)-1

    for i in reversed(range(length)):
        if string[i] == ' ':
            # replace spaces
            string[j] = '0'
            string[j-1] = '2'
            string[j-2] = '%'
            j -= 3
        else:
            # move characters
            string[j] = string[i]
            j -= 1
    return string


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()