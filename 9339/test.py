# coding: utf-8


from unittest.mock import patch
import unittest

from p9339 import solution


class P9339TestCase(unittest.TestCase):

    def test_solution(self):
        user_input_1 = [
            '4',
            '123 456 999 73',
            '6',
            '111 5 3',
            '456 -1 -1',
            '123 4 59',
            '73 6 0',
            '520 -1 -1',
            '999 6 0'
        ]
        user_input_2 = [
            '5',
            '3 5 2 7 1',
            '10',
            '5 8 3',
            '4 6 20',
            '9 4 10',
            '10 5 20',
            '1 6 1',
            '2 4 20',
            '3 4 20',
            '6 4 20',
            '7 4 15',
            '8 4 10',
        ]
        right_ans_1 = (123, 3)
        right_ans_2 = (7, 3)
        with patch('builtins.input', side_effect=user_input_1):
            ans = solution()

        self.assertEqual(ans, right_ans_1)

        with patch('builtins.input', side_effect=user_input_2):
            ans = solution()

        self.assertEqual(ans, right_ans_2)


if __name__ == '__main__':
    unittest.main()
