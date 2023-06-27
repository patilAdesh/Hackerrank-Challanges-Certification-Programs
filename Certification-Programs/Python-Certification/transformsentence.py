#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    
    x = sentence.split()
    y = []
    z = ""
    
    for i in x:
        z += i[0]
        for j in range(0, len(i)-1):
            if(i[j].lower() < i[j+1].lower()):
                z += (i[j+1].upper())
            elif(i[j].lower() > i[j+1].lower()):
                z += (i[j+1].lower())
            else:
                z += i[j+1]
        y.append(z)
        z = ""
    res = ""
    
    for i in y:
        res = res + " " + i
    return res.strip()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
