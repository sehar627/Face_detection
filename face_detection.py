import cv2

#load the pre-trained Haar Cascade classifier for face detection

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

colormap=None  # Initialize colormap variable (not used in this snippet)

while True:
    ret,frame=cap.read()
    if not ret:
        print("The camera is not accessible")
        exit()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale for face detection

    #Detect faces in the grayscale frame using the Haar Cascade classifier

    faces=face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  # Draw rectangles around detected faces

    cv2.putText(frame,"No.of face detected: "+str(len(faces)),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,0),2)

    if colormap is None:
        display_frame=frame

    else:
        display_frame=cv2.applyColorMap(frame,colormap) 
     # Apply colormap if specified

    cv2.imshow("Seflie Camera", display_frame)

    key=cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('c'):
        colormap=cv2.COLORMAP_DEEPGREEN  # Change the colormap to DEEPGREEN when 'c' is pressed

    elif key==ord('d'):
        colormap=cv2.COLORMAP_MAGMA  # Change the colormap to MAGMA when 'd' is pressed

    elif key==ord('e'):
        colormap=cv2.COLORMAP_OCEAN  # Change the colormap to OCEAN when 'e' is pressed

    elif key==ord('f'):
        colormap=cv2.COLORMAP_PINK  # Change the colormap to PINK when 'f' is pressed

    elif key==ord('s'):
        cv2.imwrite("myimage.png",display_frame)  # Save the current frame as an image when 's' is pressed

    elif key==ord('1'):
        colormap=cv2.COLORMAP_BONE  # Change the colormap to BONE when '1' is pressed


    
cap.release()
cv2.destroyAllWindow()