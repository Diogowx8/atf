import cv2


    camera = cv2.VideoCapture(0)
    car_cascade = cv2.CascadeClassifier("treinamento/cascade.xml")
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objetos = car_cascade.detectMultiScale(gray, 1.20 , 6)
        for (x, y, w, h) in objetos:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow("Camera", frame)
        k = cv2.waitKey(30)
        if k == 27:
            break

    cv2.destroyAllWindows()
    camera.release()