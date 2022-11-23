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
import math
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
    numer_of_channels = len(channels)
    length_of_rows = len(channels[0][0])
    number_of_rows = len(channels[0])
    for k in range(number_of_rows):
        row = []
        for j in range(length_of_rows):
            pixel = []
            for i in range(numer_of_channels):
                pixel.append(channels[i][k][j])
            row.append(pixel)
        colored_image.append(row)
    return colored_image


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


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> \
        SingleChannelImage:
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


def finding_neighbors(image, y, x):
    """finding the neighbors pixels relative to y,x position"""
    # Adjust the values of a the left upper pixel according to x,y
    if int(y) == len(image)-1 and int(x) == len(image[0])-1:
        a = [int(y)-1, int(x)-1]
    elif int(x) == len(image[0])-1:
        a = [int(y), int(x)-1]
    elif int(y) == len(image)-1:
        a = [int(y)-1, int(x)]
    else:
        a = [int(y), int(x)]
    # sest other neighbors according to the location of a
    b = [a[0]+1, a[1]]
    c = [a[0], a[1]+1]
    d = [a[0]+1, a[1]+1]
    return a, b, c, d


def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) \
        -> int:
    """Return the bilinear_interpolation of pixel in his relative location in image"""
    # setting the neighbors
    a, b, c, d = finding_neighbors(image, y, x)
    delta_y = (y-a[0])  # calculating delta y
    delta_x = (x-a[1])  # calculating delta x
    # calculating accoeding to the formula
    inter = image[a[0]][a[1]]*(1-delta_x)*(1-delta_y)+image[b[0]][b[1]]*delta_y*(1-delta_x) +\
        image[c[0]][c[1]]*delta_x*(1-delta_y) + \
        image[d[0]][d[1]]*delta_x*delta_y
    # returned rounded value
    return round(inter)


def relative_position(i, j, new_width, new_height, image):
    """get the position in the new image and return the relative position in the source"""
    y = (i / (new_height - 1))*(len(image)-1)
    x = (j / (new_width - 1))*(len(image[0])-1)
    return y, x


def resize(image: SingleChannelImage, new_height: int, new_width: int)\
        -> SingleChannelImage:
    """scale the image to new height x new width dimensions"""
    bigger_picture = []
    # Creating each row of the new image
    for i in range(new_height):
        bigger_row = []
        # creating the new pixels and adds the to the row
        for j in range(new_width):
            # calculating relative position
            y, x = relative_position(i, j, new_width, new_height, image)
            # adding the new pixel to the row
            bigger_row.append(bilinear_interpolation(image, y, x))
            # claculates according to bilinear interpolation formula
        bigger_picture.append(bigger_row)
    return bigger_picture


def rotate_right(image: Image) -> Image:
    """Rotate image to the right"""
    rows = len(image)
    cols = len(image[0])
    res = []
    for i in range(cols):

        temp = []
        for j in range(rows):
            # inserting the appropiate value
            temp.append(image[j][i])
        # reverse  the row
        res.append(temp[::-1])
    return res


def rotate_left(image: Image):
    """rotate image to the left"""
    rows = len(image)
    cols = len(image[0])
    res = []
    for i in range(cols):
        temp = []
        for j in range(rows):
            temp.append(image[j][i])
        res.append(temp)
    return res[::-1]


def rotate_90(image: Image, direction: str) -> Image:
    if direction == 'R':
        rotate = rotate_right(image)
    elif direction == 'L':
        rotate = rotate_left(image)
    return rotate


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    blur = apply_kernel(image, blur_kernel(blur_size))
    return


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    quantize_image = []
    for i in range(len(image)):
        quantize_row = []
        for j in range(len(image[0])):
            quantize_pixel = round(math.floor(
                image[i][j]*(N/256))*((255)/(N-1)))
            quantize_row.append(quantize_pixel)
        quantize_image.append(quantize_row)
    return quantize_image


print(quantize([[0, 50, 100], [150, 200, 250]], 8))


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    ...


if __name__ == '__main__':
    ...
