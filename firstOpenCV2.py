# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 00:00:41 2018

@author: a9657
"""

import cv2
import sys

if __name__=="__main__":
    if len(sys.argv)>1:
        image=cv2.imread(sys.argv[1])
    else:
        print "Usge:python firstOpenCV3.py imagefile"
        
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()