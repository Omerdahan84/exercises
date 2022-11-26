from image_editor import *

print("separate_channels")
print(separate_channels([[[1, 2, 3]]*3]*4)
      == [[[1]*3]*4, [[2]*3]*4, [[3]*3]*4])
print(separate_channels([[[1, 2]]]) == [[[1]], [[2]]])
print(separate_channels([[[1, 5, 6], [8, 4, 8], [3, 4, 5]], [[5, 4, 3], [9, 0, 7], [1, 4, 5]], [[2, 4, 7], [3, 9, 3], [6, 5, 3]]])
      == [[[1, 8, 3], [5, 9, 1], [2, 3, 6]], [[5, 4, 4], [4, 0, 4], [4, 9, 5]], [[6, 8, 5], [3, 7, 5], [7, 3, 3]]])
print("combine_channels")
print(combine_channels([[[1]], [[2]]]) == [[[1, 2]]])
print(combine_channels([[[1]*4]*5, [[2]*4]*5, [[3]*4]
      * 5, [[4]*4]*5]) == [[[1, 2, 3, 4]]*4]*5)
print(combine_channels([[[2, 5, 1], [25, 6, 7]], [[3, 5, 54], [2, 3, 9]], [[8, 7, 6], [2, 5, 15]]])
      == [[[2, 3, 8], [5, 5, 7], [1, 54, 6]], [[25, 2, 2], [6, 3, 5], [7, 9, 15]]])
print("RGB2grayscale")
print(RGB2grayscale([[[100, 180, 240]]]) == [[163]])
print(RGB2grayscale([[[200, 0, 14], [15, 6, 50]]]) == [[61, 14]])
print(RGB2grayscale([[[1, 5, 1], [2, 76, 2]], [[4, 87, 2], [12, 23, 34]], [[34, 45, 56], [7, 6, 5]]])
      == [[3, 45], [52, 21], [43, 6]])
print("blur_kernel")
print(blur_kernel(3) == [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
print(blur_kernel(5)
      == [[0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04]])
print("apply_kernel")
print(apply_kernel([[0, 128, 255]], blur_kernel(3)) == [[14, 128, 241]])
print(apply_kernel([[56, 54, 23], [2, 5, 45], [13, 24, 2], [56, 45, 3], [56, 75, 7], [6, 5, 4]], [[-0.1, 0.05, -0.12], [0.2, 0.12, 0.2], [0.17, 10, 30]])
      == [[199, 255, 255], [255, 255, 255], [255, 255, 105], [255, 255, 180], [244, 189, 255], [237, 201, 155]])
print(apply_kernel([[10, 20, 30, 40, 50], [8, 16, 24, 32, 40], [6, 12, 18, 24, 30],
                    [4, 8, 12, 16, 20]], blur_kernel(5)) == [[12, 20, 26, 34, 44], [11, 17, 22, 27,
                                                                                    34], [10, 16, 20, 24, 29], [7, 11, 16, 18, 21]])
# print("bilinear_interpolation")
# print(bilinear_interpolation([[0, 64], [128, 255]], 0, 0) == 0)
# print(bilinear_interpolation([[0, 64], [128, 255]], 1, 1) == 255)
# print(bilinear_interpolation([[0, 64], [128, 255]], 0.5, 0.5) == 112)
# print(bilinear_interpolation([[0, 64], [128, 255]], 0.5, 1) == 160)
# print(bilinear_interpolation([[56,54,3,4],[76,67,54,45],[3,4,5,6],[3,87,65,5],[12,23,34,45]],2.45, 3) == 6)
# print("resize")
print(resize([[1, 2, 4, 2], [2, 2, 4, 3], [4, 1, 3, 1], [5, 4, 1, 1]], 5, 5) == [
      [1, 2, 3, 4, 2], [2, 2, 3, 4, 3], [3, 2, 2, 3, 2], [4, 2, 2, 2, 1], [5, 4, 2, 1, 1]])
print(resize([[1, 2, 3, 4, 2], [2, 2, 3, 4, 3], [3, 2, 2, 3, 2], [4, 2, 2, 2, 1], [5, 4, 2, 1, 1]], 4, 4)
      == [[1, 2, 4, 2], [2, 2, 3, 3], [4, 2, 2, 1], [5, 3, 1, 1]]) print(resize([[34, 3, 24, 5, 8, 7], [23, 45, 34, 2, 1, 6], [2, 3, 7, 6, 56, 56], [2, 13, 24, 35, 4, 4], [24, 35, 46, 75, 64, 53], [123, 34, 32, 234, 54, 12]], 10, 8)
                                                                         == [[34, 12, 12, 21, 8, 7, 8, 7], [28, 27, 28, 26, 7, 4, 5, 6], [21, 35, 36, 27, 7, 5, 8, 12], [9, 15, 17, 14, 6, 24, 38, 39],
                                                                             [2, 4, 8, 11, 12, 31, 44, 44], [2, 8, 15, 21, 27, 21, 16, 16], [9, 17, 25, 34, 46, 34, 23, 20], [22, 29, 37, 47, 67, 63, 55, 48], [68, 44, 37, 55, 131, 96, 52, 35], [123, 59, 33, 61, 205, 131, 42, 12]])
# print("scale_down_colored_image")
# print(scale_down_colored_image([[[5,4,3],[8,76,76],[65,5,45],[34,4,34]],[[23,23,2],[76,65,54],[23,34,24],[132,43,232]],[[32,4,4],[54,54,5],[34,34,3],[23,34,98]]], 3)
#        == [[[5, 4, 3], [36, 40, 60], [34, 4, 34]], [[32, 4, 4], [44, 44, 4], [23, 34, 98]]])
print("rotate_90")
print(rotate_90([[1, 2, 3], [4, 5, 6]], 'R') == [[4, 1], [5, 2], [6, 3]])
print(rotate_90([[1, 2, 3], [4, 5, 6]], 'L') == [[3, 6], [2, 5], [1, 4]])
print(rotate_90([[[1, 2, 3], [4, 5, 6]], [[0, 5, 9], [255, 200, 7]]], 'L') ==
      [[[4, 5, 6], [255, 200, 7]], [[1, 2, 3], [0, 5, 9]]])
print(rotate_90([[[23, 232], [34, 43]], [[12, 23], [32, 21]], [[12, 65], [87, 76]]], "R") ==
      [[[12, 65], [12, 23], [23, 232]], [[87, 76], [32, 21], [34, 43]]])
print("get_edges")
print(get_edges([[200, 50, 200]], 3, 3, 10) == [[255, 0, 255]])
print(get_edges([[23, 34, 45], [65, 54, 43], [3, 8, 4]], 3, 3, 3) == [
      [255, 255, 255], [255, 255, 255], [0, 0, 0]])
print("quantize")
print(quantize([[0, 50, 100], [150, 200, 250]], 8)
      == [[0, 36, 109], [146, 219, 255]])
print(quantize([[32, 76, 65, 4], [54, 47, 8, 7], [1, 2, 84, 95], [87, 57, 35, 3], [123, 234, 5, 3]], 5) ==
      [[0, 64, 64, 0], [64, 0, 0, 0], [0, 0, 64, 64], [64, 64, 0, 0], [128, 255, 0, 0]])
print("quantize_colored_image")
print(quantize_colored_image([[[33, 5], [34, 2]], [[24, 43], [45, 56]], [[87, 76], [65, 54]]], 30) ==
      [[[26, 0], [26, 0]], [[18, 44], [44, 53]], [[88, 70], [62, 53]]])
# print("add_mask")
# print(add_mask([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]], [[[250,250,250],
# [0,0,0]],[[250,250,100],[1,11,13]]], [[0, 0.5]]*2) == [[[250, 250, 250], [2,
# 2, 3]], [[250, 250, 100], [6, 11, 12]]])
# print(add_mask([[50, 50, 50]], [[200, 200, 200]], [[0, 0.5, 1]]) == [[200, 125, 50]])
# print(add_mask([[[12,23],[34,23]],[[52,53],[62,123]],[[97,75],[76,35]]], [[[52,53],[34,23]],[[76,35],[97,75]],[[62,123],[12,23]]], [[0.3,0.4],[1,0.5],[0.9,0]])
#        == [[[40, 44], [34, 23]], [[52, 53], [80, 99]], [[94, 80], [12, 23]]])
# print("cartoonify")
# print(cartoonify([[[13,24,43],[45,34,12],[65,45,6]],[[4,23,54],[76,7,22],[65,5,22]],[[95,81,2],[47,7,47],[6,36,47]]], 3, 5, 3, 4)
#        == [[[0, 0, 0], [0, 0, 0], [85, 0, 0]], [[0, 0, 0], [85, 0, 0], [85, 0, 0]], [[85, 85, 0], [0, 0, 0], [0, 0, 0]]])