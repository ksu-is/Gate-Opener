# lets get started
import random
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.polynomial import poly
import easyocr




cam = cv2.VideoCapture(0)
lst = [1234, 4321, 0000, 5678]


def Camera_function():

    img_counter = 0

    while True:
        ret,frame = cam.read()

        if not ret:
            print("failed to grab frame")
            break

        cv2.imshow("test",frame)

        k = cv2.waitKey(1)

        if k%256 == 27:
            print("Escape hit, closing the app")
            break
        
        elif k%256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print("screenshot taken")
            img_counter+=1


    cam.release()

Camera_function()






def scan_function():

    pic_scan1 = ("C:\\Users\\tkcol\\OneDrive\\Desktop\\Gate-Opener\\opencv_frame_0.png")
    img_mpl = plt.imread(pic_scan1)


    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('off')
    ax.imshow(img_mpl)
    plt.show()

    word_screen = easyocr.Reader(['en'], gpu=False)
    result = word_screen.readtext(pic_scan1)
    print(result)
    print(result[0][1])

    lst.append(result[0][1])
    print("welcome!")


scan_function()
     



def entry_code():
    num = ""
    holder = "Working! Welcome"
    while True:
        num = int(input("Please enter your four digit code: "))
        if int(num) in lst:
            return holder #people who already have acess to gate
            
        elif num not in lst:
            no_num = input("Sorry that code is not in our system\n Would you like to gain acess to this lot? (yes or no): ")
            if no_num == "yes":
                no_num_sub = input("Would you like a subscription or one time acess? (sub or one): ")
                if no_num_sub == "sub":
                    sub_num = random.randint(1000,9999)
                    lst.append(sub_num)
                    return "Your new code is", sub_num ,"\n Thank you for your purchase!" # need to append the random number
                
            
                elif no_num_sub == "one":
                    return "Welcome!" # this where the gate would open up
            elif no_num == "no":
                return "OK, Thank you for your time!"
