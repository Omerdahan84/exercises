from ex7 import *


def test_mult():
    assert mult(0, 5) == 0
    assert mult(15, 0) == 0
    assert mult(-7, 3) == -21
    assert mult(3, 1) == 3
    assert mult(1, 3) == 3
    assert mult(2.5, 2) == 5
    assert mult(0, 0) == 0


def test_is_even():
    assert is_even(0)
    assert not is_even(3)
    assert is_even(10)
    assert not is_even(1)
    assert not is_even(479)
    assert is_even(2)
    assert is_even(1000)


def test_log_mult():
    assert log_mult(0, 5) == 0
    assert log_mult(15, 0) == 0
    assert log_mult(-7, 3) == -21
    assert log_mult(3, 1) == 3
    assert log_mult(1, 3) == 3
    assert log_mult(2.5, 2) == 5
    assert log_mult(0, 0) == 0
    assert log_mult(2, 100000) == 200000, "Too long runtime"


def test_is_power():
    assert not is_power(3, 17)
    assert not is_power(1, 2)
    assert is_power(5, 5)
    assert is_power(2, 1024)
    assert is_power(3, 81)
    assert not is_power(3, 84)
    assert is_power(2048, 4194304)
    assert is_power(0, 0)
    assert is_power(0, 1)  # 0 ^ 0 =1
    assert not is_power(1, 0)
    assert is_power(100000000, 1)
    assert is_power(10, 10 ** 950), "Too long runtime"
    assert not is_power(2, 2 ** 950 + 2), "Too long runtime"
    assert is_power(2 ** 21, 2 ** 42), "Too long runtime"


def test_reverse():
    assert reverse('') == ''
    assert reverse('intro') == 'ortni'
    assert reverse("t1e2s3t4") == "4t3s2e1t"
    assert reverse("1" * 950) == "1" * 950, "Too long runtime"


def test_number_of_ones():
    assert number_of_ones(13) == 6
    assert number_of_ones(0) == 0
    assert number_of_ones(1) == 1
    assert number_of_ones(9) == 1
    assert number_of_ones(10) == 2
    assert number_of_ones(30) == 13
    assert number_of_ones(476) == 198



def test_compare_2d_lists():
    assert compare_2d_lists([[]], [[]])
    assert compare_2d_lists([[1]], [[1]])
    assert compare_2d_lists([[1, 2]], [[1, 2]])
    assert not compare_2d_lists([[1, 2], [1]], [[1, 2], [1, 1]])
    assert not compare_2d_lists([[1, 2], [1]], [[1, 2], [3]])
    assert not compare_2d_lists([[1, 2], [1]], [[1, 3], [1]])
    assert not compare_2d_lists([[1, 2], []], [[1, 2], [3]])
    assert compare_2d_lists([[1, 2], []], [[1, 2], []])
    assert compare_2d_lists([[1], [], [3]], [[1], [], [3]])
    assert compare_2d_lists([], [])
    assert compare_2d_lists([[], []], [[], []])
    assert not compare_2d_lists([[], []], [[], [], []])
    very_long_list = [[5] * 950]
    assert compare_2d_lists(very_long_list, very_long_list), "Too long runtime"
    another_very_long_list = [[5] * 949]
    assert not compare_2d_lists(very_long_list, another_very_long_list), \
        "Too long runtime"
    assert not compare_2d_lists([[1, 2], [4, 5, 8]], [[1, 2], [4, 5, 6]])
    l1 = [[1], [2], [3]]
    l2 = [[1], [2], [3]]
    compare_2d_lists(l1, l2)
    assert l1 == [[1], [2], [3]] and l2 == [[1], [2], [3]], "You changed lists"


def deep_copy(magic):
    if len(magic) > 1:
        for i in range(len(magic[-1])):
            assert magic[-1][i] is not magic[i], "Not Deep Copy"


def test_magic_list():
    assert magic_list(0) == []
    assert magic_list(1) == [[]]
    assert magic_list(2) == [[], [[]]]
    assert magic_list(3) == [[], [[]], [[], [[]]]]
    assert magic_list(4) == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]
    first_magic = magic_list(2)
    first_magic[0].append(2)
    assert first_magic == [[2], [[]]], "Not Deep Copy"
    magic = magic_list(5)
    assert magic == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]],
                     [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]]
    deep_copy(magic)


test_mult()
test_is_even()
test_log_mult()
test_is_power()
test_reverse()
test_compare_2d_lists()
test_magic_list()
test_number_of_ones()
