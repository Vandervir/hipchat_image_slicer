import math
import argparse
import os
from imgpy import Img


def crop(filename, crop_size):
    if not os.path.isfile(filename):
        print('FIle do not exists')
        return
    name, ext = filename.split(".")
    with Img(fp=filename) as im:
        print(im.width, im.height)
        for width in range(0, math.ceil(im.width / crop_size)):
            for height in range(0, math.ceil(im.height / crop_size)):
                with Img(fp=filename) as temp_im:
                    print(width * crop_size, height * crop_size)
                    temp_im.crop(box=(width * crop_size, height * crop_size, width * crop_size + crop_size,
                                      height * crop_size + crop_size))
                    temp_im.save(fp='output/{}{}{}.{}'.format(name, height, width, ext))


parser = argparse.ArgumentParser()
parser.add_argument("--image", help="image file")
parser.add_argument("--size", help="slice size", default=60)
args = parser.parse_args()
crop(args.image, int(args.size))
