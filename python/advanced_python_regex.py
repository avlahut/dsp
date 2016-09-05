import pandas as pd
from itertools import groupby

df = pd.read_csv('/Users/andrewvlahutin/ds/metis/prework/dsp/python/faculty.csv')

### Q1
degreeList = df[' degree']
#remove all periods
degreeList = [x.replace('.','') for x in degreeList]
#standardize on uppercase
degreeList = [x.upper() for x in degreeList]
#strip out leading and trailing spaces
degreeList = [x.strip(' ') for x in degreeList]

#identify any strings where the list appears to have more than one degree
multipleDegrees = [x for x in degreeList if len(x) > 3]
#split the multiple degrees and add to list
for deg in multipleDegrees:
     words = deg.split();
     degreeList.remove(deg)
     degreeList.extend(words)
#sort the lsit
degreeList = sorted(degreeList)
#groupby values in degreeList, sum up the count of each
sums = [(i,sum(1 for _ in j)) for i,j in groupby(degreeList)]
[print(i,':',j) for i,j in sums]

### Q2
#titleGrp = pd.DataFrame({'count' : df.groupby( [ " title"]).size()}).reset_index()
titleGrp = pd.DataFrame({'count' : df.groupby([ " title"]).size()}).reset_index()

print(titleGrp)

### Q3
emailList = df[ ' email'].values
print(emailList)


### Q4
domainSet = set()
for email in emailList:
    domain = email.split('@')[1]
    domainSet.add(domain)

print(domainSet)
