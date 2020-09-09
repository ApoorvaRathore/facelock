import dlib
import cmake
import face_recognition as fr
import cv2
import vlc
import smtplib
#import face_recognition as fr
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import pyowm

owm = pyowm.OWM('fb55e8ac1711a0b5b3eabae65b32a603') #fb55e8ac1711a0b5b3eabae65b32a603 0eda0646e5abc58261f99346b3c98755
observation = owm.weather_at_place("Muzaffarpur,India")
w = observation.get_weather()
time=w.get_reference_time(timeformat='iso')
location=observation.get_location()


i=cv2.VideoCapture(0)
f=cv2.CascadeClassifier('C:/Users/hp/Desktop/Techienest/haarcascade_frontalface_default.xml')
player = vlc.MediaPlayer("C:/Users/hp/Downloads/WhatsApp Audio 2019-07-22 at 23.19.14.mpeg")
p=0


m_test=0
train_image=fr.load_image_file('C:/Users/hp/Downloads/008-2.jpg')
m_train=fr.face_encodings(train_image)[0]
i=cv2.VideoCapture(0)
p=0
while(1):
    
    return_value, img1 = i.read()
    #img1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    l=f.detectMultiScale(img1,1.3,7)
    print(l)
    if(len(l)>0 ):
        for (x,y,w,h) in l:     #x,y coordinates of top left corner
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),10)  #x+w,y+h coordinates of bottom right corner
            cv2.imshow("Video",img1)
            m_test=[]
            m_test=fr.face_encodings(img1)[0]
            x=fr.compare_faces([m_train],m_test)
            print(x[0])
            if(x[0]==True and p==0 ):
                 
                 print(x[0])
                 
                 #font = cv2.FONT_HERSHEY_SIMPLEX
                 #cv2.putText(img1,'Apoorva',(500,500), font, 4,(0,255,0),2,cv2.LINE_AA)
                 player.play()
                 
                 print("apoo")
                 
                 #os.system("cmd /c Taskmgr")
                 #p=1
            elif(x[0]==False ):
                player.pause()
                #msg="hey"
                
                return_value,im=i.read()
                cv2.imwrite('lol.png',im)

                def SendMail(imagefile):
                    img_data = open(imagefile, 'rb').read()
                    msg = MIMEMultipart()
                    msg['Subject'] = 'WARNING - REQUIRE ATTENTION '
                    msg['From'] = Mail  
                    msg['To'] = Mail

                    text = MIMEText(".....An intruder is trying to  unlock your device at LOCATION = Muzaffarpur, INDIA")
                    msg.attach(text)
                    image = MIMEImage(img_data, name=os.path.basename(imagefile))
                    msg.attach(image)

                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    s.ehlo()
                    s.starttls()
                    #s.ehlo()
                    s.login(mail id, password)
                    s.sendmail(from mail, to mail, msg.as_string())
                    print(" ....... MAIL IS SEND......")
                    s.quit()
    
                
                SendMail("lol.png")
    
                p=0
    
    elif(len(l)==0 ):
        player.pause()
        p=1
    """    p=0
        #z=cv2.waitKey(1)
    """
    z=cv2.waitKey(1)   
    if(z==ord('q')):
        player.stop()
        break    
"""

    elif(len(l)==0 and p==1 and x[0]==False ):
            #else:
               # font = cv2.FONT_HERSHEY_SIMPLEX
                
                print("apoorva")
                print("x[0] = ",x[0])
                print("p = ",p)
                print("len(l)",len(l))
                player.pause()
                
                #player.pause()
                msg="hey"
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()

                print("mail send reee")
                print("Quit")
                
                
                 
                #cv2.putText(img1,'Unknown',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
                p=0
                #cv2.label("Unknown")

    z=cv2.waitKey(1)
    if(z==ord('q')):
        player.stop()
        break

"""   
i.release()
cv2.destroyAllWindows()


