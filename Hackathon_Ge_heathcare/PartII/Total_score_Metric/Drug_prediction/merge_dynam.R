print("Merging if there are 15 visits")
cdf1=read.csv("to_merge.csv")
colnames(cdf1)[1] <- "PATNO"
cdf2=read.csv("data.csv")
final=merge(cdf1,cdf2,by='PATNO',all=TRUE)
write.csv(final,file="data.csv")
