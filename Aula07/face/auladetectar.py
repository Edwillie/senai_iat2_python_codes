import cv2
detectar_rosto = cv2.CascadeClassifier('c:\\Temp\\TurmaIA\\senai_iat2_python_codes\\Aula07\\face\\rosto.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detectar_rosto.detectMultiScale(gray, \
                                            scaleFactor=1.1,\
                                            minNeighbors=5,\
                                            minSize=(30,30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 2)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()