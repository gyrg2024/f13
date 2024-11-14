#открытие изображения в openCV
#pip install opencv-pethon - установка библиотеки
import cv2

pig = cv2.imread(r"3.jpeg")
mode = 0
b,g,r = cv2.split(pig)
while True:
    if(mode == 0):
        cv2.imshow("3",pig)
    elif(mode == 1):
        cv2.imshow("1",r)
    elif(mode == 2):
        cv2.imshow("1",g)      
    elif(mode == 3):
        cv2.imshow("1",b)    
    key=cv2.waitKey(33)
    print(key)
    if (key== 27):
       break
    elif(key == 114):
        mode =1
    elif(key == 103):
        mode =2
    elif(key == 98):
        mode =3
    elif(key == 32):
        mode =0
cv2.destroyAllWindows()
