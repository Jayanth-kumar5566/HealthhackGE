out=read.csv("to_merge1.csv")
nout=read.csv("to_merge2.csv")
final=merge(out,nout,by='PATNO',all=TRUE)
write.csv(final,file="../Drug_prediction/drug_input.csv")
