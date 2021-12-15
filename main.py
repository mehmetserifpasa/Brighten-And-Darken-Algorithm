import time
from PIL import Image



img = Image.open("image.jpg")
pixel = img.load()
width,height = img.size


def Process(data, radius):
    global img
    global pixel
    global width,height

    data_x = data[0]
    data_y = data[1]
    data_r = radius

    location1 = (data_x - 1, data_y)
    location2 = (data_x - 1, data_y - 1)
    location3 = (data_x, data_y - 1)
    location4 = (data_x + 1, data_y - 1)
    location5 = (data_x + 1, data_y)
    location6 = (data_x + 1, data_y + 1)
    location7 = (data_x, data_y + 1)
    location8 = (data_x - 1, data_y + 1)
    location9 = (data_x, data_y)

    LOCATION_LIST = [location1, location2, location3,
                     location4, location5, location6,
                     location7, location8, location9]

    try:
        for loc_list in LOCATION_LIST:
            LOCATION_COLOR = pixel[loc_list[0], loc_list[1]]

            img.putpixel(
                (loc_list),
                (
                    int(LOCATION_COLOR[0] / data_r),
                    int(LOCATION_COLOR[1] / data_r),
                    int(LOCATION_COLOR[2] / data_r),
                )
            )
    except:
        pass


for x in range(width+1):
    for y in range(height+1):
        i = x * 3
        k = y * 3
        Process((i,k), 3)


img.show()
