import glob
import os

import cv2

'''
    This code takes a watermark png file,
    which needs to be white text on black background,
    and the photo that's going to be watermarked and
    then puts them on top of one another.
'''
# This part of the code takes the watermark png file and its dimensions.
watermark = cv2.imread('images/watermark.png')
watermark_h, watermark_w, _ = watermark.shape

# This part of the code takes the image png file and its dimensions.
images_path = glob.glob('images/pictures/*.*')

print('Adding watermarks')

for img_path in images_path:
    img = cv2.imread(img_path)
    img_h, img_w, _ = img.shape

    center_img_h = int(img_h / 2)
    center_img_w = int(img_w / 2)

    top_y = center_img_h - int(watermark_h / 2)
    left_x = center_img_w - int(watermark_w / 2)

    bottom_y = top_y + watermark_h
    right_x = left_x + watermark_w

    # cv2.circle(img, (left_x, top_y), 10, (0, 255, 0), -1)
    # cv2.circle(img, (right_x, bottom_y), 10, (0, 255, 0), -1)

    roi = img[top_y: bottom_y, left_x: right_x]

    result = cv2.addWeighted(roi, 1, watermark, 0.3, 0)
    img[top_y: bottom_y, left_x: right_x] = result

    filename = os.path.basename(img_path)
    print(f'Adding watermark to --> {filename}  ...')

    cv2.imwrite('images/watermarked/watermarked_' + filename, img)

print('Watermark added to all the images!')

# cv2.imshow('Watermark', watermark)
# cv2.imshow('Img', img)
# cv2.imshow('Roi', roi)
# cv2.imshow('Result', result)
# cv2.waitKey(0)

