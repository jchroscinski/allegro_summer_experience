from PIL import Image

def rotate_func(input_image):
    # Declaring RGB values of the wanted pixels
    white = (255,255,255)
    red = (255,0,0)

    # Loading image and converting to representation of RGB
    an_image = Image.open(input_image)#.convert('RGB')
    sequence_of_pixels = an_image.getdata()
    list_of_pixels = list(sequence_of_pixels)


    # Creating a list of RGB values for each pixel from top to bottom by rotating input image
    rot_image = an_image.rotate(90,expand=True) 
    sequence_of_rot_pixels = rot_image.getdata()
    list_of_rot_pixels = list(sequence_of_rot_pixels)

            
    # Declaring variables
    horizontal_w = 0
    horizontal_r = 0
    vertical_w = 0
    vertical_r = 0

    # Looking for any horizontal white to red template
    for x in range(0,len(list_of_pixels)-6):
        if (list_of_pixels[x] == white and list_of_pixels[x+1] == white and list_of_pixels[x+2] == white and 
            list_of_pixels[x+3] == red and list_of_pixels[x+4] == red and list_of_pixels[x+5] == red):
            horizontal_w = 1                            

    # Looking for any horizontal red to white template
    for x in range(0,len(list_of_pixels)-6):
        if (list_of_pixels[x] == red and list_of_pixels[x+1] == red and list_of_pixels[x+2] == red and 
            list_of_pixels[x+3] == white and list_of_pixels[x+4] == white and list_of_pixels[x+5] == white):
            horizontal_r = 1           

    # Looking for any vertical white to red template
    for x in range(0,len(list_of_rot_pixels)-6):
        if (list_of_rot_pixels[x] == white and list_of_rot_pixels[x+1] == white and list_of_rot_pixels[x+2] == white and 
            list_of_rot_pixels[x+3] == red and list_of_rot_pixels[x+4] == red and list_of_rot_pixels[x+5] == red):
            vertical_w = 1                            

    # Looking for any vertical red to white template
    for x in range(0,len(list_of_rot_pixels)-6):
        if (list_of_rot_pixels[x] == red and list_of_rot_pixels[x+1] == red and list_of_rot_pixels[x+2] == red and 
            list_of_rot_pixels[x+3] == white and list_of_rot_pixels[x+4] == white and list_of_rot_pixels[x+5] == white):
            vertical_r = 1 


    # Deciding to use the appropriate operation
    sum_of_variables = horizontal_w + horizontal_r + vertical_w + vertical_r

    if sum_of_variables == 0:
        return (204, an_image)

    else:
        if sum_of_variables > 1:
            return (400, an_image)
        else:
            if vertical_w == 1:
                return (200, an_image)
            elif vertical_r == 1:
                return (200, an_image.rotate(180,expand=True))
            elif horizontal_w == 1:
                return (200, an_image.rotate(270,expand=True))
            elif horizontal_r == 1:
                return (200, an_image.rotate(90,expand=True))