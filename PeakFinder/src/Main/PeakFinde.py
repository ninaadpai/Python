'''
Created on Feb 9, 2015

@author: ninaad
'''
import time
time1=time.time()
peaks=[4,1,7,2,8,2,3,7,9,11,5,6]
newpeaks=[]
for i in range(0,len(peaks)-1):
    
    if peaks[i]>=peaks[i-i] and peaks[i]>=peaks[i+1]:
        print (peaks[i])
   
if peaks[len(peaks)-1]>=peaks[len(peaks)-2]:
        print (peaks[len(peaks)-1])


time2=time.time()
print (time2-time1)