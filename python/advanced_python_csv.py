import pandas as pd

df = pd.read_csv('/Users/andrewvlahutin/ds/metis/prework/dsp/python/faculty.csv')

###q5

df.to_csv("/Users/andrewvlahutin/ds/metis/prework/dsp/python/emails.csv",header=False,index=False,columns=[' email'])
