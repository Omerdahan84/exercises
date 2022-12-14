import image_editor
import copy


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

    assert image_editor.separate_channels([[[1, 2], [1, 1]], [[1, 2], [1, 1]]]) == [
        [[1, 1], [1, 1]], [[2, 1], [2, 1]]]
    assert image_editor.separate_channels([[[1]]]) == [[[1]]]
    assert image_editor.separate_channels(
        [[[1], [1]],
         [[2], [2]]]) == [[[1, 1], [2, 2]]]
    assert image_editor.separate_channels([[[1]]]) == [[[1]]]
    assert image_editor.separate_channels([[[1, 2], [3, 4]]]) == [
        [[1, 3]], [[2, 4]]]
    assert image_editor.separate_channels([[[1, 2]], [[3, 4]]]) == [
        [[1], [3]], [[2], [4]]]
    assert image_editor.separate_channels(
        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) == [
        [[1, 4], [7, 10]], [[2, 5], [8, 11]], [[3, 6], [9, 12]]]
    assert image_editor.separate_channels(
        [[[1, 2, 3]]*3]*4) == [[[1]*3]*4, [[2]*3]*4, [[3]*3]*4]
    assert image_editor.separate_channels([[[1, 2]]]) == [[[1]], [[2]]]
    image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    image_lst = [[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                 [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]],
                 [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]]
    assert image_editor.separate_channels(image) == image_lst


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
    assert image_editor.combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    assert (
        image_editor.combine_channels(
            [[[1] * 3] * 4, [[2] * 3] * 4, [[3] * 3] * 4])
        == [[[1, 2, 3]] * 3] * 4
    )
    assert image_editor.combine_channels([[[1]], [[2]]]) == [[[1, 2]]]
    image_lst = [[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
                 [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]],
                 [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]]
    image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    assert image_editor.combine_channels(image_lst) == image


def test_grayscale():
    assert image_editor.RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    assert image_editor.RGB2grayscale([[
        [200, 0, 14], [15, 6, 50]]]) == [[61, 14]]
    assert image_editor.RGB2grayscale([[[100, 180, 240], [100, 180, 240]],
                                       [[100, 180, 240], [100, 180, 240]]]) == [[163, 163],
                                                                                [163, 163]]
    assert image_editor.RGB2grayscale(
        [[[200, 0, 14], [15, 6, 50]]]) == [[61, 14]]
    # Tests rounding up
    assert image_editor.RGB2grayscale([[[100, 180, 240]]]) == [[163]]
    # Tests rounding down
    assert image_editor.RGB2grayscale(
        [[[200, 0, 14], [15, 6, 50]]]) == [[61, 14]]


def test_kernel():
    assert image_editor.blur_kernel(3) == [[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9],
                                           [1 / 9, 1 / 9, 1 / 9]]
    assert image_editor.blur_kernel(11) == [[1 / 121] * 11] * 11
    assert image_editor.blur_kernel(1) == [[1.0]]
    assert image_editor.blur_kernel(7) == [[1/49]*7]*7


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
    assert image_editor.apply_kernel(
        [[0, 128, 255]], [[1]]) == [[0, 128, 255]]
    assert image_editor.apply_kernel(
        [[0, 128, 255]], image_editor.blur_kernel(3)) == [[14, 128, 241]]
    assert image_editor.apply_kernel(
        [
            [10, 20, 30, 40, 50],
            [8, 16, 24, 32, 40],
            [6, 12, 18, 24, 30],
            [4, 8, 12, 16, 20],
        ],
        image_editor.blur_kernel(5),
    ) == [
        [12, 20, 26, 34, 44],
        [11, 17, 22, 27, 34],
        [10, 16, 20, 24, 29],
        [7, 11, 16, 18, 21],
    ]
    assert image_editor.apply_kernel([[1, 1, 1]], [[1]*3]*3) == [[9, 9, 9]]
    assert image_editor.apply_kernel([[1, 1, 1]], [[0]*3]*3) == [[0, 0, 0]]
    assert image_editor.apply_kernel(
        [[1, 2, 3]], [[0]*3, [0, 1, 0], [0]*3]) == [[1, 2, 3]]
    assert image_editor.apply_kernel(
        [[1, 2, 3]], [[0]*3, [0, 0, 1], [0]*3]) == [[2, 3, 3]]
    assert image_editor.apply_kernel(
        [[0, 128, 255]], image_editor.blur_kernel(3)) == [[14, 128, 241]]
    image = [[10, 20, 30, 40, 50],
             [8, 16, 24, 32, 40],
             [6, 12, 18, 24, 30],
             [4, 8, 12, 16, 20]]
    image_blurred = [[12, 20, 26, 34, 44],
                     [11, 17, 22, 27, 34],
                     [10, 16, 20, 24, 29],
                     [7, 11, 16, 18, 21]]

    assert image_editor.apply_kernel(
        image, image_editor.blur_kernel(5)) == image_blurred


def test_bilinear_interpolation():
    image = [[15, 30, 45, 60, 75],
             [90, 105, 120, 135, 150],
             [165, 180, 195, 210, 225]]
    assert image_editor.bilinear_interpolation(image, 4/5, 8/3) == 115
    assert image_editor.bilinear_interpolation(image, 0, 0) == 15
    assert image_editor.bilinear_interpolation(image, 0, 4) == 75
    assert image_editor.bilinear_interpolation(image, 2, 4) == 225
    assert image_editor.bilinear_interpolation(image, 2, 0) == 165
    assert image_editor.bilinear_interpolation(image, 0.5, 0.5) == 60
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0, 0) == 0
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 1, 1) == 255
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0.5, 1) == 160
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0, 0) == 0
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 1, 1) == 255
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0.5, 1) == 160
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0, 1) == 64
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 1, 1) == 255
    assert image_editor.bilinear_interpolation(
        [[0, 64], [128, 255]], 0.5, 0.5) == 112
    assert image_editor.bilinear_interpolation(
        [[1, 1, 1]], 0.4, 0.4) == [[1, 1, 1]]


def test_resize():
    assert image_editor.resize([[0, 50], [100, 200]], 3, 4) == [
        [0, 17, 33, 50], [50, 75, 100, 125], [100, 133, 167, 200]]
    assert image_editor.resize([[0, 1], [2, 3]], 10, 10)[9][9] == 3
    assert image_editor.resize([[0, 1], [2, 3]], 10, 10)[0][0] == 0
    assert image_editor.resize([[0, 1], [2, 3]], 10, 10)[0][9] == 1
    assert image_editor.resize([[0, 1], [2, 3]], 10, 10)[9][0] == 2
    mat = [[2, 4, 6],
           [3, 8, 12],
           [16, 5, 11]]
    assert image_editor.resize(mat, 2, 2) == [[2, 6], [16, 11]]
    assert image_editor.resize(mat, 6, 6) == [[2, 3, 4, 4, 5, 6], [2, 4, 5, 6, 7, 8], [
        3, 5, 6, 8, 9, 11], [6, 6, 7, 8, 10, 12], [11, 9, 7, 7, 9, 11], [16, 12, 7, 6, 9, 11]]
    assert image_editor. resize(mat, 3, 6) == [[2, 3, 4, 4, 5, 6], [
        3, 5, 7, 9, 10, 12], [16, 12, 7, 6, 9, 11]]
    assert image_editor.resize(mat, 6, 3) == [[2, 4, 6], [2, 6, 8], [
        3, 7, 11], [6, 7, 12], [11, 6, 11], [16, 5, 11]]
    assert image_editor.resize(mat, 4, 4) == [[2, 3, 5, 6], [
        3, 5, 8, 10], [7, 7, 9, 12], [16, 9, 7, 11]]
    assert image_editor.resize([[1, 2, 4, 2], [2, 2, 4, 3], [4, 1, 3, 1], [5, 4, 1, 1]], 5, 5) == [
        [1, 2, 3, 4, 2], [2, 2, 3, 4, 3], [3, 2, 2, 3, 2], [4, 2, 2, 2, 1], [5, 4, 2, 1, 1]]

    image = [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]
    resized_img = [[1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 1]]
    assert image_editor.resize(image, 4, 5) == resized_img
    assert image_editor.resize(resized_img, 3, 3) == image
    image = [[1, 2, 3],
             [4, 5, 6]]
    assert image_editor.resize(image, 2, 3) == image
    image = [[200, 100, 150]]
    image_cpy = copy.deepcopy(image)
    image_editor.resize(image, 4, 4)
    assert image == image_cpy


def test_rotate_90():
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'R') == [[7, 4, 1],
                                                                              [8, 5, 2],
                                                                              [9, 6, 3]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'L') == [[3, 6, 9],
                                                                              [2, 5, 8],
                                                                              [1, 4, 7]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1],
                                                                   [5, 2],
                                                                   [6, 3]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6],
                                                                   [2, 5],
                                                                   [1, 4]]
    assert image_editor.rotate_90(
        [[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[4, 5, 6], [5, 6, 7], [6, 7, 8]]],
        'L') == [
        [[3, 4, 5], [6, 7, 8]],
        [[2, 3, 4], [5, 6, 7]],
        [[1, 2, 3], [4, 5, 6]]]
    assert image_editor.rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') == [
        [[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [
        [4, 1], [5, 2], [6, 3]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [
        [3, 6], [2, 5], [1, 4]]
    assert image_editor.rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') == [
        [[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]]
    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [
        [4, 1], [5, 2], [6, 3]]

    assert image_editor.rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [
        [3, 6], [2, 5], [1, 4]]
    assert image_editor.rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') ==\
        [[[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]]
    assert image_editor.rotate_90([[[23, 232], [34, 43]], [[12, 23], [32, 21]], [[12, 65], [87, 76]]], "R") ==\
        [[[12, 65], [12, 23], [23, 232]], [[87, 76], [32, 21], [34, 43]]]
    image1 = [[1, 2, 3],
              [4, 5, 6]]
    image2 = [[4, 1],
              [5, 2],
              [6, 3]]
    image3 = [[3, 6],
              [2, 5],
              [1, 4]]
    assert image_editor.rotate_90(image1, "R") == image2
    assert image_editor.rotate_90(image1, "L") == image3
    assert image_editor.rotate_90(
        image_editor.rotate_90(image2, "L"), "L") == image3
    image4 = [[[1, 1], [2, 2]]]
    image5 = [[[1, 1]],
              [[2, 2]]]
    assert image_editor.rotate_90(image4, "R") == image5
    assert image_editor.rotate_90(image5, "L") == image4

    # From the exercise PDF
    image6 = [[[1, 2, 3], [4, 5, 6]],
              [[0, 5, 9], [255, 200, 7]]]
    image7 = [[[4, 5, 6], [255, 200, 7]],
              [[1, 2, 3], [0, 5, 9]]]
    assert image_editor.rotate_90(image6, 'L') == image7


def test_quantize():
    assert image_editor.quantize([[0, 50, 100], [150, 200, 250]], 8) == [
        [0, 36, 109], [146, 219, 255]]
    assert image_editor.quantize([[32, 76, 65, 4], [54, 47, 8, 7], [1, 2, 84, 95], [87, 57, 35, 3], [123, 234, 5, 3]], 5) ==\
        [[0, 64, 64, 0], [64, 0, 0, 0], [0, 0, 64, 64],
            [64, 64, 0, 0], [128, 255, 0, 0]]


def test_quantize_colored_image():
    assert image_editor.quantize_colored_image([[[33, 5], [34, 2]], [[24, 43], [45, 56]], [[87, 76], [65, 54]]], 30) ==\
        [[[26, 0], [26, 0]], [[18, 44], [44, 53]], [[88, 70], [62, 53]]]


def test_get_edges():
    assert image_editor.get_edges([[200, 50, 200]], 3, 3, 10) == [
        [255, 0, 255]]
    assert image_editor.get_edges([[200, 50, 200], [200, 50, 200], [200, 50, 200]], 1, 3,
                                  10) == [[255, 0, 255], [255, 0, 255], [255, 0, 255]]
    assert image_editor.get_edges([[23, 34, 45], [65, 54, 43], [3, 8, 4]], 3, 3, 3) == [
        [255, 255, 255], [255, 255, 255], [0, 0, 0]]


def test_combine_channels_inversion():
    image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    assert image == image_editor.separate_channels(
        image_editor.combine_channels(image))


def test_separate_channels_non_mutation():
    image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    image_cpy = copy.deepcopy(image)
    image_editor.separate_channels(image)
    assert image == image_cpy


def test_combine_channels_non_mutation():
    channels = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    channels_cpy = copy.deepcopy(channels)
    image_editor.combine_channels(channels)
    assert channels == channels_cpy


def test_combine_channels_inversion():
    image = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
             [[1, 2, 3], [1, 2, 3], [1, 2, 3]]]
    assert image == image_editor.separate_channels(
        image_editor.combine_channels(image))
