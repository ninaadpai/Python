'''
Created on Jan 26, 2015

@author: ninaad
'''

import re

f=open('/Users/ninaad/Documents/workspace/DateChecker/src/sampletext.txt')
text=f.read()

#print re.findall(r'[a-z]{2,3} +[0-9]{2,}[a-z]{2,2} +[a-z]{2,2} +|January|February|March|April|May|June|July|August|September|October|November|December +19[0-9]',text)
date1=re.findall(r'(?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]) (?:[a-z]{2,2}) [A-Za-z]*(?:,) \d{4}',text)
date2=re.findall(r'(?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]) (?:[a-z]{2,2}) [A-Za-z]* \d{4}',text)
date3=re.findall(r'[A-Z][a-z]{2,10} (?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]{4,4})',text)
date4=re.findall(r'[A-Z][a-z]{2,10} (?:[0-3][0-9])(?:,)* \d{4}',text)
date5=re.findall(r"[A-Z][a-z]{2,10} (?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]{4,4}) [a-z]{2,2} \'\d{2}",text)
date7=re.findall(r'[A-Z][a-z]{2,10} [0-9]{1,2}[a-z]{2,2}, \d{4}',text)
date8=re.findall(r' (?:[1-9][a-z]{2,2}|[0-3][0-9]) (?:[a-z]{2,2}) [A-Za-z]*(?:,) \d{4}',text)
date9=re.findall(r' (?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]) (?:[a-z]{2,2}) [A-Za-z]* ',text)
date10=re.findall(r' (?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]) (?:[a-z]{2,2}) [A-Za-z]*(?:,) ',text)
date11=re.findall(r'[A-Z][a-z]{2,10} (?:[0-3][0-9][a-z]{2,2}|[0-3][0-9]{4,4}) [a-z]{1,10} (?:[a-z]{1,10}) \d{4}',text)
date12=re.findall(r'Labor Day| Thanksgiving Day| Day after Thanksgiving| Winter Holiday| Christmas Eve| Christmas Day| Day after Christmas| New Year\'s Day| Martin Luther King, Jr. Day| Memorial Day',text)

date=date1+date2+date3+date4+date5+date7+date8+date9+date10+date11+date12
#print date
for d in date:
    print d




