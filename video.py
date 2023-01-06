import cv2 as cv 
vid = cv.VideoCapture(0)
while True:
    isTrue, img = vid.read()
    cv.putText(img, 'Yasmeen Jalloud', (100, 225),
    cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Text in video', gray)
    resized_image = cv.resize(img, (800, 600))
    cv.imshow("Resize", resized_image)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
