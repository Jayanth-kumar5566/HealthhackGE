import pandas
#---------Getting scores from the R file---------------
df=pandas.read_csv("../scores.csv")
#------------Selecting only PD patients---------------
del df["Unnamed: 0"]
del df["V1"]
del df["V3"]
del df["V4"]
del df["V5"]
scores=df
#--------Appending the Patient names---------------
df1=pandas.read_csv("../stage1_input.csv")
pre_index=df1.columns.tolist()
pre_index.remove("PATNO")
scores["PATNO"]=pre_index
scores=scores.set_index("PATNO")
#print scores
#--------Running through the scores-------------
treatment={}
patnam=scores.index.tolist()
for i in range(len(patnam)):
    if scores["V2"][i] <= 0.5:
        treatment[patnam[i]]="Healthy"
    elif 0.5 < scores["V2"][i] <=0.75:
        treatment[patnam[i]]="Needs Imaging Analysis"
    else:
        treatment[patnam[i]]="Give Levadopa"
scores["Treatment"]=pandas.Series(treatment)
print scores
scores.to_csv("treatments1.csv")
#--------Adding the new subjects data to the patient------------
old=pandas.read_csv("../data.csv")
old_label=open("../label.csv",'a')
ps_score=pandas.read_csv("Total_score_Metric/Personal_scoring/to_calc_ps.csv")
a=raw_input("Do you wish to change the prediction? ")
if a=="yes":
    pat=raw_input("Please enter the patient name/number? ")
    diag=raw_input("Please input the correct diagnosis? ")
    new_df=df1[["PATNO",pat]]
    new_df=new_df.set_index("PATNO")
    new_df=new_df.transpose()
    old=old.append(new_df)
    ps_score=ps_score.append(new_df)
    ps_score.to_csv("Total_score_Metric/Personal_scoring/to_calc_ps.csv")
    old.to_csv("../data.csv")
    old_label.write(str(diag)+'\n')
    old_label.close()
else:
    pass
