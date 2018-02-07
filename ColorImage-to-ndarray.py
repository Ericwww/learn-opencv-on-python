# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2
# 主函数
if __name__ == "__main__":
    if len(sys.argv) > 1:
        image = cv2.imread(sys.argv[1])
    else:
        print "Usge:python imgToArray.py imageFile"
    b=image[:,:,0]
    g=image[:,:,1]
    r=image[:,:,2]
    cv2.imshow("b", b)
    cv2.imshow("g", g)
    cv2.imshow("r", r)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
