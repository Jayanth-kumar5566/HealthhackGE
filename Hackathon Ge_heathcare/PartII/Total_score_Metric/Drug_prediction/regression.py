import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy import stats
df=pandas.read_csv("data.csv")
Y=df["PATNO"]
del df["PATNO"]
X=df
x=range(X.shape[1])
m=[]
x_0=[]
#-Uses Linear Regression along with least squares(On training dataset)--------
for i in range(X.shape[0]):
    val=X.iloc[i].tolist()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,val)
    m.append(slope)
    x_0.append(intercept)
df1=pandas.DataFrame(index=Y)
df1["Intercept"]=x_0
df1["Progression"]=m
df1.to_csv("prog_data.csv")

#-------------------------On Testing dataset--------------------
ddf=pandas.read_csv("drug_input.csv")
Y=ddf["PATNO"]
del ddf["PATNO"]
X=ddf
x=range(X.shape[1])
m=[]
x_0=[]
#-----OLS Regression-------------------------------------
for i in range(X.shape[0]):
    val=X.iloc[i].tolist()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,val)
    m.append(slope)
    x_0.append(intercept)
ddf1=pandas.DataFrame(index=Y)
ddf1["Intercept"]=x_0
ddf1["Progression"]=m
ddf1.to_csv("prog_data_pred.csv")

