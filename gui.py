#pip install opencv-contrib-python
#pip install PyQt5
#pip install opencv-contrib-python
#Diğer kitaplıklar vb. ile çakışmaları önlemek
# için en iyi uygulamanın sanal bir ortamda
# çalışmak olduğunu unutmayın .
import cv2
#pip install pyqtgraph
#pencere açıma denemesi-PyQt5
#from PyQt5.QtWidgets import QApplication, QMainWindow

#print(np.min(frame))
#print(np.max(frame)) #Bu iki satır sadece kamera tarafından
# kaydedilen maksimum ve minimum değerleri yazdırıyor.
# frameBunun bir numpy 2D dizisi olduğunu unutmayın .


#Kamera ile iletişimi başlatıyoruz.
#esc tuşuna basarsak kameradan çıkar
#space tuşuna basarsak kameradan görüntü alırız

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("frame yakalanamadı..")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27: # hangi klaveye tuşlarını kullanacağımzı buradan ayarlarız
        # ESC pressed
        print("Escape basıldı, kapatılıyor...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "img{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} resim kaydediliyor!".format(img_name))
        img_counter += 1

cam.release() #kamerayı serbest bırakıyoruz
cv2.destroyAllWindows()
