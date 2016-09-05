import pandas as pd
from itertools import islice

df = pd.read_csv('/Users/andrewvlahutin/ds/metis/prework/dsp/python/faculty.csv')

#print(df.info())

### q6
#creates a list where last name is first element
listByLast = map(lambda n,d,t,e: [n.split()[-1:][0],d.strip(),t.strip(),e.strip()], df['name'],df[' degree'],df[' title'],df[' email'])

faculty_dict = {}
for prof in listByLast:
    key = prof[0]
    if key in faculty_dict:
        #already there, add to the list
        value = faculty_dict.get(key) + [prof[1:]]
    else:
        #not there, take the 2nd and rest of list
        value = [prof[1:]]
    faculty_dict[key] = value

n_items = list(islice(faculty_dict.items(), 3))
print(n_items)
#print(faculty_dict["Li"])
#print(faculty_dict["Ellenberg"])
print("#"*10)

### q7
#creates a list where tuple of first, last name is first element
listByFirstLast = map(lambda n,d,t,e: [(n.split()[0],n.split()[-1:][0]),d.strip(),t.strip(),e.strip()], df['name'],df[' degree'],df[' title'],df[' email'])
#transfrom into dictionary. since key is first,last, no need to handle duplicates
professor_dict = {prof[0]:[prof[1:]] for prof in listByFirstLast}

n_items2 = list(islice(professor_dict.items(), 3))
print(n_items2)

#print(faculty_dict2[('Susan','Ellenberg')])
print("#"*10)
### q8

dictkeys = professor_dict.keys()
#sort by last name
sortKeys = sorted(dictkeys, key=lambda tup: tup[1])

for key in sortKeys:
    print(key, professor_dict[key])


print('done')
