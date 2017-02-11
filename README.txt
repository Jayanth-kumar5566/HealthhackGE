 ============ How to Predict disease================
    
We provide a tar file named "GE_HealthHack.tar" 
which contains R and Python scripts that will assist the clinician 
in diagnosing a patient.

The model here is trained on Parkinson's dataset

The R script classifies a subject into is PD,healthy or inconclusive.
This model then follows the progression of a PD patient from the first visit 
in terms of personalised score. This progression marker along with the 
personalised score is used to decide the drug or treatment that is to be 
administerd to the patient.

=======================Features=============================
1)Training uses 70 % of the data) and testing uses the remaining data on each
 run. The results of testing are printed out in a confusion matrix.

2)Feature importance plots are saved into the directory on each
  run as "Rplots.pdf".
======================Installation===========================

1)Download and install R from "http://lib.stat.cmu.edu/R/CRAN/" for 
your appropriate distribution.
 
2)Install following R packages from CRAN repository
    a) xgboost
    b) data.table
    c) Ckmeans.1d.dp

3)Download and install following Python packages(Assuming Python 2.7)
	a)Python-Pandas
	b)Scipy
	c)SkLearn
	d)Matplotlib

======================How to use============================
 
 1)Untar "GE_HealthHack.tar", on Linux based 
 system navigate to the directory containing "PPMI.tar" and type the 
 following command in the terminal:
 
			"tar -xvf GE_HealthHack.tar"
			
This will create a folder named "Hackathon Ge_healthcare" in the directory 
from which the command was executed.


2)Navigate to the directory "Stage1". This will be used to classify patients into 
PD, healthy, SWEDD or prodromal). This directory contains one R script and three csv
files. The user has to enter the test results for tests mentioned in the 
"stage1_input.csv" of the patient in the "stage1_input.csv" and save the file. 
If there are any tests for which the results is not known, leave that entry blank.
An example data of a test patient is filled in the file 
(which should be deleted when entering patient data). 
The other two csv files ("data.csv","label.csv") are the ones used
for the training and testing of the algorithm . It is important 
NOT to change "data.csv" and "label.csv" unless you know what you are doing.


3)To run the R script. On Linux-based systems, open a terminal
and navigate to the directory "Stage1" and type the following command: 

		"RScript 4wayclassification.R"

This should print out an integer between 0 and 4 for each patient
 filled in the "stage1_input.csv" which is to be interpreted as follows:
         
           	1 -----------> PD Patient
         	2 -----------> Healthy Control
         	3 -----------> Swedd
         	4 -----------> Prodormal
         
   
   
4)To predict the progression of a PD patient, navigate to the
directory "Stage2". 

Note: If the user "knows" a patient is PD then they can ignore Stage1 
and directly proceed to Stage2. 

This directory contains 1 Rscript and 2 csv files, the user has to
enter the baseline test results of the patient for tests
mentioned in the "stage2_input.csv" in the "stage2_input.csv"
and save the file. If there are any missing values, leave the
entry blank. An example data of a test patient is already filled
in the file. "lastfile_smoted_numerical.csv" is the file on
which the classifier is trained and tested. 
Do NOT change lastfile_smoted_numerical.csv unless absolutely necessary.
          

5)To run the Rscript, On Linux based system, open terminal and navigate to
the directory "Stage2" and type the following command: 

		"RScript xgboost.R" 
		
This should print out an integer between 1 and 3 for each patient
filled in the "stage2_input.csv", which is interpreted as follows:       
       	
       	1 --------> TAP1 Low progression rate relative to the population mean 
       	2 --------> TAP2 An average progression rate 
       	3 --------> TAP3 High progression rate relative to the population mean


