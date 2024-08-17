import os
import cv2

image = cv2.imread("numbers.jpg")

for digit in range( 10):
    os.makedirs(f"numbers/{digit}", exist_ok= True)


for i in range (10):
    for j in range(5):
        for k in range(100):
            y, x = j * 20, k * 20
            cropped_digit= image[y:y+20, x:x+20]
            filename = f"numbers/{i}/{i}{j}{k}.jpg"
            cv2.imwrite(filename, cropped_digit)

print("Cropped digits saved in separate directories")

