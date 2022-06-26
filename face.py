# Usage:
# python3 script.py --input original.png --output modified.png
# Based on: https://github.com/mostafaGwely/Structural-Similarity-Index-SSIM-

# 1. Import the necessary packages-Gerekli resimleri yükle

from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 2. Resimleri argüman olarak
#girmek istediğinizde yorum olrak eklediğim bu kısmı kullanabilirsiniz.
#ap = argparse.ArgumentParser()
#ap.add_argument("-f", "--first", required=True, help="Directory of the image that will be compared")
#ap.add_argument("-s", "--second", required=True, help="Directory of the image that will be used to compare")
#args = vars(ap.parse_args())

# 3. 2 resmi yükle
# (python face.py --ilk resimler/k1.png	--ikinci resimler/k3_02.png
#imageA = cv2.imread(args["first"])
#imageB = cv2.imread(args["second"])
imageA = cv2.imread("im1.jpg")
imageB = cv2.imread("im2.jpg")
# 4. Convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5.  İkisi arasındaki Yapısal Benzerlik İndeksini (SSIM) hesaplayın
# images, fark görüntüsünün döndürülmesini sağlar
#(score, diff) = compare_ssim(grayA, grayB, full=True)
(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

# 6. benzerlik skorunu yazdırma
# isterseniz farklılık (diff) da kullanabiliriz.
print("SSIM: {}".format(score))

#plt.imshow(imageA, cmap=plt.cm.gray)
#plt.imshow(imageB, cmap=plt.cm.gray)
#plt.axis("off")
#plt.show()
# 1.resim
cv2.imshow('before', imageA)
# 2.resim
cv2.imshow('after', imageB)
# Burada da resimdeki farklılıkları gösterme
cv2.imshow('diff', diff)
cv2.waitKey()


#veya konsolda görmek için
fig = plt.figure("Images")
images = ("Original", imageA), ("Kalite Hatası ", imageB), ("Hatalı noktalar ", diff)

#plt.imshow(imageA, cmap=plt.cm.gray)
#plt.imshow(imageB, cmap=plt.cm.gray)
#plt.imshow(diff, cmap=plt.cm.gray)
#plt.axis("off")
#plt.show()

# loop over the images

for (i, (name, image)) in enumerate(images):
        # show the image
        ax = fig.add_subplot(1, 3, i + 1)
        ax.set_title(name)
        plt.imshow(image, cmap=plt.cm.gray)
        plt.axis("off")
    # show the figure
plt.show()
