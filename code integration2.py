from tkinter import *
import os
import cv2
import time
import pyttsx3 as lapvoice
import speech_recognition as sr
import pywhatkit as pk
def voice():
    r = sr.Recognizer()
    with sr.Microphone() as mymic:
       audio = r.record(mymic,duration=5)
       text = r.recognize_google(audio)
       print(text)
       if 'instance' in text:
           lapvoice.speak("Launching EC2 Instance")
           os.system("aws ec2 run-instances --image-id ami-057752b3f1d6c4d6c --instance-type t2.micro")
           os.system("start msedge https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")
           time.sleep(3)
       elif 'docker' in text:
           lapvoice.speak("Opening Docker Containerisation System")
           lapvoice.speak("What docker commands do you want to run")
           os.system("start chrome 43.204.232.236:8080")
       elif 'message' in text:
           lapvoice.speak("Sending Whatsapp message, no need for curiosity he doesnt have any girl chats in his whatsapp")
           phone='7093912699'
           num = "+91"+phone
           message = "Message sent successfully"
           pk.sendwhatmsg_instantly(num,message,15,True,2)
       elif 'linux' in text:
           lapvoice.speak("What linux commands do you want to run")
           os.system("start chrome http://43.204.232.236/fine.html")
       elif 'big' in text:
           lapvoice.speak("Lets get into our supercomputer")
           os.system("start chrome https://13.126.229.133:4200/")
       elif 'filter' in text:
           s = sr.Recognizer()
           with sr.Microphone() as mymic1:
              lapvoice.speak("What type of filter do you want to use? Number one blur the background, Number two cartoonify the photo,Number three extra feature find the distance between your face and the screen")
              audio1 = s.record(mymic1,duration=5)
              text1 = s.recognize_google(audio1)
              print(text1)
              if 'blur' in text1:
                cap=cv2.VideoCapture(0)
                lapvoice.speak("Blurring the background")
                status,photo=cap.read()
                faceModel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                myCoordinates=faceModel.detectMultiScale(photo)
                x1=myCoordinates[0][0]
                y1=myCoordinates[0][1]
                x2=x1+myCoordinates[0][2]
                y2=y1+myCoordinates[0][3]
                newphoto=photo.copy()
                cv2.rectangle(newphoto,(x1,y1),(x2,y2),[0,255,0],5)
                blurred_image=newphoto.copy()
                blurred_image = cv2.GaussianBlur(blurred_image, (15, 15), 20)
                final_image=blurred_image.copy()
                final_image[y1:y2, x1:x2] = newphoto[y1:y2, x1:x2]
                cv2.imshow("myphoto",final_image)
                cap.release()
                if cv2.waitKey()==13:
                    cv2.destroyAllWindows()
                
              elif 'cartoon' in text1:
                  cap=cv2.VideoCapture(0)
                  status,photo=cap.read()
                  img = photo
                  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                  gray = cv2.medianBlur(gray, 5)
                  edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
                  color = cv2.bilateralFilter(img, 9, 300, 300)
                  cartoon = cv2.bitwise_and(color, color, mask=edges)
                  cv2.imshow("Cartoon", cartoon)
                  cv2.waitKey(0)
                  cv2.destroyAllWindows()
              elif 'distance' in text1:
                  cap=cv2.VideoCapture(0)
                  status,photo=cap.read()
                  faceModel=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                  myCoordinates=faceModel.detectMultiScale(photo)
                  x1=myCoordinates[0][0]
                  y1=myCoordinates[0][1]
                  x2=myCoordinates[0][2]+x1
                  y2=myCoordinates[0][3]+y1
                  width=myCoordinates[0][3]
                  object_width=20
                  focal_length=500
                  object_width_pixels = photo[y1:y2,x1:x2].shape[1]
                  distance= (object_width * focal_length) /object_width_pixels
                  print(f" Distance of Object from camera is {distance} cm")
    
                
                
              

            
    

window = Tk()
window.title("MY PROJECT")
window.colormapwindows()
label = Label(window,text="Future Forecasters",font=("Arial Bold",30),fg="blue",bg="white",anchor="center")
bt1 = Button(text="Voice Command",command=voice)
bt1.pack()
label.pack()
window.mainloop()