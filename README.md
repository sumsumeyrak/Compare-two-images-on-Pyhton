

# 1. Gerekli kütüphaneleri yülemeyi unutmayın
from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import numpy as np
import cv2
import matplotlib.pyplot as plt
# 2. Resimlerin yükleyin.Burada resimleri alırken dosya dizininizin altına ekleyip resme tıklayıp kopt path diyebilirsiniz.
imageA = cv2.imread("im1.jpg")
imageB = cv2.imread("im2.jpg")
# 4. Resimleri gri arka plana alma
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# 5.  İkisi arasındaki Yapısal Benzerlik İndeksini (SSIM) hesaplayın
# images, fark görüntüsünün döndürülmesini sağlar
#(score, diff) = compare_ssim(grayA, grayB, full=True)
(score, diff) = ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

# 6. benzerlik skorunu yazdırma isterseniz farklılık (diff) da kullanabiliriz. (print("DSIM: {}".format(diff))  )
print("SSIM: {}".format(score))  
