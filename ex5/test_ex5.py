import image_editor


def test_separate_channels():
    assert image_editor.separate_channels(
        [[[1], [1], [1], [1]]]) == [[[1, 1, 1, 1]]]
    assert image_editor.separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    assert image_editor.separate_channels([[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                           [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                           [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                           [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
                                          ) == [[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                                                [[2, 2, 2], [2, 2, 2], [
                                                    2, 2, 2], [2, 2, 2]],
                                                [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]]

    assert image_editor.separate_channels([[[1, 2], [1]]]) == [
        [[1, 1]], [[2]]]
    assert image_editor.separate_channels([[[1, 2], [1, 1]], [[1, 2], [1, 1]]]) == [
        [[1, 1], [1, 1]], [[2, 1], [2, 1]]]
    assert image_editor.separate_channels([[[1]]]) == [[[1]]]
    assert image_editor.separate_channels(
        [[[1], [1]],
         [[2], [2]]]) == [[[1, 1], [2, 2]]]
    assert image_editor.separate_channels([[[1]]]) == [[[1]]]
    assert image_editor.separate_channels([[[]]]) == [[[]]]
    assert image_editor.separate_channels([[]]) == [[[]]]
    assert image_editor.separate_channels([]) == [[[]]]


def test_combine_channels():
    assert image_editor.combine_channels([[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                                          [[2, 2, 2], [2, 2, 2], [
                                              2, 2, 2], [2, 2, 2]],
                                          [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]]) == [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                                                                                             [[1, 2, 3], [1, 2, 3], [
                                                                                                 1, 2, 3]],
                                                                                             [[1, 2, 3], [1, 2, 3], [
                                                                                                 1, 2, 3]],
                                                                                             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    assert image_editor.combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert image_editor.combine_channels([[[1, 1]], [[2, 2]]]) == [
        [[1, 2], [1, 2]]]
    assert image_editor.combine_channels([[[1, 1], [1, 1]],
                                          [[2, 2], [2, 2]]]) == [
        [[1, 2], [1, 2]], [[1, 2], [1, 2]]]
    assert image_editor.combine_channels([[[1, 1], [1, 1], [1, 1]], [[2, 2], [2, 2], [2, 2]]]) == [
        [[1, 2], [1, 2]], [[1, 2], [1, 2]], [[1, 2], [1, 2]]]


def test_grayscale():
    assert image_editor.RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert image_editor.RGB2grayscale([[
        [200, 0, 14], [15, 6, 50]]]) == [[61, 14]]


def test_apply_kernel():
    assert image_editor.apply_kernel(
        [[0, 128, 255]], image_editor.blur_kernel(3)) == [[14, 128, 241]]
    assert image_editor.apply_kernel([[10, 20, 30, 40, 50],
                                      [8, 16, 24, 32, 40],
                                      [6, 12, 18, 24, 30],
                                      [4, 8, 12, 16, 20]], image_editor.
                                     blur_kernel(5)) == [[12, 20, 26, 34, 44],
                                                         [11, 17, 22, 27, 34],
                                                         [10, 16, 20, 24, 29],
                                                         [7, 11, 16, 18, 21]]
    assert image_editor.apply_kernel(
        [[0, 128, 255]], image_editor.blur_kernel(1)) == [[0, 128, 255]]
    assert image_editor.apply_kernel([[0, 1, 2, 0, 1], [1, 2, 2, 0, 0], [0, 1, 2, 1, 0], [
                                     0, 2, 1, 1, 0], [0, 0, 1, 0, 2]], [[0, 0, 0], [1, -1, 0], [1, 1, -1]]) == [[0, 0, 3, 4, 0], [0, 0, 2, 5, 1], [0, 0, 1, 3, 2], [0, 0, 2, 0, 3], [0, 0, 0, 1, 0]]
    assert image_editor.apply_kernel([[0, 1, 2, 0, 1], [1, 2, 2, 0, 0], [0, 1, 2, 1, 0], [
        0, 2, 1, 1, 0], [0, 0, 1, 0, 2]], [[0, 0, 0], [1, -1, 0], [1, 1, -1]]) == [[0, 0, 3, 4, 0], [0, 0, 2, 5, 1], [0, 0, 1, 3, 2], [0, 0, 2, 0, 3], [0, 0, 0, 1, 0]]
