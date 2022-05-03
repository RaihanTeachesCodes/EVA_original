#https://www.naturalreaders.com/online/
# module imports

import matplotlib.pyplot as plt
import pandas as pd
from lib2to3.pgen2 import driver
from re import M
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui 
import time
from subprocess import check_output
from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage
import cv2
from cv2 import threshold
from matplotlib.pyplot import contour
import numpy as np
import math
from PIL import ImageGrab
import time
import math
import pyttsx3
import subprocess
import sys
import keytotext
from keytotext import pipeline
try:
    print("modules succeed")
except:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    modules = ["matplotlib", "pandas", "selenium", "pyautogui", "tkinter", "cv2", "pyttsx3" ]

    for modal in modules:
        try:
            install(modal)
        except:
            f"installation of {modal} fail"

class EVA():
    def __init__(self,):
        self.mission = False

    def image_resize(image):
        with open(image, 'r+b') as f:
            with Image.open(f) as image2:
                cover = resizeimage.resize_cover(image2, [200, 100])
                cover.save('photo_test.jpg', image2.format)

    def detect_object(self, image):  

        image = f"images/{image}"

        def show_img():
            print(object.get("1.0", "end-1c"))

        if self.mission:
            try:
                print("going mission tkinter")
                #tkinter opening
                root = Tk()
                root.title("Image Viewer")
                root.geometry("700x600")
                image_no_1 = ImageTk.PhotoImage(Image.open(image))
                List_images = [image_no_1]
                label = Label(image=image_no_1)
                label.grid(row=1, column=0, columnspan=3)

                button_exit = Button(root, text="Exit",
                                    command=root.quit)


                object = Text(root, height = 2,
                                width = 50,
                                bg = "light yellow")

                answer = object.get("1.0", "end-1c")

                show_button = Button(root, text="finish",
                                        command=lambda: show_img())

                show_button.grid(row=7, column=1)
                object.grid(row=7, column=0)
                button_exit.grid(row=5, column=1)


                root.mainloop()

            except:
                self.mission = False
            
            

        if self.mission == False:


            try:
                    
                PATH = "C:/Users/mathl/Downloads/raihan downloads/New folder/chromedriver.exe"
                driver = webdriver.Chrome(PATH)
                driver.get(image)
                body = driver.find_element_by_xpath("// *")
                action = ActionChains(driver)

                x_offset = 137.5
                y_offset = 443.5

                action.move_to_element_with_offset(body, x_offset, y_offset)
                action.context_click(body).perform() #Right clicks

                pyautogui.moveTo(586, 701)
                time.sleep(2)
                pyautogui.click()  
                time.sleep(7)
                pyautogui.moveTo(249, 244)
                time.sleep(5)
                pyautogui.click() 
                time.sleep(3)

                m = []
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    m.append(driver.current_url)

                driver.quit()
                print(m)

            except: 

                pass

    # EYES OPEN FUNCTION
    def open_eyes():
        print("loading")
        distance_list = []

        def stackImages(scale,imgArray):
            rows = len(imgArray)
            cols = len(imgArray[0])
            rowsAvailable = isinstance(imgArray[0], list)
            width = imgArray[0][0].shape[1]
            height = imgArray[0][0].shape[0]
            if rowsAvailable:
                for x in range ( 0, rows):
                    for y in range(0, cols):
                        if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                            imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                        else:
                            imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                        if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
                imageBlank = np.zeros((height, width, 3), np.uint8)
                hor = [imageBlank]*rows
                hor_con = [imageBlank]*rows
                for x in range(0, rows):
                    hor[x] = np.hstack(imgArray[x])
                ver = np.vstack(hor)
            else:
                for x in range(0, rows):
                    if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                        imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                    else:
                        imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
                    if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
                hor= np.hstack(imgArray)
                ver = hor
            return ver

        def getContours(img, imgCountour):

            
            # main_list: distance, 0:endpoint, 1:start point,

            countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


            for cnt in countours:
                area  = cv2.contourArea(cnt)
                if area> 500:
                    #cv2.drawContours(imgCountour, cnt, -1, (255, 0, 255), 3 )
                    peri = cv2.arcLength(cnt, True)
                    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)   
                    x , y, w, h = cv2.boundingRect(approx)
                    start_point = (x,y)
                    a = x + w
                    b = y + h
                    end_point = (x + w , y + h)
                    crosshair_point = (320, 240)
                    midpoint_object = (int(end_point[0])//2, int(end_point[1])//2 )
                    distance = int(math.sqrt( ((start_point[0]-crosshair_point[0])**2)+((start_point[1]-crosshair_point[1])**2) ) ) 
                    distance_list.append(distance)  
                    distance_list.sort()
                    focus_distance = distance_list[0]
                    
                    #print(x, y, a, b, distance,  focus_distance, distance_list[0:5] )
                    #cv2.rectangle(imgCountour, start_point, end_point, (0, 255, 0), 5)
                    minimum_focus = int(focus_distance - distance)
                    maximum_focus =  int(distance - focus_distance)

                    if distance > focus_distance:
                        popping = True
                        if popping:
                            distance_list.pop(0)
                        
                        if distance_list[0] == focus_distance:
                            popping = False
                            focus_distance = distance_list[0]

                    if x != 0 and y != 0 and a != 640 and b != 480 and distance == focus_distance and w > 50 and h > 50:
                        
                        cv2.rectangle(imgCountour, start_point, end_point, (0, 255, 0), 5)
                        #print(x, y, a, b, distance,  focus_distance, distance_list[0:5] )
                        #cv2.line(imgCountour, (320, 240), (x, y), (255, 0, 255), 5)


                        
                            
            
            cv2.drawContours(img, countours, -1, (0,255,0), 3)
                

        vid = cv2.VideoCapture(0)
        
        def empty():
            pass


        cv2.namedWindow("parameters")
        cv2.resizeWindow("parameters", 640, 240)
        cv2.createTrackbar("threshold1", "parameters", 150, 255, empty)
        cv2.createTrackbar("threshold2", "parameters", 150, 255, empty)

        img_counter = 0

        while(True):
            success, img = vid.read()
            imgcontour =img.copy()

            cv2.rectangle(imgcontour, (320, 240), (320, 240), (0,255,0), 5)

            #cv2.rectangle(imgcontour, (0,0), (640, 480), (0,255,0), 5)
            

            imgblur = cv2.GaussianBlur(img, (7,7), 1)
            imgGray = cv2.cvtColor(imgblur, cv2.COLOR_BGR2GRAY)

            threshold1 = cv2.getTrackbarPos("threshold1", "parameters")
            threshold2 = cv2.getTrackbarPos("threshold2", "parameters")

            imgcanny = cv2.Canny(imgGray, threshold1, threshold2)

            kernal = np.ones((5, 5))
            imgDil =cv2.dilate(imgcanny, kernal, iterations=1)

            getContours(imgDil, imgcontour )
            

            #imgStack = stackImages(0.8, ([img, imgcanny, imgGray], [imgDil, imgcontour, imgDil]))

            if not success:
                print("failed to grab frame")
                break
        
            cv2.imshow('frame', imgcontour)
            
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, imgcontour)
                print("{} written!".format(img_name))
                img_counter += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def profile():
        profile_df = pd.read_csv("game_asset/enviroment.csv")
        print(profile_df)

    def object_feelings_db():
        pass


    def speak(self, text, volumeE, rateE):

        self.engine = pyttsx3.init()

        """VOICE"""
        voices = self.engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        self.engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

        """ RATE"""
        rate = self.engine.getProperty('rate')   # getting details of current speaking rate
        self.engine.setProperty('rate', rateE)     # setting up new voice rate


        """VOLUME"""
        volume = self.engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
        self.engine.setProperty('volume',volumeE)    # setting up volume level  between 0 and 1


        self.engine.say(text)
        self.engine.runAndWait()
        #self.engine.stop()

    def text_generator(self, keywords ):
        nlp = pipeline("k2t-base")

        print( nlp([keywords][0]) )

    def keyword_generator():
        emotions = []
        objects = []
        object_feelings = []
        emotion_dictionary = {"objects":objects, "object_feelings": object_feelings, "emotional_state": emotions,} 
        pd.DataFrame(emotion_dictionary)
        pronouns = ["i", "you", "we", "they", "he", "she"]
        current_emotional_state = emotions[len(emotions) - 1]
        question = False
        if current_emotional_state == "curious":
            question = True

        
if __name__ == "__main__":

    eva = EVA()
    eva.text_generator(["chiken"])


