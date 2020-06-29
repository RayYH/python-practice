import unittest


class BasicUsage(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(4, 2 + 2)
        self.assertEqual(288925, 53672 + 235253)
        # 除法的运算结果为小数
        self.assertEqual(0.5, 1 / 2)
        self.assertEqual(1.0, 1 / 1)
        self.assertEqual(type(0.5), type(1 / 2))
        # 如果你想丢弃小数部分，请使用 //
        self.assertEqual(1 // 2, 0)
        self.assertEqual(1 // 1, 1)
        self.assertEqual(5.0 // 2.4, 2)
        self.assertEqual(type(1), type(1 // 2))
        # % 用于取模
        self.assertEqual(1, 1 % 2)


if __name__ == '__main__':
    unittest.main()
