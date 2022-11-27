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
import copy
import sys
##############################################################################
#                                  Functions                                 #
##############################################################################


def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """Get a 3 channel image and return matrix include 3 one channel images"""
    img_lst = []
    if len(image) == 0 or len(image[0]) == 0 or len(image[0][0]) == 0:
        return [[[]]]
    i = 0
    # for every channel the function creates a channel table
    while i < len(image[0][0]):
        channel_table = []
        for row in image:
            row_channel = []
            for pixel in row:
                # for each row in the current pixel we will add the pixel to the
                # appropiate channel
                row_channel.append(pixel[i])
            # after each row we wiil add it to the channel table
            channel_table.append(row_channel)
        # moving to the next channel
        i += 1
        # adding the channel table to the list of channels
        img_lst.append(channel_table)
    return img_lst


def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    "Take a list of one channel images and combine it to one channle"
    colored_image = []
    # number of channels equal to the len of the
    numer_of_channels = len(channels)
    # channel list
    # the number of pixel in each row in the
    length_of_rows = len(channels[0][0])
    # colurful image equals to the number of elements in a row in one channel
    # row
    number_of_rows = len(channels[0])  # number of rows equal to the number of
    # columns in the input
    # going over the row and adding pixel from
    for k in range(number_of_rows):
        row = []
        for j in range(length_of_rows):
            pixel = []
            for i in range(numer_of_channels):
                # adding the apporopiate color the the pixel, we
                # iretating in a vertical way on each column of the chnnels list
                # every columns equal to a new pixel in the colorful image
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


def mult(i, j, margin, image, kernel):
    """multuply kernel to matrix"""
    sum = 0
    kerenl_row = 0
    kerenl_col = 0
    def_val = image[i][j]
    # iritating over the size of the kernel where i,j is the center element
    for r in range(i-margin, i+margin+1):
        kerenl_col = 0
        for c in range(j-margin, j+margin+1):
            # if an image elment is out of bounds we will multiply the
            # appropiate kenel value with the center value
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                sum += def_val*kernel[kerenl_row][kerenl_col]
            else:
                # if an image elment is in bounds we will multiply the
                # appropiate kenel value with the the value from the
                # image
                sum += image[r][c] * kernel[kerenl_row][kerenl_col]
            kerenl_col += 1
        kerenl_row += 1
    return sum


def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> \
        SingleChannelImage:
    """return an image after applying a kernel matrix on it"""
    image_height = len(image)
    image_width = len(image[0])
    kernel_size = len(kernel)
    margin = kernel_size // 2
    img_kernel = []
    # iritating over the matrix
    for i in range(image_height):
        row_kernel = []
        for j in range(image_width):
            # calculates the new value and add it ccording to the demands
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
    # Adjust the values of a the corner pixels according to x,y
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
            # transpose the matrix
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
            # transpose the matrix
            temp.append(image[j][i])
        res.append(temp)
        # reverse the whole matrix
    return res[::-1]


def rotate_90(image: Image, direction: str) -> Image:
    if direction == 'R':
        rotate = rotate_right(image)
    elif direction == 'L':
        rotate = rotate_left(image)
    return rotate


def avg_calc(i, j, margin, image):
    """return tha average value of kxk matrix to
    neighborhood of a given elemnt"""
    sum = 0
    count = 0
    def_val = image[i][j]
    for r in range(i-margin, i+margin+1):
        for c in range(j-margin, j+margin+1):
            # checking if value is in bounds if not adding the center value
            # else adding the appropiate value and counting the number of
            # elements anyway
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                sum += def_val
                count += 1
            else:
                sum += image[r][c]
                count += 1
    return sum/count


def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float)\
        -> SingleChannelImage:
    # making the image blur according the kernel size
    blur = apply_kernel(image, blur_kernel(blur_size))
    margin = block_size // 2
    edges = []
    height = len(image)
    width = len(image[0])
    for i in range(height):
        edges_row = []
        for j in range(width):
            # for each pixel we will calculate the threshold , if the
            # current pixel is lower the thrshold we will color it black(0)
            # else we will color it white(255)
            threshold = avg_calc(i, j, margin, blur) - c
            if blur[i][j] < threshold:
                edges_row.append(0)
            else:
                edges_row.append(255)

        edges.append(edges_row)
    return edges


def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    quantize_image = []
    """return a quantize image according to the formula"""
    for i in range(len(image)):
        quantize_row = []  # creating new line according to the lines in
        # the originial image
        for j in range(len(image[0])):
            quantize_pixel = round(math.floor(
                image[i][j]*(N/256))*((255)/(N-1)))  # calculate the new value of the pixel
            # adding the new pixel to the row
            quantize_row.append(quantize_pixel)
        quantize_image.append(quantize_row)  # adding the row to the image
    return quantize_image


def quantize_colored_image(image: ColoredImage, N: int) -> ColoredImage:
    """makinhg quantize to colored image"""
    image_copy = copy.deepcopy(image)  # creating deep copy of the image
    channels = separate_channels(image_copy)  # seperate the channels
    new_image = []
    # for each channel we will apply quantize and the combine the channels together
    for channel in channels:
        new_channel = quantize(channel, N)
        new_image.append(new_channel)
    return combine_channels(new_image)


def activate_kernel(new_image, user_input, colorful):
    """checks the input of the user to the kernel size and 
    runs kernel for one channel and multy channels"""
    if not user_input.isnumeric():
        return None
    elif int(user_input) % 2 == 0:
        return None
    user_input = int(user_input)
    if not colorful:
        return apply_kernel(new_image, blur_kernel(user_input))
    else:
        channels = separate_channels(new_image)
        table = []
        for channel in channels:
            table.append(apply_kernel(channel, blur_kernel(user_input)))
    return combine_channels(table)


def activate_resize(height, width, image):
    """avtivate resize to multi channel image"""
    channels = separate_channels(image)
    table = []
    for channel in channels:
        table.append(resize(channel, height, width))
    return combine_channels(table)


if __name__ == '__main__':
    """This pare of the program running the editor"""
    # checking if the number of arguments is valid (2)
    if len(sys.argv) != 2:
        print("usage:python3 image_editor.py <image_path>")

    else:
        image_path = sys.argv[1]  # takes the argument to image path
        image = load_image(image_path)  # load the image
        new_image = copy.deepcopy(image)  # creating a new copy of the image
        message = "Available options in the editor(how to call): \n\
convert picture to grayscale(1)\n\
making the picture blur(2)\nchanging the size of the image(3)\n\
rotating the picture left or right in 90 degrees(4)\n\
create an image with the edges of the original image(5)\n\
make the image quantize(6)\n\
show the image(7)\n\
stop the editor and save changes(8\n"  # an outpus message
        # running the editor
        while True:
            # checks if image is colorful
            if type(new_image[0][0]) == list:
                colorful = True
            else:
                colorful = False
            # prompt the uset to choose type of function to run
            user_input = input("\n"+message+"please choose an \
edit you would like to do:")
            # if answer does not exist prompt to ask again
            while user_input not in "12345678":  # checks if the user input is
                # valid if not asks for anothe input
                error_message = "You choosed a wrong number or entered an invalid \
input\n\nAvailable \
options in the editor(how to call): \nconvert picture to grayscale(1)\n\
making the picture blur(2)\nchanging the size of the image(3)\n\
rotating the picture left or right in 90 degrees(4)\n\
create an image with the edges of the original image(5)\n\
make the image quantize(6)\n\
show the image(7)\n\
stop the editor and save changes(8)\n"
                user_input = input(error_message+"please choose an \
edit you would like to do:")

            # activating the editor for grayscale
            if user_input == '1':
                if not colorful:
                    print("image is alrady in grayscale")
                else:
                    new_image = RGB2grayscale(new_image)
            # acitvating kernel
            if user_input == '2':
                kernel_size = input(
                    "Enter the size of the kernel you want to blur with: ")
                if activate_kernel(new_image, kernel_size, colorful) is None:
                    print("please enter a valid value")
                else:
                    new_image = activate_kernel(
                        new_image, kernel_size, colorful)
            # activate resize
            if user_input == '3':
                new_dim = input(
                    "Enter the dimensions of the new image:(height,width) ")

                dimension = new_dim.split(",")
                if len(dimension) != 2:
                    print("invalid format")
                elif not dimension[0].isnumeric() or int(dimension[0]) <= 1:
                    print("invalid format")
                elif not dimension[1].isnumeric() or len(dimension) > 2 \
                        or int(dimension[1]) <= 1:
                    print("invalid format")
                else:

                    if not colorful:
                        new_image = resize(new_image, int(
                            dimension[0]), int(dimension[1]))

                    else:
                        new_image = activate_resize(
                            int(dimension[0]), int(dimension[1]), new_image)

            # activate rotate
            if user_input == '4':
                direction = input(
                    "choose a direction to rotate the image(R/L)")
                if direction != 'L' and direction != 'R':
                    print("invalid format")
                elif direction == 'L':
                    new_image = rotate_90(new_image, 'L')
                elif direction == 'R':
                    new_image = rotate_90(new_image, 'R')
            # activate get edges
            if user_input == '5':
                sizes = input(
                    "enter blur size,block size and c:(sizes are odd)")
                inputs = sizes.split(',')
                if len(inputs) != 3:
                    print("invalid format")
                elif not inputs[0].isnumeric():
                    print("invalid format")
                elif not inputs[1].isnumeric():
                    print("invalid format")
                elif not inputs[2].replace(".", "", 1).isdigit():
                    print("invalid format")
                else:
                    blur_size = int(inputs[0])
                    block_size = int(inputs[1])
                    c = float(inputs[2])
                    if blur_size < 1 or blur_size % 2 == 0 or \
                            block_size < 1 or block_size % 2 == 0 or \
                            c < 0:
                        print("invalid format")
                    else:
                        if not colorful:
                            new_image = get_edges(
                                new_image, blur_size, block_size, c)

                        else:
                            new_image = get_edges(
                                RGB2grayscale(new_image), blur_size,
                                block_size, c)

            # activate quantize
            if user_input == '6':
                colors = input(
                    "enter the number of channels you want to quantize")
                if not colors.isnumeric():
                    print("invalid input")
                elif int(colors) <= 1:
                    print("invalid input")
                else:
                    if colorful:
                        new_image = quantize_colored_image(
                            new_image, int(colors))

                    else:
                        new_image = quantize(new_image, int(colors))

            # shows the image
            if user_input == '7':
                show_image(new_image)
            # finish running
            if user_input == '8':
                path = input("enter a path to save result")
                save_image(new_image, path)
                break
