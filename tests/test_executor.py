import unittest


class TestExecutor(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1 + 1, 2)

    def test_string(self):
        self.assertEqual("agent", "agent")


if __name__ == "__main__":
    unittest.main()
