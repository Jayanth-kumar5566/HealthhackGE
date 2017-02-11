require(data.table)
require(xgboost)
# Convert your data file into .csv format
filename <- "data.csv"
data <- read.csv("prog_data.csv")
label<-read.csv("labels.csv")
prediction<-read.csv("prog_data_pred.csv")
names<-strsplit(colnames(prediction),",")
#------------------------Transposing the Columns---------------------------
# first remember the names
n <- prediction$PATNO
# transpose all but the first column (name)
prediction <- as.data.frame(t(prediction[,-1]))
colnames(prediction) <- n
prediction$myfactor <- factor(row.names(prediction))
prediction<-prediction[1:123]
prediction<-as.matrix(prediction)
#---------------------------------------------------------------------------
data<-data.table(sapply(data,as.numeric))
label<-data.table(sapply(label,as.numeric))
data<-as.matrix(data)
label<-as.matrix(label)
set.seed(42)
n<-dim(data)[1]
trind<-sample(1:n,floor(.7*n),FALSE)
teind<-setdiff(1:n,trind)
tdata=data[teind,]
tlabel=label[teind,]#Actual data
data=data[trind,]
label=label[trind,]
#----------------------Training the Classifier-------------------------------
bst <- xgboost(data = data,label =label,eta =0.5,max.depth = 7, nround = 400,objective = "multi:softprob", num_class =max(label,na.rm=TRUE)+1 ,nthread = 3, verbose = 1,missing=NA)
# we input data as our testing set
test_data=tdata
test_label=tlabel
x=dim(test_data)[1]
preds <- predict(bst,test_data,missing=NA) # returns probabilities of each label
# needs to find max probability label for each dataline
predsmat <- matrix(preds,x,max(test_label)+1, byrow = T)

predictedlab <- list()
for (i in 1:x){predictedlab <- c(predictedlab,which(predsmat[i,]==max(predsmat[i,]))-1)}
print("Confusion Matrix for the Testing Set")
table(unlist(predictedlab),tlabel)
#-------------------Variable importance plot----------------------------------
print("Saving variable Importance Plot")
importance_matrix<-xgb.importance(colnames(data),model=bst,data=data,label=label)
library("Ckmeans.1d.dp", lib.loc="/home/jhome/R/x86_64-pc-linux-gnu-library/3.1")
xgb.plot.importance(importance_matrix[1:45])
#----------------Prediction from the table------------------------------------
n_preds <- predict(bst,prediction,missing=NA)
n_predsmat <- matrix(n_preds,dim(prediction)[1],max(test_label)+1, byrow = T) 
n_predictedlab <- list()
write.csv(n_predsmat,file="predictions.csv")
for (i in 1:dim(prediction)[1]){n_predictedlab <- c(n_predictedlab,which(n_predsmat[i,]==max(n_predsmat[i,]))-1)}
print("Prediction of the Patient")
names(n_predictedlab)<-names[-1]
print(n_predictedlab)

