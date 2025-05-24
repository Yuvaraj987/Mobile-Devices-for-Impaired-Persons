import cv2
import numpy as np
import pyttsx3


engine = pyttsx3.init()


def detect_object(frame):
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    edges = cv2.Canny(gray, 50, 150)
    
   
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    
  
    if lines is not None:
      
        for line in lines:
          
            rho, theta = line[0]
            
           
            angle = theta * 180/np.pi
            
            
            if angle > 45 and angle < 135:
                
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                
                
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                
                if x1 < x2:
                    engine.say("Object on your right")
                else:
                    engine.say("Object on your left")
                    
                engine.runAndWait()
                
    cv2.imshow("Object Detection", frame)
    
    cv2.waitKey(1)

cap = cv2.VideoCapture(0)


while True:
    
    ret, frame = cap.read()
    

    if ret:
    
        detect_object(frame)
        
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()