#tw live可搜尋台灣即時影像：https://trafficvideo2.tainan.gov.tw/b596d902

from ultralytics import YOLO
import cv2,time
#設定視窗名稱及型態
cv2.namedWindow('YOLOv8', cv2.WINDOW_NORMAL)

target=0 
model = YOLO('yolov8m.pt')  # n,s,m,l,x 五種大小

names=model.names
print(names)

cap=cv2.VideoCapture(target)

while 1:
    st=time.time()  
    r,frame = cap.read()
    if r==False:
        break
    results = model(frame,verbose = False)
    frame= results[0].plot()
    et=time.time()
   
    FPS=int(1/(et-st)) #評估時間

    cv2.putText(frame, 'FPS=' + str(FPS), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)
    cv2.imshow('YOLOv8', frame)
    key=cv2.waitKey(1)
    if key==27:
        break