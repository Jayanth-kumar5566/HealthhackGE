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
p1_eff=[]
p2_eff=[]
#-Uses Linear Regression along with least squares(On training dataset)--------
for i in range(X.shape[0]):
    val=X.iloc[i].tolist()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,val)
    m.append(slope)
    x_0.append(intercept)
    p2_eff.append(val[-2])
    p1_eff.append(val[-1])
df1=pandas.DataFrame(index=Y)
df1["Intercept"]=x_0
df1["Progression"]=m
df1["Penaltimate Visit"]=p2_eff
df1["This time Visit"]=p1_eff
df1["Diff"]=df1["This time Visit"]-df1["Penaltimate Visit"]
df1.to_csv("prog_data.csv")

#-------------------------On Testing dataset--------------------
ddf=pandas.read_csv("drug_input.csv")
del ddf["Unnamed: 0"]
Y=ddf["PATNO"]
del ddf["PATNO"]
X=ddf
x=range(X.shape[1])
m=[]
x_0=[]
p1_eff=[]
p2_eff=[]
#-----OLS Regression-------------------------------------
row_num=[]
for i in range(X.shape[0]):
    val=X.iloc[i].tolist()
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,val)
    m.append(slope)
    x_0.append(intercept)
    if len(val)>=2:
    	p2_eff.append(val[-2])
    	p1_eff.append(val[-1])
    elif len(val)== 12:
    	a=raw_input("Do you want to add this to the training? ")
    	if a == "yes":
          row_num.append(i)      		
    	else:
            pass
    else:
    	p2_eff.append(val[-1]) # Assuming no progression, since not able to calulate
    	p1_eff.append(val[-1])
    	print "Number of Visits less than 2 adding diff = 0"
    	pass
ddf1=pandas.DataFrame(index=Y)
ddf1["Intercept"]=x_0
ddf1["Progression"]=m
ddf1["Penaltimate Visit"]=p2_eff
ddf1["This time Visit"]=p1_eff
ddf1["Diff"]=ddf1["This time Visit"]-ddf1["Penaltimate Visit"]
ddf1.to_csv("prog_data_pred.csv")
#--------------Dynamicity--------------------------
cf=pandas.DataFrame()
for i in row_num:
    cf[Y[i]]=X.iloc[i]
cf=cf.transpose()
cf.to_csv("to_merge.csv")
