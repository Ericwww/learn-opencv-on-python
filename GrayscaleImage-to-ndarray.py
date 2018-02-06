# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2
# 主函数
if __name__ == "__main__":
    if len(sys.argv) > 1:
        img = cv2.imread(sys.argv[1])
    else:
        print "Usge:python imgToArray.py imageFile"
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
