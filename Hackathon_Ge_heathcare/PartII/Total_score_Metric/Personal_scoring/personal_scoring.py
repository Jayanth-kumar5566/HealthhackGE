
# coding: utf-8

# # This code predicts weather a person is likely to have diabetes or not based on his features

# ### Importing libraries

# In[29]:

import numpy as np
import pandas 
import matplotlib.pyplot as plt
from sklearn import preprocessing

# In[40]:
#Input in data because we use average and standard deviation of the population to normalize the values
df=pandas.read_csv("data.csv")
df=df.set_index("PATNO")
#index=df.index
#columns=df.columns
ddf=pandas.read_csv("../../../stage1_input.csv")
ddf=ddf.set_index("PATNO")
ddf=ddf.transpose()
out=pandas.read_csv("../Drug_prediction/drug_input.csv")
#-------------Normalizing the data--------------
ddf=(ddf-df.mean())/df.var()
inp=raw_input("Would you like to add the patients to training set? ")
if inp=="yes":
    df=df.append(ddf)
    df.to_csv("data.csv")
else:
    pass
nout=pandas.DataFrame()
visit=raw_input("Which visit is it? ")
nout[str(visit)]=ddf.mean(axis=1)
nout["PATNO"]=ddf.index
out=out.set_index("PATNO")
nout=nout.set_index("PATNO")
out.to_csv("to_merge1.csv")
nout.to_csv("to_merge2.csv")
print "Done created personal scoring"
