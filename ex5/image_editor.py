#################################################################
# FILE : image_editor.py
# WRITER : Omer Dahan , omer.dahan , 315466664
# EXERCISE : intro2cs ex5 2022-2023
# DESCRIPTION: A simple program that make photo filters
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
# Daffy Duck, duck_daffy.
# WEB PAGES I USED: www.looneytunes.com/lola_bunny
# NOTES: ...
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex5_helper import *
from typing import Optional

##############################################################################
#                                  Functions                                 #
##############################################################################


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """Get a 3 channel image and return matrix include 3 one channel images"""
    img_lst = []
    if len(image) == 0 or len(image[0]) == 0 or len(image[0][0]) == 0:
        return [[[]]]
    i = 0
    while i < len(image[0][0]):
        channel_table = []
        for row in image:
            row_channel = []
            for pixel in row:
                if (i >= len(pixel)):
                    continue
                row_channel.append(pixel[i])
            channel_table.append(row_channel)
        i += 1
        img_lst.append(channel_table)
    return img_lst


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    "Take a list of one channel images and combine it to one channle"
    colored_image = []
    for i in range(len(channels)):
        row = []
        for k in range(len(channels[i])):
            pixel = []
            if len(channels) >= 1:
                pixel.append(channels[0][i][k])
            if len(channels) >= 2:
                pixel.append(channels[1][i][k])
            if len(channels) >= 3:
                pixel.append(channels[2][i][k])
            row.append(pixel)
        colored_image.append(row)
    return colored_image


# print(combine_channels([[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
    # [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]],
    # [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]]))

# print(combine_channels([[[1]], [[2]]]))


def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """Gets a colorful image and turn it to grayscale"""
    gray_img: SingleChannelImage = []
    # For every row in the original image we will create a gray row
    for i in range(len(colored_image)):
        gray_row = []
        # in each row we iretating over the pixel and make them a one value
        # grayscale pixel acording to the formula
        for j in range(len(colored_image[i])):
            gray_pixel = 0
            gray_pixel = round((colored_image[i][j][0]*0.299) + (
                colored_image[i][j][1]*0.587)+(colored_image[i][j][2]*0.114))
            gray_row.append(gray_pixel)  # Adding the gray pixel
        gray_img.append(gray_row)  # Adding the garay row
    return gray_img


def blur_kernel(size: int) -> Kernel:
    """ makes a Kernel matrix in size x size dimensions with each value equal to 1/size^2"""
    Kernel = []
    for i in range(size):
        Kernel_row = []
        for j in range(size):
            Kernel_row.append(1/(size**2))
        Kernel.append(Kernel_row)
    return Kernel


def in_bounds(width, height, current_row, current_col, margin):
    """check if a given locatin is in bound of matrix"""
    if current_row - margin < 0 or current_col - margin < 0 or current_col + margin >= height or\
            current_row + margin >= width:
        return False
    return True


def mult(i, j, margin, image, kernel):
    """multuply kernel to matrix"""
    sum = 0
    kerenl_row = 0
    kerenl_col = 0
    def_val = image[i][j]
    for r in range(i-margin, i+margin+1):
        kerenl_col = 0
        for c in range(j-margin, j+margin+1):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                sum += def_val*kernel[kerenl_row][kerenl_col]
            else:
                sum += image[r][c] * kernel[kerenl_row][kerenl_col]
            kerenl_col += 1
        kerenl_row += 1
    return sum


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    image_height = len(image)
    image_width = len(image[0])
    kernel_size = len(kernel)
    margin = kernel_size // 2
    img_kernel = []
    for i in range(image_height):
        row_kernel = []
        for j in range(image_width):
            if in_bounds(image_width, image_height, i, j, margin):
                sum = mult(i, j, margin, image, kernel)
                row_kernel.append(check_kerenel_value(sum))
            else:
                sum = mult(i, j, margin, image, kernel)
                row_kernel.append(check_kerenel_value(sum))
        img_kernel.append(row_kernel)
    return img_kernel


def check_kerenel_value(value):
    """making the kernel value round and between 0 to 255"""
    if value > 255:
        return 255
    if value < 0:
        return 0
    return round(value)


print(apply_kernel([[0, 1, 2, 0, 1], [1, 2, 2, 0, 0], [0, 1, 2, 1, 0], [
    0, 2, 1, 1, 0], [0, 0, 1, 0, 2]], [[0, 0, 0], [1, -1, 0], [1, 1, -1]]))


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    ...


def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    ...


def rotate_90(image: Image, direction: str) -> Image:
    ...


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    ...


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    ...


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    ...


if __name__ == '__main__':
    ...
