import unittest
import StacksAndQueues

class Test_test1(unittest.TestCase):
    def test_AllBracesMatch(self):
        text = "{H[i t(h)e]re!}"

        self.assertTrue( StacksAndQueues.braces_are_matching(text) )

    def test_Mismatch(self):
        text = "{H[i t(h])ere!}"

        self.assertFalse( StacksAndQueues.braces_are_matching(text) )

    def test_ExtraOpenBraces(self):
        text = "{{H[i t(h)e]re!}"

        self.assertFalse( StacksAndQueues.braces_are_matching(text) )

    def test_ExtraClosedBraces(self):
        text = "{H[i t(h)e]re!}]"

        self.assertFalse( StacksAndQueues.braces_are_matching(text) )


if __name__ == '__main__':
    unittest.main()
