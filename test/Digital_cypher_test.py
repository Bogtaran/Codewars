from unittest import TestCase, main
from Digital_cypher import encode, index, sum_num_key


class IndexTest(TestCase):
    def test_encode(self):
        self.assertEqual(encode('', 12), [])

    def test_index(self):
        self.assertEqual(index('a'), [1])

    def test_index(self):
        self.assertEqual(index('ab'), [1, 2])

    def test_sum_num_key(self):
        self.assertEqual(sum_num_key([1, 2], 12), [2, 4])

    def test_sum_num_key(self):
        self.assertEqual(sum_num_key([1, 2], 123), [2, 4])

    def test_sum_num_key(self):
        self.assertEqual(sum_num_key([1, 2, 3], 12), [2, 4, 4])

    def test_encode(self):
        self.assertEqual(encode('ab', 12), [2, 3])

    def test_encode(self):
        self.assertEqual(encode('abc', 12), [2, 4, 4])


if __name__ == '__main__':
    main()
