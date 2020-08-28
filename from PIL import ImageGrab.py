import cv2
import numpy as np
import os
import pyautogui

output = "video.avi"
img = pyautogui.screenshot()
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
#get info from img
height, width, channels = img.shape
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

while(True):
 try:
  img = pyautogui.screenshot()
  image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  out.write(image)
  #cv2.imshow("test", image)
  StopIteration(0.5)
 except KeyboardInterrupt:
  break

out.release()
cv2.destroyAllWindows()