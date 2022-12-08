from ex7_helper import *
from ex7 import *


def test_mult():
    assert mult(1, 1) == 1
    assert mult(2, 1) == 2
    assert mult(2, 3) == 6
    assert mult(2.5, 2) == 5
    assert mult(2.5, 1) == 2.5
    assert mult(0, 1) == 0
    assert mult(0, 100) == 0
    assert mult(10, 10) == 100
    assert mult(0, 0) == 0
    assert mult(10, 0) == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(1000) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(1) is False
    assert is_even(479) is False
    assert is_even(8) is True


def test_log_mult():
    assert log_mult(1, 1) == 1
    assert log_mult(2, 1) == 2
    assert log_mult(2, 3) == 6
    assert log_mult(2.5, 2) == 5
    assert log_mult(2.5, 1) == 2.5
    assert log_mult(0, 1) == 0
    assert log_mult(0, 100) == 0
    assert log_mult(10, 10) == 100
    assert log_mult(0, 0) == 0
    assert log_mult(10, 0) == 0
    assert log_mult(2, 100000) == 200000 , "Too long runtime"
    # This test won't work if your runtime is O(n), because the recursion
    # depth is too deep.


def test_is_power():
    assert is_power(2, 16) is True
    assert is_power(3, 17) is False
    assert is_power(1, 1) is True
    assert is_power(1, 5) is False
    assert is_power(5, 25) is True
    assert is_power(5, 5) is True
    assert is_power(2, 2048) is True
    assert is_power(3, 81) is True
    assert is_power(3, 84) is False
    assert is_power(2048, 4194304) is True
    assert is_power(0, 0) is True
    assert is_power(0, 1) is True  # 0 ^ 0 =1
    assert is_power(1, 0) is False
    assert is_power(1000, 1) is True
    assert is_power(100000000, 1) is True
    assert is_power(2, 2 ** 950) is True, "Too long runtime"
    assert is_power(10, 10 ** 950) is True, "Too long runtime"
    assert is_power(2, 2 ** 950 + 2) is False, "Too long runtime"
    assert is_power(2 ** 21, 2 ** 42) is True, "Too long runtime"


def test_reverse():
    assert reverse("intro") == "ortni"
    assert reverse("test") == "tset"
    assert reverse("tst") == "tst"
    assert reverse("t1e2s3t4") == "4t3s2e1t"
    assert reverse("") == ""
    assert reverse("1") == "1"
    assert reverse("1" * 950) == "1" * 950, "Too long runtime"


def test_number_of_ones():
    assert number_of_ones(1) == 1
    assert number_of_ones(9) == 1
    assert number_of_ones(13) == 6
    assert number_of_ones(18) == 11
    assert number_of_ones(19) != 11


def test_ones_in_num_helper():
    # Testing of a helper function. You can ignore if this function doesn't
    # exist in your code.
    assert number_of_ones_helper(10,0) == 1
    assert number_of_ones_helper(110,0) == 2
    assert number_of_ones_helper(111,0) == 3
    assert number_of_ones_helper(112,0) == 2
    assert number_of_ones_helper(211,0) == 2
    assert number_of_ones_helper(212,0) == 1
    assert number_of_ones_helper(1001,0) == 2
    assert number_of_ones_helper(1010100,0) == 3


def test_compare_1d_lists():
    # Testing of a helper function. You can ignore if this function doesn't
    # exist in your code.
    assert compare_1d_lists([1], [1]) is True
    assert compare_1d_lists([1, 2], [1, 2]) is True
    assert compare_1d_lists([1, 2], [1, 3]) is False
    assert compare_1d_lists([1, 2], [1]) is False
    assert compare_1d_lists([2], [1]) is False
    assert compare_1d_lists([1, 2], [1, 3]) is False
    assert compare_1d_lists([2, 3], [1, 3]) is False

    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    compare_1d_lists(l1, l2)
    assert l1 == [1, 2, 3] and l2 == [1, 2, 3], "You changed lists"


def test_compare_2d_lists():
    assert compare_2d_lists([[1]], [[1]]) is True
    assert compare_2d_lists([[1, 2]], [[1, 2]]) is True
    assert compare_2d_lists([[1, 2], [1]], [[1, 2], [1]]) is True
    assert compare_2d_lists([[1, 2], [1]], [[1, 2], [3]]) is False
    assert compare_2d_lists([[1, 2], [1]], [[1, 3], [1]]) is False
    assert compare_2d_lists([[1, 2], []], [[1, 2], [3]]) is False
    assert compare_2d_lists([[1, 2], [1]], [[2, 1], [3]]) is False
    assert compare_2d_lists([[1, 2], []], [[1, 2], []]) is True
    assert compare_2d_lists([[1], [2], [3]], [[1], [2], [3]]) is True
    assert compare_2d_lists([[1], [], [3]], [[1], [], [3]]) is True
    assert compare_2d_lists([], []) is True
    assert compare_2d_lists([[], []], [[], []]) is True
    assert compare_2d_lists([[], []], [[], [], []]) is False
    very_long_list = [[5] * 950]
    assert compare_2d_lists(very_long_list, very_long_list) is True,\
        "Too long runtime"
    another_very_long_list = [[5] * 949]
    assert compare_2d_lists(very_long_list, another_very_long_list) is False, \
        "Too long runtime"
    assert compare_2d_lists([[1, 2], [4, 5, 8]], [[1, 2], [4, 5, 6]]) is False

    l1 = [[1], [2], [3]]
    l2 = [[1], [2], [3]]
    compare_2d_lists(l1, l2)
    assert l1 == [[1], [2], [3]] and l2 == [[1], [2], [3]], "You changed lists"


def test_magic_list():
    assert magic_list(0) == []
    assert magic_list(1) == [[]]
    assert magic_list(2) == [[], [[]]]
    assert magic_list(3) == [[], [[]], [[], [[]]]]
    assert magic_list(4) == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]
    # Checking if it is a deepcopy or not:
    first_magic = magic_list(2)
    first_magic[0].append(2)
    assert first_magic == [[2], [[]]], "Not Deep Copy"
    assert first_magic != [[2], [[2]]]