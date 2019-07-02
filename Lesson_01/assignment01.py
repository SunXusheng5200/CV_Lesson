import numpy as np
import cv2
import random
from matplotlib import pyplot as plt

# image crop
def crop(img, height_co, width_co):
    img_crop = img[0:height_co, 0:width_co]
    return img_crop

# image rotation
def rotation(img, angle, scale=1.0):
    M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), angle, scale=1.0)
    img_rotate = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return img_rotate

def colorShift(img, scale):
    B, G, R = cv2.split(img)
    b_rand = random.randint(-scale, scale)

    if b_rand == 0:
        pass

    elif b_rand > 0:
        lim = 255 - b_rand
        B[B > lim] = 255
        B[B <= lim] = (b_rand + B[B <= lim]).astype(img.dtype)

    elif b_rand < 0:
        lim = 0 - b_rand
        B[B < lim] = 0
        B[B >= lim] = (b_rand + B[B >= lim]).astype(img.dtype)

    g_rand = random.randint(-scale, scale)

    if g_rand == 0:
        pass

    elif g_rand > 0:
        lim = 255 - g_rand
        G[G > lim] = 255
        G[G <= lim] = (g_rand + G[G <= lim]).astype(img.dtype)

    elif g_rand < 0:
        lim = 0 - g_rand
        G[G < lim] = 0
        G[G >= lim] = (g_rand + G[G >= lim]).astype(img.dtype)

    r_rand = random.randint(-scale, scale)

    if r_rand == 0:
        pass

    elif r_rand > 0:
        lim = 255 - r_rand
        R[R > lim] = 255
        R[R <= lim] = (r_rand + R[R <= lim]).astype(img.dtype)

    elif r_rand < 0:
        lim = 0 - r_rand
        R[R < lim] = 0
        R[R >= lim] = (r_rand + R[R >= lim]).astype(img.dtype)

    img_merge = cv2.merge((B, G, R))

    return img_merge

def random_warp(img, row, col,random_margin):
    height, width, channels = img.shape

    x1 = random.randint(-random_margin, random_margin)
    y1 = random.randint(-random_margin, random_margin)
    x2 = random.randint(width - random_margin - 1, width - 1)
    y2 = random.randint(-random_margin, random_margin)
    x3 = random.randint(width - random_margin - 1, width - 1)
    y3 = random.randint(height - random_margin - 1, height - 1)
    x4 = random.randint(-random_margin, random_margin)
    y4 = random.randint(height - random_margin - 1, height - 1)

    dx1 = random.randint(-random_margin, random_margin)
    dy1 = random.randint(-random_margin, random_margin)
    dx2 = random.randint(width - random_margin - 1, width - 1)
    dy2 = random.randint(-random_margin, random_margin)
    dx3 = random.randint(width - random_margin - 1, width - 1)
    dy3 = random.randint(height - random_margin - 1, height - 1)
    dx4 = random.randint(-random_margin, random_margin)
    dy4 = random.randint(height - random_margin - 1, height - 1)

    pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
    M_warp = cv2.getPerspectiveTransform(pts1, pts2)
    img_warp = cv2.warpPerspective(img, M_warp, (width, height))
    return M_warp, img_warp

def main():
    img = cv2.imread(input("Please input your path of the image: "))
    # img = cv2.imread('D:\sunxusheng\my_lesson\lena.jpg')
    img_crop = crop(img, 200, 200)
    img_rotation = rotation(img_crop, angle=30, scale=1.0)
    img_ColorShift = colorShift(img_rotation, scale=50)
    rows, cols, ch = img.shape
    M_warp, img_warp = random_warp(img_ColorShift, img_ColorShift[0], img_ColorShift[1], random_margin=60)
    cv2.imshow('img_warp', img_warp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()