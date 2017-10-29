import unittest


# O(n)
def pal_perm(string):
    '''function checks if a string is a permutation of a palindrome or not'''
    string = list(string.replace(" ", ""))

    letters = set()

    for letter in string:
        letter = letter.lower()
        if letter in letters:
            letters.remove(letter)
        else:
            letters.add(letter)

    if len(letters) > 1:
        return False
    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()