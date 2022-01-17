# time complexity - O(N + M + max(N,M)) where N and M are lengths of input strings
# space complexity - O(N+M) to store arrays version1 and version2

import unittest

def compareVersion(version1, version2):
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]
    for i in range(max(len(versions1),len(versions2))):
        a = versions1[i] if i < len(versions1) else 0
        b = versions2[i] if i < len(versions2) else 0
        if a > b:
            return 1
        elif a < b:
            return -1
    return 0


class TestCases(unittest.TestCase):

    # 5 test cases for success check
    def test_successcase_1(self):
        self.assertEqual(compareVersion("0.1", "1.0"), -1, "Should be -1")
    def test_successcase_2(self):
        self.assertEqual(compareVersion("2.9.9.8", "2.9.9.9"), -1, "Should be -1")
    def test_successcase_3(self):
        self.assertEqual(compareVersion("2.9.8", "2.9.8.9"), -1, "Should be -1")
    def test_successcase_4(self):
        self.assertEqual(compareVersion("1.2.4.5", "1.2"), 1, "Should be 1")
    def test_successcase_5(self):
        self.assertEqual(compareVersion("0.1.1", "0.1.2"), -1, "Should be -1")

    # 4 test cases for failure check
    def test_failurecase_1(self):
        self.assertEqual(compareVersion("0.1", "1.0"), 1, "Should be -1")
    def test_failurecase_2(self):
        self.assertEqual(compareVersion("1.0", "0.1"), -1, "Should be 1")
    def test_failurecase_3(self):
        self.assertEqual(compareVersion("1.0", "1.0"), 1, "Should be 0")
    def test_failurecase_4(self):
        self.assertEqual(compareVersion("2.5", "2.5.0"), 1, "Should be 0")


if __name__ == '__main__':
    unittest.main()